from player import Player, player1, player2
from termcolor import colored
import random


def boatPlacementCheck(player, x, y, size, directions_to_check, left_results, right_results,up_results, down_results):
    original_x = x
    original_y = y
    original_size = size

    while directions_to_check != []:

        while "left" in directions_to_check or size == 0:
            if player1.defense_view[x][y] == 0:
                size = size - 1
                left_results.append([x,y])
                if is_index_in_range(player1.defense_view, x, y-1):
                    y = y - 1
                else:
                    directions_to_check.remove("left")
            else:
                directions_to_check.remove("left")
                x = original_x
                y = original_y
                size = original_size

        while "right" in directions_to_check or size == 0:
            if player1.defense_view[x][y] == 0:
                size = size - 1
                right_results.append([x,y])
                if is_index_in_range(player1.defense_view, x, y+1):
                    y = y + 1
                else:
                    directions_to_check.remove("right")
            else:
                directions_to_check.remove("right")
                x = original_x
                y = original_y
                size = original_size

        while "up" in directions_to_check or size == 0:
            if player1.defense_view[x][y] == 0:
                size = size - 1
                up_results.append([x,y])
                if is_index_in_range(player1.defense_view, x - 1, y):
                   x = x - 1
                else:
                    directions_to_check.remove("up")
            else:
                directions_to_check.remove("up")
                x = original_x
                y = original_y
                size = original_size

        while "down" in directions_to_check or size == 0:
            if player1.defense_view[x][y] == 0:
                size = size - 1
                down_results.append([x,y])
                if is_index_in_range(player1.defense_view, x+1, y):
                   x = x + 1
                else:
                    directions_to_check.remove("down")
            else:
                directions_to_check.remove("down")
                x = original_x
                y = original_y
                size = original_size



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
                if char in ["X", "#", "!", "0", "D", "F", "G", "H", "I", "J", "C", "B", "P", "S"]:
                    # Add color to char and append it to colored_board
                    if char == "D" or char == "C" or char == "B" or char == "P" or char == "S":
                        colored_board += colored(char, "red")
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

