from player import Player, player1, player2
import random


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
    results,
):
    array = player.defense_view
    length_to_parse = size
    original_size = original_size
    original_x = original_x
    original_y = original_y
    y = y
    x = x

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
                    results=[],
                )
            if player.defense_view[x][y] == 0:
                length_to_parse -= 1
                results.append([x, y])
                if length_to_parse - 1 == 0:
                    if is_index_in_range(player.defense_view, x, y - 1):
                        if player.defense_view[x][y - 1] == 0:
                            results.append([x, y - 1])
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
                                results=results,
                            )
                        directions_checked.remove("left")
                recursiveCheck(
                    size=length_to_parse,
                    original_size=original_size,
                    x=x,
                    y=y - 1,
                    original_x=original_x,
                    original_y=original_y,
                    player=player,
                    directions_checked=directions_checked,
                    results=results,
                )
            else:
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
                    results=[],
                )
            if player.defense_view[x][y] == 0:
                length_to_parse -= 1
                results.append([x, y])
                if length_to_parse - 1 == 0:
                    if is_index_in_range(player.defense_view, x, y + 1):
                        if player.defense_view[x][y + 1] == 0:
                            results.append([x, y + 1])
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
                                results=results,
                            )
                    directions_checked.remove("right")
                recursiveCheck(
                    size=length_to_parse,
                    original_size=original_size,
                    x=x,
                    y=y + 1,
                    original_x=original_x,
                    original_y=original_y,
                    player=player,
                    directions_checked=directions_checked,
                    results=results,
                )
            else:
                directions_checked.remove("right")
        ##########!############
        if "up" in directions_checked:
            if x < 0 or x > 9 or y < 0 or y > 9:
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
                    results=[],
                )
            if player.defense_view[x][y] == 0:
                length_to_parse -= 1
                results.append([x, y])
                if length_to_parse - 1 == 0:
                    if is_index_in_range(player.defense_view, x - 1, y):
                        if player.defense_view[x - 1][y] == 0:
                            results.append([x - 1, y])
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
                                results=results,
                            )
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
                    results=results,
                )
            else:
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
                    results=results,
                )
            if player.defense_view[x][y] == 0:
                length_to_parse -= 1
                results.append([x, y])
                if length_to_parse - 1 == 0:
                    if is_index_in_range(player.defense_view, x + 1, y):
                        if player.defense_view[x + 1][y] == 0:
                            results.append([x + 1, y])
                            recursiveCheck(
                                size=original_size,
                                original_size=original_size,
                                x=x + 1,
                                y=y,
                                original_x=original_x,
                                original_y=y,
                                player=player,
                                directions_checked=directions_checked,
                                results=results,
                            )
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
                        results=results,
                    )
            else:
                directions_checked.remove("down")
    else:
        return results


def gameStart():
    boat_spawn()
    for boat in player1.boats:
        directions = ["left", "right", "up", "down"]
        placing = True
        while placing:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            possible_results = []
            random_location = player1.defense_view[x][y]
            results = recursiveCheck(
                boat.size, boat.size, x, y, x, y, player1, directions, possible_results
            )
            if possible_results == []:
                placing = False


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
