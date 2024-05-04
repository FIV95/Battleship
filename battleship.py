from termcolor import colored, cprint
from player import Player
from boat import Boat

board = [
    # . 1 2 3 4 5 6 7 8 9 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # E
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # F
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # H
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # I
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # J
]

board_dict = {
    "A1": board[0][0],
    "A2": board[0][1],
    "A3": board[0][2],
    "A4": board[0][3],
    "A5": board[0][4],
    "A6": board[0][5],
    "A7": board[0][6],
    "A8": board[0][7],
    "A9": board[0][8],
    "A10": board[0][9],
    "B1": board[1][0],
    "B2": board[1][1],
    "B3": board[1][2],
    "B4": board[1][3],
    "B5": board[1][4],
    "B6": board[1][5],
    "B7": board[1][6],
    "B8": board[1][7],
    "B9": board[1][8],
    "B10": board[1][9],
    "C1": board[2][0],
    "C2": board[2][1],
    "C3": board[2][2],
    "C4": board[2][3],
    "C5": board[2][4],
    "C6": board[2][5],
    "C7": board[2][6],
    "C8": board[2][7],
    "C9": board[2][8],
    "C10": board[2][9],
    "D1": board[3][0],
    "D2": board[3][1],
    "D3": board[3][2],
    "D4": board[3][3],
    "D5": board[3][4],
    "D6": board[3][5],
    "D7": board[3][6],
    "D8": board[3][7],
    "D9": board[3][8],
    "D10": board[3][9],
    "E1": board[4][0],
    "E2": board[4][1],
    "E3": board[4][2],
    "E4": board[4][3],
    "E5": board[4][4],
    "E6": board[4][5],
    "E7": board[4][6],
    "E8": board[4][7],
    "E9": board[4][8],
    "E10": board[4][9],
    "F1": board[5][0],
    "F2": board[5][1],
    "F3": board[5][2],
    "F4": board[5][3],
    "F5": board[5][4],
    "F6": board[5][5],
    "F7": board[5][6],
    "F8": board[5][7],
    "F9": board[5][8],
    "F10": board[5][9],
    "G1": board[6][0],
    "G2": board[6][1],
    "G3": board[6][2],
    "G4": board[6][3],
    "G5": board[6][4],
    "G6": board[6][5],
    "G7": board[6][6],
    "G8": board[6][7],
    "G9": board[6][8],
    "G10": board[6][9],
    "H1": board[7][0],
    "H2": board[7][1],
    "H3": board[7][2],
    "H4": board[7][3],
    "H5": board[7][4],
    "H6": board[7][5],
    "H7": board[7][6],
    "H8": board[7][7],
    "H9": board[7][8],
    "H10": board[7][9],
    "I1": board[8][0],
    "I2": board[8][1],
    "I3": board[8][2],
    "I4": board[8][3],
    "I5": board[8][4],
    "I6": board[8][5],
    "I7": board[8][6],
    "I8": board[8][7],
    "I9": board[8][8],
    "I10": board[8][9],
    "J1": board[9][0],
    "J2": board[9][1],
    "J3": board[9][2],
    "J4": board[9][3],
    "J5": board[9][4],
    "J6": board[9][5],
    "J7": board[9][6],
    "J8": board[9][7],
    "J9": board[9][8],
    "J10": board[9][9],
}


# player will have blank board on game start
# player will fill have their boat positions filled
# computer will automatically place their boats on game start

# need a way to label array positons to something the player understands:
# a-1 = [0][0]

# logic rules:
# boats cannot overlap
# boats can be touching though
# boats can be represented as letters in the matrix
# [0][0]

# 	Carrier 	5 = C
# 	Battleship 	4 = B
# 	Destroyer 	3 = D
# 	Submarine 	3 = S
# 	Patrol Boat 2 = P
# Misses = X
# Empty slots = 0

#! Game Functions


