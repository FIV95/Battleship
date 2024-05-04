from termcolor import colored, cprint
board = [
# . 1 2 3 4 5 6 7 8 9 10
    [0,0,0,0,0,0,0,0,0,0], #A
    [0,0,0,0,0,0,0,0,0,0], #B
    [0,0,0,0,0,0,0,0,0,0], #C
    [0,0,0,0,0,0,0,0,0,0], #D
    [0,0,0,0,0,0,0,0,0,0], #E
    [0,0,0,0,0,0,0,0,0,0], #F
    [0,0,0,0,0,0,0,0,0,0], #G
    [0,0,0,0,0,0,0,0,0,0], #H
    [0,0,0,0,0,0,0,0,0,0], #I
    [0,0,0,0,0,0,0,0,0,0], #J
    ]

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

def printDemo(board_string):
    colored_board = ""
    board_array = board_string.split('\n')  # Split the string into lines
    for board in board_array:
        if "||" in board:  # Check if || is in the line
            row_label, board_content = board.split("||", 1)  # Split the line into row label and board content at the first occurrence of ||
            colored_board += row_label + "||"  # Add the row label and || to colored_board without any coloring
            for char in board_content:
                if char in ['P', 'C', 'D', 'S', 'B', '0']:
                    if char == 'P':
                        colored_board += colored(char, 'red', on_color='on_light_red')
                    elif char == 'C':
                        colored_board += colored(char, 'red', "on_light_red")
                    elif char == 'D':
                        colored_board += colored(char, 'red', on_color="on_light_red")
                    elif char == 'S':
                        colored_board += colored(char, 'red', on_color="on_light_red")
                    elif char == 'B':
                        colored_board += colored(char, 'red', on_color="on_light_red")
                    elif char == '0':
                        colored_board += colored(char, 'blue')
                else:
                    colored_board += char
        else:  # This is a row label or border
            colored_board += board
        colored_board += "\n"

    for line in colored_board.splitlines():
        print(line)


def gameStart():
    start_game = "(s) = Start Game"
    info = "(i) = Info"
    quit = "(q) = quit"
    colored_start_game = colored(start_game, 'green')
    colored_info = colored(info, 'blue')
    colored_quit = colored(quit, 'red')
    logo1 = ("""
        ############################################################################################################
        #                                                                                                          #
        #    ███████████             █████     █████    ████               █████████  █████       ███              #
        #   ░░███░░░░░███           ░░███     ░░███    ░░███              ███░░░░░███░░███       ░░░               #
        #    ░███    ░███  ██████   ███████   ███████   ░███   ██████    ░███    ░░░  ░███████   ████  ████████    #
        #    ░██████████  ░░░░░███ ░░░███░   ░░░███░    ░███  ███░░███   ░░█████████  ░███░░███ ░░███ ░░███░░███   #
        #    ░███░░░░░███  ███████   ░███      ░███     ░███ ░███████     ░░░░░░░░███ ░███ ░███  ░███  ░███ ░███   #
        #    ░███    ░███ ███░░███   ░███ ███  ░███ ███ ░███ ░███░░░      ███    ░███ ░███ ░███  ░███  ░███ ░███   #
        #    ███████████ ░░████████  ░░█████   ░░█████  █████░░██████    ░░█████████  ████ █████ █████ ░███████    #
        #   ░░░░░░░░░░░   ░░░░░░░░    ░░░░░     ░░░░░  ░░░░░  ░░░░░░      ░░░░░░░░░  ░░░░ ░░░░░ ░░░░░  ░███░░░     #
        #                                                                                              ░███        #
        #                                                                                              █████       #
        #                                                                                             ░░░░░        #
        # -------------------------------------------------------------------------------------------------------- #""")
    logo2 = f"""
        #   {colored_start_game}                                                                                       #
        #   {colored_info}                                                                                             #
        #   {colored_quit}                                                                                             #
        #                                                                                                          #
        ############################################################################################################
    """
    print(logo1, end="")
    print(logo2)

