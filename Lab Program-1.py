import random

# ---------------------------------------------------------
# TIC-TAC-TOE GAME (Human vs Computer)
# The computer selects a random empty position, as in the
# algorithm shown in the lab notebook.
# ---------------------------------------------------------

def display_board(board):
    print("\n")
    for row in range(3):
        print(" " + " | ".join(board[row]))
        if row < 2:
            print("---+---+---")
    print()


def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    # Check both diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_draw(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    print("\n========== TIC-TAC-TOE ==========")

    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        human_symbol = input("Choose your symbol (X/O): ").strip().upper()
        if human_symbol in ("X", "O"):
            break
        print("Invalid choice. Please enter X or O.")

    computer_symbol = "O" if human_symbol == "X" else "X"
    current_turn = "X"  # X always makes the first move

    print(f"You are {human_symbol}; computer is {computer_symbol}.")
    print("Enter row and column values from 1 to 3.")

    game_over = False

    while not game_over:
        display_board(board)

        if current_turn == human_symbol:
            # Human move
            while True:
                try:
                    row = int(input("Enter row (1-3): ")) - 1
                    col = int(input("Enter column (1-3): ")) - 1

                    if not (0 <= row < 3 and 0 <= col < 3):
                        print("Position out of range. Try again.")
                    elif board[row][col] != " ":
                        print("That position is already occupied. Try again.")
                    else:
                        break
                except ValueError:
                    print("Please enter valid numbers.")

            board[row][col] = human_symbol

            if check_win(board, human_symbol):
                display_board(board)
                print("Congratulations! You win the game.")
                game_over = True
            elif check_draw(board):
                display_board(board)
                print("The game is a draw.")
                game_over = True
            else:
                current_turn = computer_symbol

        else:
            # Computer move: choose one random empty cell
            print("Computer is making a move...")
            empty_positions = [
                (r, c)
                for r in range(3)
                for c in range(3)
                if board[r][c] == " "
            ]

            row, col = random.choice(empty_positions)
            board[row][col] = computer_symbol
            print(f"Computer placed {computer_symbol} at row {row + 1}, column {col + 1}.")

            if check_win(board, computer_symbol):
                display_board(board)
                print("Computer wins the game.")
                game_over = True
            elif check_draw(board):
                display_board(board)
                print("The game is a draw.")
                game_over = True
            else:
                current_turn = human_symbol


# ---------------------------------------------------------
# VACUUM CLEANER ENVIRONMENT
# Room status: 1 = Dirty, 0 = Clean
# ---------------------------------------------------------

def display_environment(status):
    print(f"Room A: {'Dirty' if status['A'] == 1 else 'Clean'}")
    print(f"Room B: {'Dirty' if status['B'] == 1 else 'Clean'}")


def other_room(room):
    return "B" if room == "A" else "A"


# ---------------------------------------------------------
# 1. SIMPLE REFLEX VACUUM AGENT
# It acts only on the current room's perceived status:
# Dirty -> Suck; Clean -> Move to the other room.
# The notebook uses three perception-action cycles.
# ---------------------------------------------------------

def simple_reflex_vacuum_agent():
    print("\n====== SIMPLE REFLEX VACUUM AGENT ======")

    status = {
        "A": random.randint(0, 1),
        "B": random.randint(0, 1)
    }
    agent_location = random.choice(["A", "B"])
    performance_cost = 0

    print("\nInitial environment:")
    display_environment(status)
    print("Initial agent location: Room", agent_location)

    for step in range(1, 4):
        current_room = agent_location
        percept_status = status[current_room]

        print(f"\nStep {step}: Agent is in Room {current_room}")

        if percept_status == 1:
            print(f"Room {current_room} is Dirty.")
            print("Action: Suck")
            status[current_room] = 0
            performance_cost += 1
        else:
            print(f"Room {current_room} is Clean.")
            next_room = other_room(current_room)
            print(f"Action: Move to Room {next_room}")
            agent_location = next_room
            performance_cost += 1

        print("Current environment:")
        display_environment(status)
        print("Agent location: Room", agent_location)
        print("Performance cost:", performance_cost)

    print("\nSimple Reflex Agent finished.")
    print("Final environment:")
    display_environment(status)
    print("Total performance cost:", performance_cost)


# ---------------------------------------------------------
# 2. GOAL-BASED VACUUM AGENT
# Goal: Both Room A and Room B must be clean.
# The agent keeps acting until the goal state is reached.
# ---------------------------------------------------------

def goal_based_vacuum_agent():
    print("\n====== GOAL-BASED VACUUM AGENT ======")

    status = {
        "A": random.randint(0, 1),
        "B": random.randint(0, 1)
    }
    agent_location = random.choice(["A", "B"])
    performance_cost = 0

    print("\nInitial environment:")
    display_environment(status)
    print("Initial agent location: Room", agent_location)

    # Continue while at least one room is dirty
    while status["A"] == 1 or status["B"] == 1:
        current_room = agent_location

        if status[current_room] == 1:
            print(f"\nGoal evaluation: Room {current_room} is Dirty.")
            print("Action: Suck")
            status[current_room] = 0
            performance_cost += 1
        else:
            next_room = other_room(current_room)
            print(f"\nGoal evaluation: Room {current_room} is Clean.")
            print(f"Navigating to Room {next_room}.")
            agent_location = next_room
            performance_cost += 1

        print("Current environment:")
        display_environment(status)
        print("Agent location: Room", agent_location)
        print("Performance cost:", performance_cost)

    print("\nGoal reached: Both rooms are Clean.")
    print("Final environment:")
    display_environment(status)
    print("Total performance cost:", performance_cost)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main():
    while True:
        print("\n========== AI LAB PROGRAMS ==========")
        print("1. Tic-Tac-Toe Game")
        print("2. Simple Reflex Vacuum Cleaner Agent")
        print("3. Goal-Based Vacuum Cleaner Agent")
        print("4. Run all vacuum cleaner agents")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            tic_tac_toe()
        elif choice == "2":
            simple_reflex_vacuum_agent()
        elif choice == "3":
            goal_based_vacuum_agent()
        elif choice == "4":
            simple_reflex_vacuum_agent()
            goal_based_vacuum_agent()
        elif choice == "5":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
