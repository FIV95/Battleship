import random
from boat import Boat
from HelperFunctions import is_index_in_range as range_check
from HelperFunctions import board, board_dict
from HelperFunctions import coordinate_translator
from HelperFunctions import array_translator
from HelperFunctions import view_render


class Player:
    all_players = []
    def __init__ (self, name):
        self.boats = []
        self.name = name
        self.defense_view = [[0 for _ in range(10)] for _ in range(10)]
        self.defense_look_up = {f"{chr(97+i)}{j+1}": self.defense_view[i][j] for i in range(10) for j in range(10)}
        self.offense_view = [[0 for _ in range(10)] for _ in range(10)]
        self.offense_look_up = {f"{chr(97+i)}{j+1}": self.offense_view[i][j] for i in range(10) for j in range(10)}
        self.moves = []
        self.misses = []
        self.hits = []
        self.hit_look_up = { }
        self.sinks = []
        Player.all_players.append(self)


        ## offense view contains hit/miss/sink data so player1 offense_view has to match player2 defense_view

    def __repr__(self):
        string = "{name}".format(name = self.name)
        return string

    def hit_look_up_modifier(self, hit):
        ## hit will be string ex. "a1"
        self.hit_look_up[hit] = True

    def computer_turn_initiate(self):
        last_four_moves = self.moves[-4:]
        # the values of the last four moves are again stored in four seperate arrays
        ## value1 = x
        ## value2 = y
        ## we compare those values to the values stored in self.offense_view
        possible_moves = []
        if len(last_four_moves) > 0:
            for move in last_four_moves:
                x = move[0]
                y = move[1]
                if self.offense_view[x][y] in self.hits:
                    ## if the value of the last four moves is in hits, we want to add the surrounding values to the possible_moves array
                    ## but first we have to check if they are in the moves array AND are within the bounds of the board
                    if range_check(x+1, y) and [x+1, y] not in self.moves:
                        possible_moves.append([x+1, y])
                    if range_check(x-1, y) and [x-1, y] not in self.moves:
                        possible_moves.append([x-1, y])
                    if range_check(x, y+1) and [x, y+1] not in self.moves:
                        possible_moves.append([x, y+1])
                    if range_check(x, y-1) and [x, y-1] not in self.moves:
                        possible_moves.append([x, y-1])

                    random_selection = random.randint(0, len(possible_moves)-1)
                    ## we want to return the key from the self.offense_look_up dictionary thats asscociated with the random_selection
                    return possible_moves[random_selection]
        else:
            # true random
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            result = [x,y]
            return result

    def player_turn_initiate(self, player2):
        while True:
            player_input = input("\nEnter your attack coordinates: ").upper()
            if player_input == 'D':
                view_render(self.defense_view)
                self.player_turn_complete(player2,Boat.boat_dict)
            elif player_input == 'O':
                view_render(self.offense_view)
            elif player_input == 'EXIT':
                exit()
            elif player_input in board_dict:
                array = coordinate_translator(player_input)
                if array in self.moves:
                    print("You have already attacked this coordinate, please try again")
                else:
                    self.moves.append(array)
                    return array
            else:
                print("Invalid input")
                self.player_turn_complete(player2,Boat.boat_dict)

    def turn_print(self, array_to_be_translated):
        if self == player1:
            source = "Player 1"
        else:
            source = "Player 2"
        cordinate = array_translator(array_to_be_translated)
        print("{source} has attacked {cordinate}".format(source = source, cordinate = cordinate))

    def turn_process(self, target, coordinate_array, boat_dict):
        player_name = self.name
        if target.defense_view[coordinate_array[0]][coordinate_array[1]] in ['C', 'B', 'D', 'S', 'P']:
            boat_type = target.defense_view[coordinate_array[0]][coordinate_array[1]]
            boat = boat_dict[(player_name,boat_type)]
            ## input has hit carrier
            ## deduct health from target carrier
            ## print that the attack has hit a boat. -- Check if healh == 0 ? Print Sink
            ## if miss print miss
            boat.hp = boat.hp - 1
            if boat.hp == 0:
                print("{target} has lost a ship.".format(target = target))
            else:
                print("Attack successful. Marking boards respectively")
                self.offense_view[coordinate_array[0]][coordinate_array[1]] = '#'
                target.defense_view[coordinate_array[0]][coordinate_array[1]] = '#'
        else:
            print("Attack has missed!")
            self.offense_view[coordinate_array[0]][coordinate_array[1]] = 'X'

    def computer_turn_complete(self, player1, boat_dict):
        target_array = self.computer_turn_initiate()
        self.turn_print(target_array)
        self.turn_process(target = player1, coordinate_array=target_array, boat_dict= boat_dict)

    def player_turn_complete(self, player2, boat_dict):
        target_array = self.player_turn_initiate(player2)
        self.turn_print(target_array)
        print(target_array)
        self.turn_process(target = player2, coordinate_array=target_array, boat_dict= boat_dict)

    def player1_boat_status(self):
        for boat in self.boats:
            print(boat)

player1 = Player("Player 1")
player2 = Player("Player 2")

