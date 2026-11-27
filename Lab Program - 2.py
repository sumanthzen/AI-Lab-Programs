
import heapq

initial = (2, 8, 3,
           1, 6, 4,
           7, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


# Case 1: Number of misplaced tiles
def misplaced(state):
    return sum(state[i] != goal[i] for i in range(9))


# Case 2: Manhattan distance
def manhattan(state):
    distance = 0

    for i, tile in enumerate(state):
        goal_pos = goal.index(tile)

        distance += abs(i // 3 - goal_pos // 3)
        distance += abs(i % 3 - goal_pos % 3)

    return distance


# Generate valid successor states
def neighbors(state):
    zero = state.index(0)
    r, c = divmod(zero, 3)

    for move, dr, dc in [
        ("Up", -1, 0),
        ("Down", 1, 0),
        ("Left", 0, -1),
        ("Right", 0, 1)
    ]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            pos = nr * 3 + nc
            board = list(state)
            board[zero], board[pos] = board[pos], board[zero]
            yield move, tuple(board)


# A* Search
def astar(heuristic, name):
    pq = [(heuristic(initial), 0, initial)]
    parent = {initial: (None, None)}
    cost = {initial: 0}
    visited = set()

    while pq:
        f, g, state = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            break

        for move, nxt in neighbors(state):
            new_g = g + 1

            if new_g < cost.get(nxt, float("inf")):
                cost[nxt] = new_g
                parent[nxt] = (state, move)
                new_f = new_g + heuristic(nxt)
                heapq.heappush(pq, (new_f, new_g, nxt))
    else:
        print("No solution found")
        return

    # Reconstruct solution path
    path = []
    state = goal

    while state is not None:
        prev, move = parent[state]
        path.append((state, move))
        state = prev

    path.reverse()

    print("\n", name)
    print("Solution steps:", len(path) - 1)

    for step, (state, move) in enumerate(path):
        g = step
        h = heuristic(state)
        f = g + h

        print("\nStep:", step, "| Move:", move)
        print("g =", g, "h =", h, "f =", f)

        for i in range(0, 9, 3):
            print(state[i:i + 3])


astar(misplaced, "CASE 1: Misplaced Tiles")
astar(manhattan, "CASE 2: Manhattan Distance")
