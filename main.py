from enum import Enum
from random import randint


class EMenu(Enum):
    def __str__(self):
        return str.title(str(self.name)).replace("_", " ")


class MainMenu(EMenu):
    START = 1
    EXIT = 2


class Menu(EMenu):
    FIGHT = 1
    UPGRADE = 2


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self._current_health = health
        self.total_health = health
        self.power = power

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    def get_current_health(self):
        return self._current_health

    def set_current_health(self, value):
        self._current_health = value

    def sub_current_health(self, value):
        if self._current_health - value < 0:
            print("setting to 0!")
            self._current_health = 0
        else:
            self._current_health -= value

    def attack(self, character):
        self.sub_current_health(character.power)

    def reset(self):
        self.set_current_health(self.total_health)


class Battle:
    def __init__(self, player: Character, opponent: Character):
        self.player = player
        self.opponent = opponent
        self.first_move = randint(0, 1)

    def start(self):
        while self.player.set_current_health != 0 or self.opponent.set_current_health != 0:
            pass
        self.reset()

    def reset(self):
        self.player.reset()
        self.opponent.reset()


class App:
    def __init__(self):
        self._run = True
        self.version = "0.1"
        self.selection = None

    def run(self):
        while self._run:
            print(f'DragonFight v{self.version}')
            self.init()

            if self.main_menu():
                self.start()
            else:
                print("exiting")
                exit()

    def main_menu(self):
        self.inpt()

        if self.selection is MainMenu.START.value:
            return True
        elif self.selection is MainMenu.EXIT.value:
            return False
        else:
            print("Not a valid selection.")
            self.main_menu()

    def start(self):
        self.inpt()

        if self.selection is Menu.FIGHT.value:
            pass

        else:
            print("Not a valid selection.")
            self.start()

    def inpt(self):
        self.selection = int(input("> "))

    def init(self):
        sindragosa = Character("Sindragosa", 100, 9)
        alexstrasza = Character("Alexstrasza", 100, 11)


if __name__ == '__main__':
    App().run()
