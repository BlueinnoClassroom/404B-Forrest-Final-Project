import random

# Function to create a new board
def create_board(size):
    board = []
    for _ in range(size):
        board.append(["O"] * size)
    return board

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to place ships on the board
def place_ship(board, row, col, direction, length):
    if direction == "horizontal":
        for i in range(length):
            board[row][col+i] = "#"
    elif direction == "vertical":
        for i in range(length):
            board[row+i][col] = "#"

# Function to play the game
def play_battleship():
    # Input from the user
    size = int(input("Enter the size of the board: "))
    ship_amount = 0
    ship_lengths = []

    while True:
        ship_amount = int(input("Enter the number of ships: "))
        if ship_amount <= size:
            break
        else:
            print("Invalid ship amount. The number of ships cannot exceed the board size.")

    for i in range(ship_amount):
        while True:
            length = int(input("Enter the length of ship {}: ".format(i+1)))
            if length > 0 and length <= size:
                ship_lengths.append(length)
                break
            else:
                print("Invalid ship length. Please enter a positive value less than or equal to the board size.")

    board = create_board(size)
    ships = []
    for length in ship_lengths:
        while True:
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            direction = random.choice(["horizontal", "vertical"])
            if direction == "horizontal" and col + length <= size:
                if all(board[row][col+i] == "O" for i in range(length)):
                    place_ship(board, row, col, direction, length)
                    ships.append(length)
                    break
            elif direction == "vertical" and row + length <= size:
                if all(board[row+i][col] == "O" for i in range(length)):
                    place_ship(board, row, col, direction, length)
                    ships.append(length)
                    break

    print("All ships placed!")
    hidden_board = create_board(size)
    print_board(hidden_board)

    # Game loop
    while True:
        row_guess = int(input("Enter the row coordinate to guess (0 to {}): ".format(size - 1)))
        col_guess = int(input("Enter the column coordinate to guess (0 to {}): ".format(size - 1)))

        if row_guess < 0 or row_guess >= size or col_guess < 0 or col_guess >= size:
            print("Invalid coordinates. Please enter valid coordinates.")
            continue

        if hidden_board[row_guess][col_guess] == "X":
            print("You've already guessed this coordinate. Try again.")
        elif board[row_guess][col_guess] == "#":
            print("Hit!")
            hidden_board[row_guess][col_guess] = "X"
            print_board(hidden_board)
        else:
            print("Miss!")
            hidden_board[row_guess][col_guess] = "-"

        # Check if all ships are sunk
        if all(ship_length == 0 for ship_length in ships):
            print("Congratulations! You've sunk all the ships!")
            break

        # Update ship lengths
        for i, ship_length in enumerate(ships):
            if ship_length > 0:
                ships[i] = ship_length - 1

# Play the game
play_battleship()