def defense_view_render(array):
    string1 = """
    |                         ||  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10                              |"""
    string2= """
    | ________________________________________________________________________________________________________________  |
    |                                                                                                                   |"""

    string3= """
    |                       A ||  {a1}  |  {a2}  |  {a3}  |  {a4}  |  {a5}  |  {a6}  |  {a7}  |  {a8}  |  {a9}  |  {a10}  ||                           |
    |                       B ||  {b1}  |  {b2}  |  {b3}  |  {b4}  |  {b5}  |  {b6}  |  {b7}  |  {b8}  |  {b9}  |  {b10}  ||                           |
    |                       C ||  {c1}  |  {c2}  |  {c3}  |  {c4}  |  {c5}  |  {c6}  |  {c7}  |  {c8}  |  {c9}  |  {c10}  ||                           |
    |                       D ||  {d1}  |  {d2}  |  {d3}  |  {d4}  |  {d5}  |  {d6}  |  {d7}  |  {d8}  |  {d9}  |  {d10}  ||                           |
    |                       E ||  {e1}  |  {e2}  |  {e3}  |  {e4}  |  {e5}  |  {e6}  |  {e7}  |  {e8}  |  {e9}  |  {e10}  ||                           |
    |                       F ||  {f1}  |  {f2}  |  {f3}  |  {f4}  |  {f5}  |  {f6}  |  {f7}  |  {f8}  |  {f9}  |  {f10}  ||                           |
    |                       G ||  {g1}  |  {g2}  |  {g3}  |  {g4}  |  {g5}  |  {g6}  |  {g7}  |  {g8}  |  {g9}  |  {g10}  ||                           |
    |                       H ||  {h1}  |  {h2}  |  {h3}  |  {h4}  |  {h5}  |  {h6}  |  {h7}  |  {h8}  |  {h9}  |  {h10}  ||                           |
    |                       I ||  {i1}  |  {i2}  |  {i3}  |  {i4}  |  {i5}  |  {i6}  |  {i7}  |  {i8}  |  {i9}  |  {i10}  ||                           |
    |                       J ||  {j1}  |  {j2}  |  {j3}  |  {j4}  |  {j5}  |  {j6}  |  {j7}  |  {j8}  |  {j9}  |  {j10}  ||                           |""".format(
        a1 = array[0][0],
        a2 = array[0][1],
        a3 = array[0][2],
        a4 = array[0][3],
        a5 = array[0][4],
        a6 = array[0][5],
        a7 = array[0][6],
        a8 = array[0][7],
        a9 = array[0][8],
        a10 = array[0][9],
        b1 = array[1][0],
        b2 = array[1][1],
        b3 = array[1][2],
        b4 = array[1][3],
        b5 = array[1][4],
        b6 = array[1][5],
        b7 = array[1][6],
        b8 = array[1][7],
        b9 = array[1][8],
        b10 = array[1][9],
        c1 = array[2][0],
        c2 = array[2][1],
        c3 = array[2][2],
        c4 = array[2][3],
        c5 = array[2][4],
        c6 = array[2][5],
        c7 = array[2][6],
        c8 = array[2][7],
        c9 = array[2][8],
        c10 = array[2][9],
        d1 = array[3][0],
        d2 = array[3][1],
        d3 = array[3][2],
        d4 = array[3][3],
        d5 = array[3][4],
        d6 = array[3][5],
        d7 = array[3][6],
        d8 = array[3][7],
        d9 = array[3][8],
        d10 = array[3][9],
        e1 = array[4][0],
        e2 = array[4][1],
        e3 = array[4][2],
        e4 = array[4][3],
        e5 = array[4][4],
        e6 = array[4][5],
        e7 = array[4][6],
        e8 = array[4][7],
        e9 = array[4][8],
        e10 = array[4][9],
        f1 = array[5][0],
        f2 = array[5][1],
        f3 = array[5][2],
        f4 = array[5][3],
        f5 = array[5][4],
        f6 = array[5][5],
        f7 = array[5][6],
        f8 = array[5][7],
        f9 = array[5][8],
        f10 = array[5][9],
        g1 = array[6][0],
        g2 = array[6][1],
        g3 = array[6][2],
        g4 = array[6][3],
        g5 = array[6][4],
        g6 = array[6][5],
        g7 = array[6][6],
        g8 = array[6][7],
        g9 = array[6][8],
        g10 = array[6][9],
        h1 = array[7][0],
        h2 = array[7][1],
        h3 = array[7][2],
        h4 = array[7][3],
        h5 = array[7][4],
        h6 = array[7][5],
        h7 = array[7][6],
        h8 = array[7][7],
        h9 = array[7][8],
        h10 = array[7][9],
        i1 = array[8][0],
        i2 = array[8][1],
        i3 = array[8][2],
        i4 = array[8][3],
        i5 = array[8][4],
        i6 = array[8][5],
        i7 = array[8][6],
        i8 = array[8][7],
        i9 = array[8][8],
        i10 = array[8][9],
        j1 = array[9][0],
        j2 = array[9][1],
        j3 = array[9][2],
        j4 = array[9][3],
        j5 = array[9][4],
        j6 = array[9][5],
        j7 = array[9][6],
        j8 = array[9][7],
        j9 = array[9][8],
        j10 = array[9][9],
    )
    string4 = """
    |___________________________________________________________________________________________________________________|"""
    printBoard(string1, string2, string3, string4)

def boat_spawn():
    player1_carrier = Boat("Carrier", 5, "CCCCC", player1)
    player1_battleship = Boat("Battleship", 4, "BBBB", player1)
    player1_destroyer = Boat("Destroyer", 3, "DDD", player1)
    player1_submarine = Boat("Submarine", 3, "SSS", player1)
    player1_patrol_boat = Boat("Patrol Boat", 2, "PP", player1)

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


def is_index_in_range(array, row_index, col_index):
    return 0 <= row_index < len(array) and 0 <= col_index < len(array[0])


