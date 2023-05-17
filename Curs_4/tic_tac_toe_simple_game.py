import random

# Create players
players = ["X", "0"]


# Create board game
def create_board() -> list:
    """
    The board game will be a matrix made up from 3 rows and 3 columns. This
    means having 3 lists (which will be the rows of the board) and each list
    will have 3 elements.
    :return: the board game
    """
    board = list()

    for row in range(3):
        # Create a row
        row = list()

        # Add 3 "empty" items to it.
        for element in range(3):
            # "-" means that the item was not taken by "X" or "0"
            row.append("-")

        # Add row to board
        board.append(row)

    return board


def print_board(board) -> None:
    """
    Function to display the elements of the board.
    :param board: board game
    :return: Nothing / None
    """
    for row in board:
        for item in row:
            print(item, end=" ")
        print()


def choose_random_player(players_list: list) -> str:
    """
    Using the choice() method from the random module, return a random player
    from the players list.
    :param players_list: list of game players
    :return: a random player
    """
    player = random.choice(players_list)

    return player


def get_players_move(player: str, board: list) -> None:
    """
    Get player's move, validate it and if the input values are ok, store players
    move on the board.
    :param player: current player
    :param board: board game
    :return: nothing / None
    """
    # Ask for player input untill the data entered is correct/valid
    while True:
        # Get row and column
        row, column = input("Enter row and column: ").split()

        # Change row and column data type from str to int
        row = int(row)
        column = int(column)

        # Check if row and column are within the accepted values.
        if row > 2 or row < 0 or column > 2 or column < 0:
            print("Row and column must be between 0 and 2")
            continue

        # Check if board position is not already taken by the other player.
        if board[row][column] == "-":
            # If the position is available exit the loop
            break
        else:
            # If the position is already taken, ask player again for input
            print(f"Position board[{row}][{column}] is already taken.")
            continue

    # After player's move was validated, store it.
    board[row][column] = player


# Create board
board_game = create_board()

# Get first random player
current_player = choose_random_player(players)

# Validate and store player's move
get_players_move(current_player, board_game)

# Prin tboard
print_board(board_game)
