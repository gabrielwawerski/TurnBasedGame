from enum import Enum


class MenuEnum(Enum):
    START = 1
    EXIT = 2

    def __str__(self):
        return str.title(str(self.name)).replace("_", " ")


class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health


class Battle:
    def __init__(self, opponent1, opponent2):
        self.opponent1 = opponent1
        self.opponnet2 = opponent2


class App:
    def __init__(self):
        self._run = True

    def run(self):
        while self._run:
            pass


if __name__ == '__main__':
    App().run()







