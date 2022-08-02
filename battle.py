from enum import Enum
from random import randint

from util import div, subdiv, print_menu


class BattleMenu(Enum):
    ATTACK = 1
    USE_POTION = 2


class Turn(Enum):
    PLAYER = 0
    NPC = 1


class Battle:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.current_turn = Turn.PLAYER if randint(0, 1) == 0 else Turn.NPC

    def start(self):
        div()
        print("Battle started!")

        while True:
            if self.player.isdead():
                print("You died.")
                break
            elif self.opponent.isdead():
                print(f"You have defeated {self.opponent.name}!")
                break
            self.print_allchar_info()

            if self.current_turn == Turn.PLAYER:
                subdiv()
                print("Your turn!")
                print_menu(BattleMenu)

                battle_menu_vals = [member.value for member in BattleMenu]
                player_active = True
                while player_active:
                    selection = int(input("> "))
                    if selection in battle_menu_vals:
                        self.player.process_turn(BattleMenu(selection), self.opponent)
                        self.switch_turn()
                        player_active = False
                        subdiv()
                    else:
                        print("Not a valid selection.")
                        subdiv()

            elif self.current_turn == Turn.NPC:
                subdiv()
                print(f"{self.opponent.name}'s turn!")
                self.opponent.act(self.player)
                print(f"{self.opponent.name} attacks {self.player.name} for {self.opponent.power} damage!")
                self.switch_turn()
                subdiv()

        print("Battle finished!")
        self.reset()
        div()

    def switch_turn(self):
        self.current_turn = Turn.PLAYER if self.current_turn == Turn.NPC else Turn.NPC

    def print_char_info(self, character):
        print(f"{character.name} | Health: {character.get_current_health()}")

    def print_allchar_info(self):
        self.print_char_info(self.player)
        self.print_char_info(self.opponent)

    def reset(self):
        self.player.reset()
        self.opponent.reset()
