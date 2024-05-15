import random
from boat import Boat
from player import Player, player1, player2
import HelperFunctions


def gameStart():
    boat_spawn()
    for player in Player.all_players:
        for boat in player.boats:
            directions = ["left", "right", "up", "down"]
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            possible_results_left = []
            possible_results_right = []
            possible_results_up = []
            possible_results_down = []
            random_location = player.defense_view[x][y]
            while random_location != 0:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    random_location = player.defense_view[x][y]
            boatPlacementCheck(player, x, y, boat.size, directions, possible_results_left, possible_results_right, possible_results_up, possible_results_down)
            all_results = [possible_results_left] + [possible_results_right] + [possible_results_down] + [possible_results_up]
            all_results = [array for array in all_results if len(array) == boat.size]
            length_of_final_results = len(all_results)
            random_index = random.randint(0, length_of_final_results -1)
            choice = all_results[random_index]
            hp_count = len(boat.health)
            boat_char = boat.health[0]
            while hp_count > 0:
                for i in choice:
                    player.defense_view[i[0]][i[1]] = boat_char
                    hp_count = hp_count - 1
            possible_results_down = []
            possible_results_up = []
            possible_results_left = []
            possible_results_right = []



    HelperFunctions.view_render(player.defense_view)

def boat_spawn():
    player1_carrier = Boat(name="Carrier", size=5, health="CCCCC", hp=5, player=player1)
    player1_battleship = Boat(name="Battleship", size=4, health="BBBB", hp=4, player=player1)
    player1_destroyer = Boat(name="Destroyer", size=3, health="DDD", hp=3, player=player1)
    player1_submarine = Boat(name="Submarine", size=3, health="SSS", hp=3, player=player1)
    player1_patrol_boat = Boat(name="Patrol Boat", size=2, health="PP", hp=2, player=player1)

    player2_carrier = Boat(name="Carrier", size=5, health="CCCCC", hp=5, player=player2)
    player2_battleship = Boat(name="Battleship", size=4, health="BBBB", hp=4, player=player2)
    player2_destroyer = Boat(name="Destroyer", size=3, health="DDD", hp=3, player=player2)
    player2_submarine = Boat(name="Submarine", size=3, health="SSS", hp=3, player=player2)
    player2_patrol_boat = Boat(name="Patrol Boat", size=2, health="PP", hp=2, player=player2)


    for boat in Boat.all_boats:
        if boat.player == player1:
            player1.boats.append(boat)
        if boat.player == player2:
            player2.boats.append(boat)
    Boat.boat_dict = {
    ("Player 1", "C"): player1.boats[0],
    ("Player 1", "B"): player1.boats[1],
    ("Player 1", "D"): player1.boats[2],
    ("Player 1", "S"): player1.boats[3],
    ("Player 1", "P"): player1.boats[4],
    ("Player 2", "C"): player2.boats[0],
    ("Player 2", "B"): player2.boats[1],
    ("Player 2", "D"): player2.boats[2],
    ("Player 2", "S"): player2.boats[3],
    ("Player 2", "P"): player2.boats[4],
    }
    return Boat.boat_dict


def mid_game_info():
    print("\nIf at anytime you wish to view your defense board, type 'd'")
    print("If at anytime you wish to view your offense board, type 'o'")


def boatPlacementCheck(player, x, y, size, directions_to_check, left_results, right_results,up_results, down_results):
    original_x = x
    original_y = y
    original_size = size

    while directions_to_check != []:

        while "left" in directions_to_check and size != 0:
            if player.defense_view[x][y] == 0:
                size = size - 1
                left_results.append([x,y])
                if size == 0:
                    directions_to_check.remove("left")
                    size = original_size
                    x = original_x
                    y = original_y
                    break
                if HelperFunctions.is_index_in_range(player.defense_view, x, y-1):
                    y = y - 1
                else:
                    directions_to_check.remove("left")
                    x = original_x
                    y = original_y
                    size = original_size
            else:
                directions_to_check.remove("left")
                left_results = []
                x = original_x
                y = original_y
                size = original_size

        while "right" in directions_to_check and size != 0:
            if player.defense_view[x][y] == 0:
                size = size - 1
                right_results.append([x,y])
                if size == 0:
                    directions_to_check.remove("right")
                    size = original_size
                    x = original_x
                    y = original_y
                    break
                if HelperFunctions.is_index_in_range(player.defense_view, x, y+1):
                    y = y + 1
                else:
                    directions_to_check.remove("right")
                    x = original_x
                    y = original_y
                    size = original_size
            else:
                directions_to_check.remove("right")
                right_results = []
                x = original_x
                y = original_y
                size = original_size

        while "up" in directions_to_check and size != 0:
            if player.defense_view[x][y] == 0:
                size = size - 1
                up_results.append([x,y])
                if size == 0:
                    directions_to_check.remove("up")
                    size = original_size
                    original_x = x
                    original_y = y
                    break
                if HelperFunctions.is_index_in_range(player.defense_view, x - 1, y):
                   x = x - 1
                else:
                    directions_to_check.remove("up")
                    x = original_x
                    y = original_y
                    size = original_size
            else:
                directions_to_check.remove("up")
                up_results = []
                x = original_x
                y = original_y
                size = original_size

        while "down" in directions_to_check and size != 0:
            if player.defense_view[x][y] == 0:
                size = size - 1
                down_results.append([x,y])
                if size == 0:
                    directions_to_check.remove("down")
                    size = original_size
                    original_x = x
                    original_y = y
                    break
                if HelperFunctions.is_index_in_range(player.defense_view, x+1, y):
                   x = x + 1
                else:
                    directions_to_check.remove("down")
                    x = original_x
                    y = original_y
                    size = original_size
            else:
                directions_to_check.remove("down")
                down_results = []
                x = original_x
                y = original_y
                size = original_size

    return

def primary_game_loop():
    turn = 0
    print("\t\t\nAt any point type exit to close the game")
    while any(boat.hp > 0 for boat in player1.boats) and all(boat.hp > 0 for boat in player2.boats):
        print("\t\t\n\nTURN # {turn} -------------------------------------------------".format(turn = turn))
        mid_game_info()
        player1.player_turn_complete(player2,Boat.boat_dict)
        player2.computer_turn_complete(player1, Boat.boat_dict)
        print()

    if all(boat.hp <= 0 for boat in player1.boats):
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")
    turn = turn + 1
