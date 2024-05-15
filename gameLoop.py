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
                "Invalid selection Please enter 's' 'i' or 'q'",
                "red",
                "on_green",
                attrs=["bold"],
            )
