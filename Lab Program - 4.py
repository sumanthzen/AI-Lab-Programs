
import random

N = 4

def heuristic(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def hill_climbing():
    while True:
        state = [random.randint(0, N - 1) for _ in range(N)]

        while True:
            h = heuristic(state)

            if h == 0:
                return state

            best_state = state[:]
            best_h = h

            for col in range(N):
                for row in range(N):
                    if row != state[col]:
                        neighbor = state[:]
                        neighbor[col] = row
                        neighbor_h = heuristic(neighbor)

                        if neighbor_h < best_h:
                            best_state = neighbor
                            best_h = neighbor_h

            if best_state == state:
                break

            state = best_state


def display_board(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


solution = hill_climbing()

print("Solution:", solution)
print("Heuristic:", heuristic(solution))
print("Chessboard:")
display_board(solution)
