import time
from enum import Enum
from random import randint


class EMenu(Enum):
    def __str__(self):
        return str.title(str(self.name)).replace("_", " ")


class MainMenu(EMenu):
    START = 1
    EXIT = 9


class Menu(EMenu):
    FIGHT = 1
    UPGRADE = 2
    EXIT = 9


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
        character.sub_current_health(self.power)

    def reset(self):
        self.set_current_health(self.total_health)


class NPC(Character):
    pass


class Player(Character):
    pass


class Battle:
    def __init__(self, player: Character, opponent: Character):
        self.player = player
        self.opponent = opponent
        self.current_turn = randint(0, 1)

    def start(self):
        print("Battle started!")

        while True:
            if self.player.get_current_health() == 0:
                break
            elif self.opponent.get_current_health() == 0:
                break
            self.print_allchar_info()

            # player's turn
            if self.current_turn == 0:
                # time.sleep(1)
                turn_active = True
                while turn_active:
                    print("1. Attack")
                    selection = int(input("> "))
                    if selection == 1:
                        self.player.attack(self.opponent)
                        print(f"You attack {self.opponent.name} for {self.player.power} dmg!")
                        self.current_turn = 1
                        turn_active = False
            # npc turn
            elif self.current_turn == 1:
                # time.sleep(1)
                print(f"{self.opponent.name}'s turn!")
                self.opponent.attack(self.player)
                print(f"{self.opponent.name} attacks {self.player.name} for {self.opponent.power} dmg!")
                self.current_turn = 0
        print("Battle finished!")
        self.reset()

    def print_char_info(self, character: Character):
        print(f"{character.name} | Health: {character.get_current_health()}")

    def print_allchar_info(self):
        self.print_char_info(self.player)
        self.print_char_info(self.opponent)

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
            print(f"{MainMenu.START.value}. Start")
            print(f"{MainMenu.EXIT.value}. Exit")
            self.init()
            self.inpt()

            if self.selection == MainMenu.START.value:
                self.start()
            elif self.selection == MainMenu.EXIT.value:
                print("exiting")
                exit()
            else:
                print("Not a valid selection.")

    def start(self):
        print(f"{Menu.FIGHT.value}. Fight")
        print(f"{Menu.EXIT.value}. Exit")
        self.inpt()

        if self.selection == Menu.FIGHT.value:
            print("in here")
            Battle(self.player, self.npc).start()

        elif self.selection == Menu.EXIT.value:
            exit()

        else:
            print("Not a valid selection.")
            self.start()

    def main_menu(self):
        self.inpt()

        if self.selection == MainMenu.START.value:
            return True
        elif self.selection == MainMenu.EXIT.value:
            return False
        else:
            print("Not a valid selection.")
            self.main_menu()

    def inpt(self):
        self.selection = int(input("> "))

    def init(self):
        self.player = Character("Alexstrasza", 100, 11)
        self.npc = Character("Sindragosa", 100, 9)


if __name__ == '__main__':
    App().run()
