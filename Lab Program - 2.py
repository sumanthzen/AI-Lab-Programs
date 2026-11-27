

# 8 Puzzle using Depth First Search (DFS)

initial = (1, 2, 3,
           0, 4, 6,
           7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Generate possible next states
def get_neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    neighbors = []

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c

            board = list(state)
            board[zero], board[pos] = board[pos], board[zero]

            neighbors.append(tuple(board))

    return neighbors


# Display the puzzle
def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# DFS Algorithm
def dfs(initial, goal):

    stack = [(initial, [initial])]
    visited = {initial}

    while stack:

        state, path = stack.pop()

        if state == goal:
            return path

        # Reverse insertion to explore Up first
        for next_state in reversed(get_neighbors(state)):

            if next_state not in visited:
                visited.add(next_state)

                new_path = path + [next_state]

                stack.append((next_state, new_path))

    return None


# Main Program
print("8 PUZZLE USING DFS")

solution = dfs(initial, goal)

if solution:
    print("Goal Found!")
    print("Number of moves:", len(solution) - 1)

    for step, state in enumerate(solution):
        print("Step", step)
        display(state)

else:
    print("No solution found")
