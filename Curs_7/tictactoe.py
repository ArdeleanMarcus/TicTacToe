import random

from tkinter import Tk, PhotoImage, Label, Frame, TOP, BOTH
from tkinter.font import Font
from tkinter import Button


BOARD_SIZE = 3


class Player:
    """Contains players details"""
    def __init__(self, label: str, sprite: PhotoImage):
        self.label = label
        self.sprite = sprite


class TicTacToeService:
    """Has the 'backend' logic"""
    board = list()
    players: tuple
    current_player: Player
    player_won: bool = False

    def __init__(self, board_size: int = BOARD_SIZE):
        self.board_size = board_size

    def change_player(self) -> None:
        """
        Changes player's turn / Changes active player.
        :return: None
        """
        # Check if current player is X
        if self.current_player.label == "X":
            # If current player is X, change it with player 0
            self.current_player = self.players[1]
        else:
            # If current player is not X, change it to player X
            self.current_player = self.players[0]


class TicTacToeBoard(Tk, TicTacToeService):
    """Has the 'frontend' logic"""
    game_title: Label
    game_start_button: Button
    game_grid: Frame
    game_end_frame: Frame
    cells: dict = dict()

    def __init__(self):
        Tk.__init__(self)  # Initialise tkinter
        TicTacToeService.__init__(self)  # Initialise the "backend" of the game

        self.title("Tic-Tac-Toe")  # Set window title
        self.minsize(600, 600)  # Set window size
        self.aspect(1, 1, 1, 1)  # Set default window aspect ratio to square
        self.__create_players()  # Create X and 0 players
        self.__get_first_random_player()  # Get a random first player
        self.__start_menu()  # Display the start menu

    def __create_players(self) -> None:
        # Import player sprites
        player_x = PhotoImage(file=r"/Users/marcusardelean/Desktop/_/X.png")
        player_0 = PhotoImage(file="/Users/marcusardelean/Desktop/_/0.png")

        # Resize sprite to fit button
        player_x = player_x.subsample(1)
        player_0 = player_0.subsample(1)

        # Create X and 0 player instances
        self.players = (
            Player(label="X", sprite=player_x),
            Player(label="0", sprite=player_0)
        )

    def __get_first_random_player(self):
        # Using the choice method from the random module, get a random player
        # to start the game
        self.current_player = random.choice(self.players)

    def __start_menu(self) -> None:
        """
        This menu will be displayed at the start of each game.
        :return: None
        """
        # Create game title
        self.game_title = Label(
            master=self,
            text="Are you ready ?",
            font=Font(size=28, weight="bold")
        )
        # Display game title
        self.game_title.pack()

        # Create start game button
        self.game_start_button = Button(
            master=self,
            text="Start",
            command=self.__create_board_grid  # This function will get executed when the button is pressed
        )
        # Display start game button
        self.game_start_button.pack()

    def end_menu(self):
        """This menu will be displayed at the end of each game."""
        # Remove game grid cells
        self.game_grid.pack_forget()

        # Create and display game end frame
        self.game_end_frame = Frame(master=self)
        self.game_end_frame.pack()

        # Create and display the "play again" button.
        play_again_btn = Button(
            master=self.game_end_frame,
            text="Play again?",
            command=self.reset_board  # This function will get executed when the button is pressed
        )
        play_again_btn.pack()

        # Create and display the "exit" button.
        exit_btn = Button(
            master=self.game_end_frame,
            text="Exit",
            command=self.destroy  # This function will get executed when the button is pressed
        )
        exit_btn.pack()

    def reset_board(self):
        """Reset the game's board to play again."""
        # Remove tha game end frame
        self.game_end_frame.pack_forget()
        # Reset games board, cells and the change the player_won flag to False
        self.reset_game()
        # Update the display message
        self.__update_display(message="Are you ready ?")
        # Create the board grid again
        self.__create_board_grid()

    def reset_game(self):
        """Reset the game state to play again."""
        # Remove all player moves
        self.board = list()
        # Remove button cells
        self.cells = dict()
        # Set player_won flag back to False
        self.player_won = False

    def __create_board_grid(self):
        # Remove start game button
        self.game_start_button.pack_forget()

        # Update display with current player.
        self.__update_display(
            message=f"Player's {self.current_player.label} turn"
        )

        # Create and display games main grid frame
        self.game_grid = Frame(master=self)
        self.game_grid.pack(side=TOP, fill=BOTH, expand=True)

        for row in range(self.board_size):
            # Create board game row
            board_row = list()

            for column in range(self.board_size):
                # weight ensures the row and column expand at the same rate when
                # the window is resized
                self.game_grid.columnconfigure(column, weight=1)
                self.game_grid.rowconfigure(row, weight=1)

                button = Button(
                    master=self.game_grid,
                    compound=TOP,
                    highlightbackground="#9EDECB"
                )

                # Store button in a cells dictionary
                self.cells[button] = (row, column)

                # Display button
                button.bind("<ButtonPress-1>", self.play)
                button.grid(
                    row=row,
                    column=column,
                    padx=3,
                    pady=3,
                    sticky="NSEW"
                )

                # Add empty elements to the row
                board_row.append("")

            # Store row in board
            self.board.append(board_row)

    def __update_display(self, message: str) -> None:
        """
        Updates game title with a custom message.
        :param message: Message to be displayed
        :return: None
        """
        self.game_title["text"] = message

    def play(self, event):
        # Catch a button press event.
        clicked_btn = event.widget

        # Get the row and column of the pressed button.
        row, column = self.cells[clicked_btn]

        # Check if move is valid
        # Display players move
        # Process move
        # Check if player won
        # Check if game is tied
        # Change player and continue game


if __name__ == "__main__":
    game_board = TicTacToeBoard()
    game_board.mainloop()
