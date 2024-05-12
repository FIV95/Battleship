class Boat:
    all_boats = []

    def __init__(self, name, size, health, hp, player):
        self.name = name
        self.size = size
        self.health = health
        self.hp= hp
        self.player = player
        self.position = ""
        Boat.all_boats.append(self)

    def __repr__(self):
        string = "Name: {name}, Health: {health}".format(
            name=self.name,
            health=self.hp,
        )
        return string

    def is_dead(self):
        return self.health == ""

    def take_damage(self):
        new_health = self.health[:-1]
        self.health = new_health
        return self.name