def gameInfo():
    info0 = """
    ###################################################################################################################
    +------------------------------------------------------------------------------------------------------------------+"""
    info1= """
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
    | *A sample board is shown below of what the enemy's boat positioning may look like:                               |
    |  """
    info7_5 = """Keep in mind you will not be able to see the enemies board, only your own mission data."""
    board1 = """
    |__________________________________________________________________________________________________________________|
    |                        ||  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10                              |
    | ________________________________________________________________________________________________________________ |
    |                      A ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  P  |  P   ||                          |
    |                      B ||  C  |  C  |  C  |  C  |  C  |  0  |  0  |  0  |  0  |  0   ||                          |
    |                      C ||  D  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0   ||                          |
    |                      D ||  D  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0   ||                          |
    |                      F ||  D  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0   ||                          |
    |                      G ||  S  |  S  |  S  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                          |
    |                      H ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                          |
    |                      I ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                          |
    |                      J ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                          |
    |__________________________________________________________________________________________________________________|
    |                                                                                                                  |"""
    board2= """
    | The board below represents your view of the enemies board. You will be able to see hits, misses, and sunk ships. |
    |__________________________________________________________________________________________________________________|
    |                             ||  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10                         |
    | ________________________________________________________________________________________________________________ |
    |                           A ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  #  | 0  ||                       |
    |                           B ||  !  |  !  |  !  |  !  |  !  |  0  |  0  |  0  |  0  | 0  ||                       |
    |                           C ||  #  |  0  |  0  |  0  |  X  |  X  |  X  |  0  |  0  | 0  ||                       |
    |                           D ||  #  |  X  |  0  |  0  |  0  |  X  |  0  |  0  |  0  | 0  ||                       |
    |                           F ||  0  |  0  |  X  |  X  |  X  |  X  |  0  |  0  |  0  | 0  ||                       |
    |                           G ||  0  |  0  |  X  |  X  |  X  |  X  |  0  |  0  |  0  | 0  ||                       |
    |                           H ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  | 0  ||                       |
    |                           I ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  | 0  ||                       |
    |                           J ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  | 0  ||                       |
    |__________________________________________________________________________________________________________________|
    | Good luck and have fun!                                                                                          |
    | If you wish to start the game, please enter 's'. Any other character will return you to the main menu.           |
    +------------------------------------------------------------------------------------------------------------------+
    """
    print(info0, end="")
    info1_colored = ""

    for char in info1:
        if char not in [' ', '|']:
            info1_colored += colored(char, 'cyan')
        else:
            info1_colored += char
    info2_colored = ""
    for char in info2:
        if char not in [' ', '|']:
            info2_colored += colored(char, 'cyan')
        else:
            info2_colored += char
    info3_colored = ""
    for char in info3:
        if char not in [' ', '|']:
            info3_colored += colored(char, 'cyan', attrs=["underline"])
        else:
            info3_colored += char
    info4_colored = ""
    for char in info4:
        if char not in [' ', '|']:
            info4_colored += colored(char, 'cyan')
        else:
            info4_colored += char
    format_colored = ""
    for char in attkFormat:
        if char not in [' ', '|']:
            format_colored += colored(char, 'cyan', attrs=["underline"])
        else:
            attkFormat += char
    info5_colored = ""
    for char in info5:
        if char not in [' ', '|']:
            if char == '*':
                info5_colored += colored(char, 'red', attrs=["bold"])
            elif char == '0':
                info5_colored += colored(char, 'blue')
            elif char == 'X':
                info5_colored += colored(char, 'white')
            elif char == '#':
                info5_colored += colored(char, 'yellow')
            elif char == '!':
                info5_colored += colored(char, 'red')
            else : info5_colored += colored(char, 'cyan')
        else:
            info5_colored += char

    info6_colored = ""
    for char in info6:
        if char not in [' ', '|']:
            info6_colored += colored(char, 'cyan')
        else:
            info6_colored += char
    info7_colored = ""
    for char in info7:
        if char not in [' ', '|']:
            if char == '*':
                info7_colored += colored(char, 'red', attrs=["bold"])
            else:
                info7_colored += colored(char, 'cyan')
        else:
            info7_colored += char


    print(info1_colored, end="")
    print(info2_colored, end="")
    print(info3, end="")
    cprint(info3_5, "cyan", attrs=["underline"], end=" ")
    print(info4_colored, end=" ")
    print(format_colored, end="")
    print("                           |\n", end="")
    print("    |                                                                                                                  |", end="")
    print(info5_colored, end="")
    print(info6_colored, end="")
    print(info7_colored, end="")
    cprint(info7_5, "cyan", attrs=["underline"], end=" ")
    print("                        |", end="")
    printDemo(board1)

    response = input()
    if response == 's':
        pass
    else:
        gameLoop()

def gameLoop():
    while True:
        response = input()
        if response == 's':
            pass ##TODO GameStart
        elif response == 'i':
            gameInfo()
        elif response == 'q':
            while True:
                print("Are you sure you wish to exit?")
                input_color_yes = colored("(y)es", 'green')
                input_color_no = colored("(n)o", 'red')
                confirm = input(f"{input_color_yes} or {input_color_no}?\n")
                if confirm == 'y':
                    print("Exiting game...")
                    exit()
                else:
                    print("Please enter 's', 'i', or 'q'")
                    gameLoop()
        else:
            cprint("Invalid selection Pleaes enter 's' 'i' or 'q'", "red", "on_green", attrs=["bold"])
#! Main
gameStart()
gameLoop()
