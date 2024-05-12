from termcolor import colored, cprint
import GameFunctions
import HelperFunctions
import StartUpFunctions


def gameLoop():
    while True:
        response = input()
        if response == "s":
            print("Starting game...")
            GameFunctions.gameStart()
            GameFunctions.primary_game_loop()
        elif response == "i":
            StartUpFunctions.gameInfo()
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
StartUpFunctions.gameStart()
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