def recursiveCheck(
    size,
    original_size,
    x,
    y,
    original_x,
    original_y,
    player,
    directions_checked,
    left_results,
    right_results,
    up_results,
    down_results
):
    length_to_parse = size

    ##########!############
    if directions_checked != []:
        if "left" in directions_checked:
            if x < 0 or x > 9 or y < 0 or y > 9:
                directions_checked.remove("left")
                recursiveCheck(
                    size=original_size,
                    original_size=original_size,
                    x=original_x,
                    original_x=original_x,
                    y=original_y,
                    original_y=original_y,
                    player=player,
                    directions_checked=directions_checked,
                    left_results=left_results,
                    right_results = right_results,
                    up_results=up_results,
                    down_results=down_results
                )
            if is_index_in_range(player.defense_view, x - 1, y):
                if player.defense_view[x][y] == 0:
                    length_to_parse -= 1
                    left_results.append([x, y])
                    if length_to_parse - 1 == 0:
                        if is_index_in_range(player.defense_view, x, y - 1):
                            if player.defense_view[x][y - 1] == 0:
                                left_results.append([x, y - 1])
                                directions_checked.remove("left")
                                recursiveCheck(
                                    size=original_size,
                                    original_size=original_size,
                                    x=original_x,
                                    original_x=original_x,
                                    original_y=original_y,
                                    y=original_y,
                                    player=player,
                                    directions_checked=directions_checked,
                                    left_results=left_results,
                                    right_results = right_results,
                                    up_results=up_results,
                                    down_results=down_results
                                )

                recursiveCheck(
                        size=length_to_parse,
                        original_size=original_size,
                        x=x,
                        y=y - 1,
                        original_x=original_x,
                        original_y=original_y,
                        player=player,
                        directions_checked=directions_checked,
                        left_results=left_results,
                        right_results = right_results,
                        up_results=up_results,
                        down_results=down_results
                    )
            else:
                if "left" in directions_checked:
                    directions_checked.remove("left")
        ##########!#############
        if "right" in directions_checked:
            if x < 0 or x > 9 or y < 0 or y > 9:
                directions_checked.remove("right")
                recursiveCheck(
                    size=original_size,
                    original_size=original_size,
                    x=original_x,
                    original_x=original_x,
                    y=original_y,
                    original_y=original_y,
                    player=player,
                    directions_checked=directions_checked,
                    left_results=left_results,
                    right_results = right_results,
                    up_results=up_results,
                    down_results=down_results
                )
            if is_index_in_range(player.defense_view, x, y):
                if player.defense_view[x][y] == 0:
                    length_to_parse -= 1
                    right_results.append([x, y])
                    if length_to_parse - 1 == 0:
                        if is_index_in_range(player.defense_view, x, y + 1):
                            if player.defense_view[x][y + 1] == 0:
                                right_results.append([x, y + 1])
                                directions_checked.remove("right")
                                recursiveCheck(
                                    size=original_size,
                                    original_size=original_size,
                                    x=original_x,
                                    original_x=original_x,
                                    original_y=original_y,
                                    y=original_y,
                                    player=player,
                                    directions_checked=directions_checked,
                                    left_results=left_results,
                                    right_results=right_results,
                                    up_results=up_results,
                                    down_results=down_results
                                )
                recursiveCheck(
                    size=length_to_parse,
                    original_size=original_size,
                    x=x,
                    y=y + 1,
                    original_x=original_x,
                    original_y=original_y,
                    player=player,
                    directions_checked=directions_checked,
                    left_results=left_results,
                    right_results=right_results,
                    up_results=up_results,
                    down_results=down_results
                )
            else:
                 if "right" in directions_checked:
                    directions_checked.remove("right")
        ##########!############
        if "up" in directions_checked:
            if x < 0 or x > 9 or y < 0 or y > 9 or player.defense_view[x][y] != 0:
                directions_checked.remove("up")
                recursiveCheck(
                    size=original_size,
                    original_size=original_size,
                    x=original_x,
                    y=original_y,
                    original_x=original_x,
                    original_y=original_y,
                    player=player,
                    directions_checked=directions_checked,
                    left_results=left_results,
                    right_results=right_results,
                    up_results=up_results,
                    down_results=down_results
                )
            if is_index_in_range(player.defense_view, x, y):
                if player.defense_view[x][y] == 0:
                    length_to_parse -= 1
                    up_results.append([x, y])
                    if length_to_parse - 1 == 0:
                        if is_index_in_range(player.defense_view, x - 1, y):
                            if player.defense_view[x - 1][y] == 0:
                                up_results.append([x - 1, y])
                                directions_checked.remove("up")
                                recursiveCheck(
                                    size=original_size,
                                    original_size=original_size,
                                    x=original_x,
                                    y=original_y,
                                    original_x=original_x,
                                    original_y=original_y,
                                    player=player,
                                    directions_checked=directions_checked,
                                    left_results=left_results,
                                    right_results=right_results,
                                    up_results=up_results,
                                    down_results=down_results
                                )
                            if "up" in directions_checked:
                                directions_checked.remove("up")

                recursiveCheck(
                    size=length_to_parse,
                    original_size=original_size,
                    x=x - 1,
                    y=y,
                    original_x=original_x,
                    original_y=original_y,
                    player=player,
                    directions_checked=directions_checked,
                    left_results=left_results,
                    right_results=right_results,
                    up_results=up_results,
                    down_results=down_results
                )
            else:
                 if "up" in directions_checked:
                    directions_checked.remove("up")
        ##########!############
        if "down" in directions_checked:
            if x < 0 or x > 9 or y < 0 or y > 9:
                directions_checked.remove("down")
                recursiveCheck(
                    size=original_size,
                    original_size=original_size,
                    x=original_x,
                    y=original_y,
                    original_x=original_x,
                    original_y=original_y,
                    player=player,
                    directions_checked=directions_checked,
                    left_results=left_results,
                    right_results=right_results,
                    up_results=up_results,
                    down_results=down_results
                )
            if is_index_in_range(player.defense_view, x, y):
                if player.defense_view[x][y] == 0:
                    length_to_parse -= 1
                    down_results.append([x, y])
                    if length_to_parse - 1 == 0:
                        if is_index_in_range(player.defense_view, x + 1, y):
                            if player.defense_view[x + 1][y] == 0:
                                down_results.append([x + 1, y])
                                directions_checked.remove("down")
                                recursiveCheck(
                                    size=original_size,
                                    original_size=original_size,
                                    x=x + 1,
                                    y=y,
                                    original_x=original_x,
                                    original_y=y,
                                    player=player,
                                    directions_checked=directions_checked,
                                left_results=left_results,
                                right_results=right_results,
                                up_results=up_results,
                                down_results=down_results
                                )
                        if "down" in directions_checked:
                            directions_checked.remove("down")
                if is_index_in_range(player.defense_view, x + 1, y):
                    recursiveCheck(
                        size=length_to_parse,
                        original_size=original_size,
                        x=x + 1,
                        y=y,
                        original_x=original_x,
                        original_y=original_y,
                        player=player,
                        directions_checked=directions_checked,
                        left_results=left_results,
                        right_results=right_results,
                        up_results=up_results,
                        down_results=down_results
                    )
            else:
                 if "down" in directions_checked:
                    directions_checked.remove("down")
    else:
        return


