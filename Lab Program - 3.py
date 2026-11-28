
import heapq

# Initial and goal states
initial = (1, 2, 3,
           4, 0, 6,
           7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Heuristic 1: Misplaced Tiles
def misplaced_tiles(state, goal):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


# Heuristic 2: Manhattan Distance
def manhattan_distance(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            x1, y1 = divmod(i, 3)
            j = goal.index(state[i])
            x2, y2 = divmod(j, 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Generate neighboring states
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0),
             (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* Search Algorithm
def astar(initial, goal, heuristic):
    open_list = []

    heapq.heappush(open_list, (0, initial))

    g = {initial: 0}
    parent = {initial: None}

    closed = set()

    while open_list:

        f, current = heapq.heappop(open_list)

        if current in closed:
            continue

        # Check goal state
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        closed.add(current)

        # Generate successors
        for neighbor in get_neighbors(current):

            if neighbor in closed:
                continue

            new_g = g[current] + 1
            new_f = new_g + heuristic(neighbor, goal)

            if neighbor not in g or new_g < g[neighbor]:

                g[neighbor] = new_g
                parent[neighbor] = current

                heapq.heappush(
                    open_list, (new_f, neighbor)
                )

    return None


# Display solution
def display(path):
    if path is None:
        print("No solution found")
        return

    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for step, state in enumerate(path):
        print("\nStep", step)
        for i in range(0, 9, 3):
            print(state[i:i+3])


# Execute A* using Misplaced Tiles
print("A* SEARCH - MISPLACED TILES")
path = astar(initial, goal, misplaced_tiles)
display(path)


# Execute A* using Manhattan Distance
print("\nA* SEARCH - MANHATTAN DISTANCE")
path = astar(initial, goal, manhattan_distance)
display(path)