def printSample(board_string, header):
    print(header, end="")
    colored_board = ""
    board_array = board_string.split("\n")  # Split the string into lines
    for i, board in enumerate(board_array):
        newline = (
            "\n" if i > 0 else ""
        )  # Add a newline character at the beginning of each line, except for the first line
        if "||" in board:  # Check if || is in the line
            row_label, board_content = board.split("||", 1)
            colored_board += newline + row_label + "||"
            for char in board_content:
                if char in ["P", "C", "D", "S", "B", "0"]:
                    if char == "P":
                        colored_board += colored(char, "red", on_color="on_light_red")
                    elif char == "C":
                        colored_board += colored(char, "red", "on_light_red")
                    elif char == "D":
                        colored_board += colored(char, "red", on_color="on_light_red")
                    elif char == "S":
                        colored_board += colored(char, "red", on_color="on_light_red")
                    elif char == "B":
                        colored_board += colored(char, "red", on_color="on_light_red")
                    elif char == "0":
                        colored_board += colored(char, "blue", on_color="on_blue")
                else:
                    colored_board += char
        else:
            colored_board += newline + board

    # Print the colored board without a trailing newline on the last line
    colored_board_lines = colored_board.split("\n")
    for i, line in enumerate(colored_board_lines):
        if i == len(colored_board_lines) - 1:  # If this is the last line
            print(line, end="")
        else:
            print(line)


def infoColor(info):
    colored_info = ""
    for char in info:
        if char not in [" ", "|"]:
            colored_info += colored(char, "cyan")
        else:
            colored_info += char
    return colored_info


def printBoard(header, border, board, footer):
    print(header, end="")
    print(border, end="")
    colored_board = ""
    board_array = board.split("\n")
    for i, line in enumerate(board_array):
        if "||" in line:  # Check if || is in the line
            row_label, board_content = line.split("||", 1)
            colored_board += row_label + "||"
            for char in board_content:
                if char in ["X", "#", "!", "0", "D", "F", "G", "H", "I", "J"]:
                    # Add color to char and append it to colored_board
                    if char == "X":
                        colored_board += colored(char, "white")
                    elif char == "#":
                        colored_board += colored(char, "yellow")
                    elif char == "!":
                        colored_board += colored(
                            char, "red", attrs=["concealed"], on_color="on_light_red"
                        )
                    elif char == "0":
                        colored_board += colored(char, "blue", "on_blue")
                else:
                    colored_board += char
            if i != len(board_array) - 1:  # If the current line is not the last line
                colored_board += "\n"
        else:
            colored_board += line
            if i != len(board_array) - 1:  # If the current line is not the last line
                colored_board += "\n"
    print(colored_board, end="")
    print(footer, end="")


def gameStart():
    start_game = "(s) = Start Game"
    info = "(i) = Info"
    quit = "(q) = quit"
    colored_start_game = colored(start_game, "green")
    colored_info = colored(info, "blue")
    colored_quit = colored(quit, "red")
    logo1 = """
          #####################################################################################################
          #                                                                                                   #
          #    ███████████             █████     █████    ████                   █████       ███              #
          #   ░░███░░░░░███           ░░███     ░░███    ░░███                  ░░███       ░░░               #
          #    ░███    ░███  ██████   ███████   ███████   ░███   ██████   █████  ░███████   ████  ████████    #
          #    ░██████████  ░░░░░███ ░░░███░   ░░░███░    ░███  ███░░███ ███░░   ░███░░███ ░░███ ░░███░░███   #
          #    ░███░░░░░███  ███████   ░███      ░███     ░███ ░███████ ░░█████  ░███ ░███  ░███  ░███ ░███   #
          #    ░███    ░███ ███░░███   ░███ ███  ░███ ███ ░███ ░███░░░   ░░░░███ ░███ ░███  ░███  ░███ ░███   #
          #    ███████████ ░░████████  ░░█████   ░░█████  █████░░██████  ██████  ████ █████ █████ ░███████    #
          #   ░░░░░░░░░░░   ░░░░░░░░    ░░░░░     ░░░░░  ░░░░░  ░░░░░░  ░░░░░░  ░░░░ ░░░░░ ░░░░░  ░███░░░     #
          #                                                                                       ░███        #
          #                                                                                       █████       #
          #                                                                                      ░░░░░        #
          #                                                                                                   #
          #####################################################################################################"""
    logo2 = f"""
          #   {colored_start_game}                                                                                #
          #   {colored_info}                                                                                      #
          #   {colored_quit}                                                                                      #
          #                                                                                                   #
          #####################################################################################################
    """
    print(logo1, end="")
    print(logo2)


