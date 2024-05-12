import random
from boat import Boat
from player import Player
import HelperFunctions


def gameStart():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
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
            print("Value of choice", choice)
            hp_count = len(boat.health)
            boat_char = boat.health[0]
            while hp_count > 0:
                for i in choice:
                    print(type(i))
                    player.defense_view[i[0]][i[1]] = boat_char
                    hp_count = hp_count - 1
            HelperFunctions.defense_view_render(player.defense_view)
            possible_results_down = []
            possible_results_up = []
            possible_results_left = []
            possible_results_right = []
    boat_dict = {
    ("player1", "C"): player1.boats[0],
    ("player1", "B"): player1.boats[1],
    ("player1", "D"): player1.boats[2],
    ("player1", "S"): player1.boats[3],
    ("player1", "P"): player1.boats[4],
    ("player2", "C"): player2.boats[0],
    ("player2", "B"): player2.boats[1],
    ("player2", "D"): player2.boats[2],
    ("player2", "S"): player2.boats[3],
    ("player2", "P"): player2.boats[4],
}


    HelperFunctions.defense_view_render(player.defense_view)

def boat_spawn():
    player1_carrier = Boat("Carrier", 5, "CCCCC", 5, player1)
    player1_battleship = Boat("Battleship", 4, "BBBB", 4, player1)
    player1_destroyer = Boat("Destroyer", 3, "DDD", 3,  player1)
    player1_submarine = Boat("Submarine", 3, "SSS", 3,  player1)
    player1_patrol_boat = Boat("Patrol Boat", 2, "PP", 2, player1)

    player2_carrier = Boat("Carrier", 5, "CCCCC", player2)
    player2_battleship = Boat("Battleship", 4, "BBBB", player2)
    player2_destroyer = Boat("Destroyer", 3, "DDD", player2)
    player2_submarine = Boat("Submarine", 3, "SSS", player2)
    player2_patrol_boat = Boat("Patrol Boat", 2, "PP", player2)

    for boat in Boat.all_boats:
        if boat.player == player1:
            player1.boats.append(boat)
        if boat.player == player2:
            player2.boats.append(boat)

def mid_game_info():
    print("If at anytime you wish to view your defense board, type 'd'")


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
    while all(boat.hp > 0 for boat in player1.boats) and all(boat.hp > 0 for boat in player2.boats):
        mid_game_info()
        player1.player_turn_complete(player2)
        player2.computer_turn_complete(player1)

    if all(boat.hp <= 0 for boat in player1.boats):
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")
