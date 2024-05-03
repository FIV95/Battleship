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
    print("""
    ###################################################################################################################
    +------------------------------------------------------------------------------------------------------------------+
    |  Hello and welcome to the the terminal version of the classic boardgame battleship!                              |
    |                                                                                                                  |
    |  In this version you will be battling against an automated opponent - a true multiplayer mode may be introduced  |
    |  in a future release!                                                                                            |
    |                                                                                                                  |
    |  In this current version, your boats your boats and the enemy boats will be placed automatically.                |
    |                                                                                                                  |
    |  Game Objective: The Rules are simple, destroy the five enemy ships before they can destroy yours. Each turn     |
    |  you are allowed to fire one "shell" onto the enemies playing field by entering a coordinate. The enemy will     |
    |  also fire onto your playing field each turn.                                                                    |
    |                                                                                                                  |
    |  When prompted the coordinate must be entered in the following format: A1, B2, C3, etc.                          |
    |                                                                                                                  |
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
    |                                                                                                                  |
    |  You will be notified when you have hit, missed, or sunk an enemy ship. Likewise, the enemy will know when they  |
    |  have hit, missed, or sunk one of your ships.                                                                    |
    |                                                                                                                  |
    |  Ships can be placed horizontally or vertically, but not diagonally. Ships can be placed touching each other,    |
    |  but not overlapping.                                                                                            |
    |                                                                                                                  |
    |  A sample board is shown below of what the enemy's boat positioning may look like:                               |
    |  Keep in mind you will not be able to see the enemies board, only your own.                                      |
    |------------------------------------------------------------------------------------------------------------------|
    |                            ||  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10                          |
    | ________________________________________________________________________________________________________________ |
    |                          A ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  P  |  P   ||                      |
    |                          B ||  C  |  C  |  C  |  C  |  C  |  0  |  0  |  0  |  0  |  0   ||                      |
    |                          C ||  D  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0   ||                      |
    |                          D ||  D  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0   ||                      |
    |                          F ||  D  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0   ||                      |
    |                          G ||  S  |  S  |  S  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                      |
    |                          H ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                      |
    |                          I ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                      |
    |                          J ||  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  B  |  0   ||                      |
    |------------------------------------------------------------------------------------------------------------------|
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
    """)
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
