from termcolor import colored, cprint
import GameFunctions
import HelperFunctions
import StartUpFunctions
from gameLoop import gameLoop




#! Main
StartUpFunctions.gameLaunch()
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
