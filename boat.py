from player import player1, player2
import random

class Boat:
    all_boats = []

    def __init__(self,name,size, health, player):
        self.name = name
        self.size = size
        self.health = health
        self.player = player
        self.position = ""
        Boat.all_boats.append(self)

    def __repr__(self):
        string = "Name: {name}, Size: {size}, Health: {health}, Player: {player}, Position: {position}".format(name = self.name, size = self.size, health = self.health, player = self.player, position = self.position)
        return string

    def is_dead(self):
        return self.health == ""

    def take_damage(self):
        new_health = self.health[:-1]
        self.health = new_health
        return self.name

    def gameStart():
        player1_carrier = Boat("Carrier", 5, "CCCCC", player1)
        player1_battleship = Boat("Battleship", 4,  "BBBB", player1)
        player1_destroyer = Boat("Destroyer", 3, "DDD", player1)
        player1_submarine = Boat("Submarine", 3, "SSS", player1)
        player1_patrol_boat = Boat("Patrol Boat", 2, "PP", player1)

        player2_carrier = Boat("Carrier", 5, "CCCCC", player2)
        player2_battleship = Boat("Battleship", 4,  "BBBB", player2)
        player2_destroyer = Boat("Destroyer", 3, "DDD", player2)
        player2_submarine = Boat("Submarine", 3, "SSS", player2)
        player2_patrol_boat = Boat("Patrol Boat", 2, "PP", player2)


        for boat in Boat.all_boats:
            if boat.player == player1:
                player1.boats.append(boat)
            if boat.player == player2:
                player2.boats.append(boat)

        ## boat placement in defensive view
        ## we know our stopping condition its when the five boats of the player have been added to the board.
        ## the boats array is sorted from biggest boat to smallest boats[0] - boats[4]
        ## we can ues the random module to place each boat. the random function can return our starting point a single index in the 2d array
        ## with that given starting point we have to check if going
        """
        [left,right,up,down]
        [x][-self.size]/
        [x][+self.size]/
        [-self.size][x]
        [+self.size][x] recursion?"""

print(player1.boats)
