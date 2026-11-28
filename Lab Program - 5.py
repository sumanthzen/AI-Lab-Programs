
import random
import math

N = 8

# Count attacking pairs of queens
def count_conflicts(state):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

# Generate a neighbouring state
def get_neighbor(state):
    new_state = state[:]
    col = random.randint(0, N - 1)
    new_row = random.randint(0, N - 1)
    new_state[col] = new_row
    return new_state

# Simulated Annealing algorithm
def simulated_annealing():
    current = [random.randint(0, N - 1) for _ in range(N)]
    current_cost = count_conflicts(current)

    T = 100.0
    cooling_rate = 0.995

    while T > 0.1 and current_cost != 0:
        next_state = get_neighbor(current)
        next_cost = count_conflicts(next_state)

        delta_E = current_cost - next_cost

        if delta_E > 0:
            current = next_state
            current_cost = next_cost
        else:
            probability = math.exp(delta_E / T)

            if random.random() < probability:
                current = next_state
                current_cost = next_cost

        T = T * cooling_rate

    return current, current_cost

# Repeat until a solution is found
while True:
    solution, conflicts = simulated_annealing()
    if conflicts == 0:
        break

print("Final Board Configuration:", solution)
print("Number of Conflicts:", conflicts)

# Display chessboard
for row in range(N):
    for col in range(N):
        if solution[col] == row:
            print(" Q ", end="")
        else:
            print(" . ", end="")
    print()
