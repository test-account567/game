import time
import random
from gamer import Gamer


"""
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
"""

user = Gamer("User", 100)  # initializing a player 1
comp = Gamer("Computer", 100)  # initializing a player 2

"""[user.soft_kick, user.strong_kick, user.health_up]"""
user_actions = [1, 2, 3]  # list of user methods

"""[comp.soft_kick, comp.strong_kick, comp.health_up, comp.health_chance]"""
comp_actions = [1, 2, 3, 4]  # list comp methods

user_rand_actions = random.choice(user_actions)  # to get random method
comp_rand_actions = random.choice(comp_actions)  # to get random method


def user_actions(funcs):  # function , to eval some method
    if funcs == 1:
        return 1
    elif funcs == 2:
        return 2
    elif funcs == 3:
        return 3


def comp_actions(funcs):  # function , to eval some method
    if funcs == 1:
        return 1
    elif funcs == 2:
        return 2
    elif funcs == 3:
        return 3
    elif funcs == 4:
        return 4


def game_user(action):
    if action == 1:
        res = user.health - comp.soft_kick()
        setattr(user, "health", res)
        return print(f"Computer kick you , Your health is {user.health}, Computer health is {comp.health}")
    elif action == 2:
        res = user.health - comp.strong_kick()
        setattr(user, "health", res)
        return print(f"Computer kick you , Your health is {user.health}, Computer health is {comp.health}")
    elif action == 3:
        if user.health + user.health_up() >= 100:
            res = 100
            setattr(user, "health", res)
            return print(f"Your health go up {user.health} , Your health is {user.health}, Computer health is {comp.health}")
        else:
            res = user.health + user.health_up()
            setattr(user, "health", res)
            print(f"Your health go up {user.health} , Your health is {user.health}, Computer health is {comp.health}")


def game_comp(action):
    if action == 1:
        res = comp.health - user.soft_kick()
        setattr(comp, "health", res)
        return print(f"You kick a computer , Your health is {user.health}, Computer health is {comp.health}")
    elif action == 2:
        res = comp.health - user.strong_kick()
        setattr(comp, "health", res)
        return print(f"You kick a computer , Your health is {user.health}, Computer health is {comp.health}")
    elif action == 3:
        if comp.health + comp.health_up() >= 100:
            res = 100
            setattr(comp, "health", res)
            return print(f"Computer health up{user.health}, Your health is {user.health}, Computer health is {comp.health}")
        else:
            res = comp.health + user.health_up()
            setattr(user, "health", res)
            print(f"Your health go up {user.health} , Your health is {user.health}, Computer health is {comp.health}")
    elif action == 4:
        if comp.health <= 35:
            res = comp.health + comp.health_chance()
            setattr(comp, "health", res)
            return print(f"Computer health up{user.health}, Your health is {user.health}, Computer health is {comp.health}")


rand_players = [1, 2]  # [game_user, game_comp]  # list of players
run_func = random.choice(rand_players)  # (rand_players)  # to get random player


def run(func):  # function to get random gamer
    if func == 1:
        return game_user(user_actions(user_rand_actions))
    elif func == 2:
        return game_comp(comp_actions(comp_rand_actions))


def main():  # main function
    print("Welcome to the game !")
    time.sleep(2)
    print(f"Gamer 1: {user.name}, health: {user.health}, Gamer 2: {comp.name}, health: {comp.health}")
    time.sleep(2)
    while user.health == 100 or comp.health == 100:
        run(run_func)
        time.sleep(2)
        if user.health <= 0 or comp.health <= 0:
            break
        elif user.health < 100:
            continue
        elif comp.health < 100:
            continue


if __name__ == '__main__':
    main()