def gameStart():
    boat_spawn()
    for boat in player1.boats:
        directions = ["left", "right", "up", "down"]
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        possible_results_left = []
        possible_results_right = []
        possible_results_up = []
        possible_results_down = []
        random_location = player1.defense_view[x][y]
        while random_location != 0:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                random_location = player1.defense_view[x][y]
        results = recursiveCheck(
            boat.size, boat.size, x, y, x, y, player1, directions, possible_results_left, possible_results_right, possible_results_up, possible_results_down
        )
        print("BOAT SIZE = ", boat.size)
        all_results = [possible_results_left] + [possible_results_right] + [possible_results_down] + [possible_results_up]
        print("All Results = ", all_results)
        print("Length of left results = ", len(all_results[0]))
        print("Length of right results = ", len(all_results[1]))
        print("Length of up results = ", len(all_results[2]))
        print("Length of down results = ", len(all_results[3]))
        print("length of all_results BEFORE remove", len(all_results))
        for array in all_results:
            if len(array) != boat.size:
                all_results.remove(array)
        print("Second All Results = ", all_results)
        print("length of all_results AFTER remove", len(all_results))
        length_of_final_results = len(all_results)
        random_index = random.randint(0, length_of_final_results-1)
        choice = all_results[random_index]
        print("Value of choice", choice)
        hp_count = len(boat.health)
        boat_char = boat.health[0]
        for i in choice:
            print(type(i))
            player1.defense_view[i[0]][i[1]] = boat_char
            hp_count = hp_count - 1
            if hp_count == 0:
                continue
        print(player1.defense_view)
        defense_view_render(player1.defense_view)


        print(all_results)
        print("BOAT DONE")


class Boat:
    all_boats = []

    def __init__(self, name, size, health, player):
        self.name = name
        self.size = size
        self.health = health
        self.player = player
        self.position = ""
        Boat.all_boats.append(self)

    def __repr__(self):
        string = "Name: {name}, Size: {size}, Health: {health}, Player: {player}, Position: {position}".format(
            name=self.name,
            size=self.size,
            health=self.health,
            player=self.player,
            position=self.position,
        )
        return string

    def is_dead(self):
        return self.health == ""

    def take_damage(self):
        new_health = self.health[:-1]
        self.health = new_health
        return self.name

        ## boat placement in defensive view
        ## we know our stopping condition its when the five boats of the player have been added to the board.
        ## the boats array is sorted from biggest boat to smallest boats[0] - boats[4]
        ## we can ues the random module to place each boat. the random function can return our starting point a single index in the 2d array
        ## with that given starting point we have to check if going
        """
        [left,right,up,down]
        [x][-self.size] OR [x][-x]
        [x][+self.size] OR [x][+x]
        [-self.size][x] OR [-x][x]
        [+self.size][x] OR [+x][x] recursion?"""


print(player1.boats)
test = gameStart()
