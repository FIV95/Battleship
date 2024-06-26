from termcolor import colored, cprint
import HelperFunctions
from gameLoop import gameLoop
import GameFunctions

def gameLaunch():
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

def infoColor(info):
    colored_info = ""
    for char in info:
        if char not in [" ", "|"]:
            colored_info += colored(char, "cyan")
        else:
            colored_info += char
    return colored_info

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
    |                       B ||  #  |  #  |  #  |  #  |  #  |  0  |  0  |  0  |  0  | 0  ||                           |
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
    HelperFunctions.printBoard(header=board2_b, border=board2_c, board=board2_d, footer=board2_e)
    print(info8)
    response = input()
    if response == "s":
        print("Starting game...")
        GameFunctions.gameStart()
        GameFunctions.primary_game_loop()
    else:
        gameLoop()
