class Player:
    def __init__ (self, name):
        self.boats = []
        self.name = name
        self.defense_view = [[0 for _ in range(10)] for _ in range(10)]
        self.offense_view = [[0 for _ in range(10)] for _ in range(10)]
        self.misses = []
        self.hits = []
        self.sinks = []


        ## offense view contains hit/miss/sink data so player1 offense_view has to match player2 defense_view

    def __repr__(self):
        string = "{name}".format(name = self.name)
        return string


player1 = Player("Player 1")
player2 = Player("Player 2")
