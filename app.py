from battle import Battle
from character import *
from enums import *
from util import div, print_menu, title


class App:
    """
    v0.11
        - Modularize
        - Minor improvements

    v0.1
        - Basic functionality
    """
    def __init__(self):
        self._run = True
        self.version = "0.11"
        self.selection = None

    def run(self):
        title(f'DragonFight v{self.version}')
        print_menu(MainMenu)
        self.init()

        while self._run:
            self.inpt()

            if self.selection == MainMenu.START.value:
                self.start()
            elif self.selection == MainMenu.EXIT.value:
                print("exiting")
                exit()
            else:
                print("Not a valid selection.")

    def start(self):
        div()
        print_menu(Menu)
        self.inpt()

        if self.selection == Menu.FIGHT.value:
            Battle(self.player, self.npc).start()
        elif self.selection == Menu.UPGRADE.value:
            pass
        elif self.selection == Menu.STORE.value:
            pass
        elif self.selection == Menu.EXIT.value:
            exit()
        else:
            print("Not a valid selection.")
            self.start()

    def init(self):
        self.player = Player("Alexstrasza", 100, 11)
        self.npc = NPC("Sindragosa", 100, 9)

    def inpt(self):
        self.selection = int(input("> "))