def gameInfo():
    info0 = """
    ###################################################################################################################
    +------------------------------------------------------------------------------------------------------------------+"""
    info1 = """
    |  Hello and welcome to the the terminal version of the classic boardgame battleship!                              |"""
    info2 = """
    |                                                                                                                  |
    |  In this version you will be battling against an automated opponent - a true multiplayer mode may be introduced  |
    |  in a future release!                                                                                            |
    |                                                                                                                  |
    |  In this current version, your boats and the enemy boats will be placed automatically.                           |
    |                                                                                                                  |
    """
    info3 = """|  """
    info3_5 = """Game Objective:"""
    info4 = """The Rules are simple, destroy the five enemy ships before they can destroy yours. Each turn     |
    |  you are allowed to fire one "shell" onto the enemies playing field by entering a coordinate. The enemy will     |
    |  also fire onto your playing field each turn.                                                                    |
    |                                                                                                                  |
    |  When prompted the coordinate must be entered in the following format:"""
    attkFormat = """A1, B2, C3, etc..."""
    info5 = """
    |  Each ship has a different length and is represented by a letter on the board.                                   |
    |  *Carrier: 5 spaces - C                                                                                          |
    |  *Battleship: 4 spaces - B                                                                                       |
    |  *Destroyer: 3 spaces - D                                                                                        |
    |  *Submarine: 3 spaces - S                                                                                        |
    |  *Patrol Boat: 2 spaces - P                                                                                      |
    |                                                                                                                  |
    |  *Missses are represented by an 'X'                                                                              |
    |  *Hits are represented by an '#'                                                                                 |
    |  *Sunk ships are represented by a '!'                                                                            |
    |  *Spaces not yet fired upon are represented by a '0'                                                             |
    |                                                                                                                  |"""
    info6 = """
    |  You will be notified when you have hit, missed, or sunk an enemy ship. Likewise, the enemy will know when they  |
    |  have hit, missed, or sunk one of your ships.                                                                    |
    |                                                                                                                  |
    |  Ships can be placed horizontally or vertically, but not diagonally. Ships can be placed touching each other,    |
    |  but not overlapping.                                                                                            |"""
    info7 = """
    |                                                                                                                  |
    |  A sample board is shown below of what the enemy's boat positioning may look like:                               |
    |  """
    info7_5 = """*Keep in mind you will not be able to see the enemies board, only your own mission data."""
    board1 = """
    |__________________________________________________________________________________________________________________|
    |                        ||  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  ||                          |
    | ________________________________________________________________________________________________________________ |"""
    board1_a = """
    |                      A ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  P  |  P   ||                          |
    |                      B ||  C  |  C  |  C  |  C  |  C  |  0  |  0  |  0  |  0  |  0   ||                          |
    |                      C ||  D  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0   ||                          |
    |                      D ||  D  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0   ||                          |
    |                      F ||  D  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0   ||                          |
    |                      G ||  S  |  S  |  S  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                          |
    |                      H ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                          |
    |                      I ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                          |
    |                      J ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                          |
    |__________________________________________________________________________________________________________________|"""
    board2_a = """
    |                                                                                                                  |
    | The board below represents your view of the enemies board. You will be able to see hits, misses, and sunk ships. |
    |__________________________________________________________________________________________________________________|"""
    board2_b = """
    |                         ||  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10                             |"""
    board2_c = """
    | ________________________________________________________________________________________________________________ |"""
    board2_d = """
    |                       A ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  #  | 0  ||                           |
    |                       B ||  !  |  !  |  !  |  !  |  !  |  0  |  0  |  0  |  0  | 0  ||                           |
    |                       C ||  #  |  0  |  0  |  0  |  X  |  X  |  X  |  0  |  0  | 0  ||                           |
    |                       D ||  #  |  X  |  0  |  0  |  0  |  X  |  0  |  0  |  0  | 0  ||                           |
    |                       F ||  0  |  0  |  X  |  X  |  X  |  X  |  0  |  0  |  0  | 0  ||                           |
    |                       G ||  0  |  0  |  X  |  X  |  X  |  X  |  0  |  0  |  0  | 0  ||                           |
    |                       H ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  | 0  ||                           |
    |                       I ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  | 0  ||                           |
    |                       J ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  | 0  ||                           |"""
    board2_e = """
    |__________________________________________________________________________________________________________________|"""
    info8 = """
    | Good luck and have fun!                                                                                          |
    | If you wish to start the game, please enter 's'. Any other character will return you to the main menu.           |
    +------------------------------------------------------------------------------------------------------------------+"""
    print(info0, end="")
    info1_colored = infoColor(info1)
    info2_colored = infoColor(info2)
    info4_colored = infoColor(info4)
    info6_colored = infoColor(info6)
    info7 = infoColor(info7)
    info8 = infoColor(info8)

    info3_colored = ""
    for char in info3:
        if char not in [" ", "|"]:
            info3_colored += colored(char, "cyan", attrs=["underline"])
        else:
            info3_colored += char

    info5_colored = ""
    for char in info5:
        if char not in [" ", "|"]:
            if char == "*":
                info5_colored += colored(char, "red", attrs=["bold"])
            elif char == "0":
                info5_colored += colored(char, "blue")
            elif char == "X":
                info5_colored += colored(char, "white")
            elif char == "#":
                info5_colored += colored(char, "yellow")
            elif char == "!":
                info5_colored += colored(char, "red")
            else:
                info5_colored += colored(char, "cyan")
        else:
            info5_colored += char

    info7_5_colored = ""
    for char in info7_5:
        if char not in [" ", "|"]:
            if char == "*":
                info7_5_colored += colored(char, "red", attrs=["bold"])
            else:
                info7_5_colored += colored(char, "cyan")
        else:
            info7_5_colored += char
    board2_a_colored = ""
    for char in board2_a:
        if char not in [" ", "|", "_"]:
            board2_a_colored += colored(char, "cyan")
        else:
            board2_a_colored += char

    print(info1_colored, end="")
    print(info2_colored, end="")
    print(info3, end="")
    cprint(info3_5, "cyan", attrs=["underline"], end=" ")
    print(info4_colored, end=" ")
    cprint(attkFormat, "cyan", attrs=["underline"], end="")
    print("                        |\n", end="")
    print(
        "    |                                                                                                                  |",
        end="",
    )
    print(info5_colored, end="")
    print(info6_colored, end="")
    print(info7, end="")
    print(info7_5_colored, end="")
    print("                        |", end="")
    printSample(header=board1, board_string=board1_a)
    print(board2_a_colored, end="")
    printBoard(header=board2_b, border=board2_c, board=board2_d, footer=board2_e)
    print(info8)
    response = input()
    if response == "s":
        pass
    else:
        gameLoop()


