from enum import Enum


class EMenu(Enum):
    def __str__(self):
        return str.title(str(self.name)).replace("_", " ")


class MainMenu(EMenu):
    START = 1
    EXIT = 2


class Menu(EMenu):
    pass


class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health


class Battle:
    def __init__(self, opponent1, opponent2):
        self.opponent1 = opponent1
        self.opponent2 = opponent2


class App:
    def __init__(self):
        self._run = True
        self.version = "0.1"

    def run(self):
        while self._run:
            print(f'DragonFight v{self.version}')

            if self.main_menu():
                self.start()
            else:
                exit()

    def main_menu(self):
        selection = int(input("> "))

        if selection is MainMenu.START.value:
            return True
        elif selection is MainMenu.EXIT.value:
            print("exiting")
            return False
        else:
            print("Not a valid selection.")
            self.main_menu()

    def start(self):
        print("here")


if __name__ == '__main__':
    App().run()
