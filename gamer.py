from random import choice


class Gamer:

    def __init__(self, name, health):
        self.name = name
        self.health = health


    def soft_kick(self):
        result = choice(range(18, 26))
        return result


    def strong_kick(self):
        result = choice(range(10, 36))
        return result


    def health_up(self):
        result = choice(range(18, 26))
        return result


    def health_chance(self):
        result = choice(range(18, 26))*2
        return result