def gameLoop():
    while True:
        response = input()
        if response == "s":
            pass  ##TODO GameStart
        elif response == "i":
            gameInfo()
        elif response == "q":
            while True:
                print("Are you sure you wish to exit?")
                input_color_yes = colored("(y)es", "green")
                input_color_no = colored("(n)o", "red")
                confirm = input(f"{input_color_yes} or {input_color_no}?\n")
                if confirm == "y":
                    print("Exiting game...")
                    exit()
                else:
                    print("Please enter 's', 'i', or 'q'")
                    gameLoop()
        else:
            cprint(
                "Invalid selection Pleaes enter 's' 'i' or 'q'",
                "red",
                "on_green",
                attrs=["bold"],
            )


#! Main
gameStart()
gameLoop()

"""
# we have 100 slots available
# 	Carrier 	5 = C
# 	Battleship 	4 = B
# 	Destroyer 	3 = D
# 	Submarine 	3 = S
# 	Patrol Boat 2 = P
# 17 slots are taking up by boats
#3 83 slots are empty

# limitations for placement?
when placing the carrier, we need 4 more spaces of contigual blocks in linear direction
when placing the battleship, we need 3 more spaces of contigual blocks in linear direction
when placing the destroyer, we need 2 more spaces of contigual blocks in linear direction
when placing the submarine, we need 2 more spaces of contigual blocks in linear direction
when placing the patrol boat, we need 1 more space of contigual blocks in linear direction

boat class - COMPLETE

player class -


"""
