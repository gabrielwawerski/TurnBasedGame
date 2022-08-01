from enum import Enum
from random import randint

from character import Character, NPC
from util import div, subdiv, print_menu


class BattleMenu(Enum):
    ATTACK = 1
    USE_POTION = 2


class Turn(Enum):
    PLAYER = 0
    NPC = 1


class Battle:
    def __init__(self, player: Character, opponent: NPC):
        self.player = player
        self.opponent = opponent
        self.current_turn = Turn.PLAYER if randint(0, 1) == 0 else Turn.NPC

    def start(self):
        div()
        print("Battle started!")

        while True:
            if self.player.get_current_health() == 0:
                print("You died.")
                print("Battle finished!")
                self.reset()
                div()
                break
            elif self.opponent.get_current_health() == 0:
                print(f"You have defeated {self.opponent.name}!")
                print("Battle finished!")
                self.reset()
                div()
                break
            self.print_allchar_info()

            if self.current_turn == Turn.PLAYER:
                turn_active = True
                while turn_active:
                    subdiv()
                    print("Your turn!")
                    print_menu(BattleMenu)
                    selection = int(input("> "))

                    if selection == BattleMenu.ATTACK.value:
                        self.player.attack(self.opponent)
                        print(f"You attack {self.opponent.name} for {self.player.power} damage!")
                        self.switch_turn()
                        turn_active = False
                        subdiv()

            elif self.current_turn == Turn.NPC:
                subdiv()
                print(f"{self.opponent.name}'s turn!")
                self.opponent.act(self.player)
                print(f"{self.opponent.name} attacks {self.player.name} for {self.opponent.power} damage!")
                self.switch_turn()
                subdiv()

    def switch_turn(self):
        self.current_turn = Turn.PLAYER if self.current_turn == Turn.NPC else Turn.NPC

    def print_char_info(self, character: Character):
        print(f"{character.name} | Health: {character.get_current_health()}")

    def print_allchar_info(self):
        self.print_char_info(self.player)
        self.print_char_info(self.opponent)

    def reset(self):
        self.player.reset()
        self.opponent.reset()
