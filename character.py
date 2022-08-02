from battle import BattleMenu


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self._current_health = health
        self.total_health = health
        self.power = power
        # gain experience every battle, level up? 
        self.level = 1
        self.experience = 0

        self._isdead = False

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    def get_current_health(self):
        return self._current_health

    def set_current_health(self, value: int):
        self._current_health = value

    def add_current_health(self, value: int):
        if self._current_health + value > self.total_health:
            self.set_current_health(self.total_health)
        else:
            self._current_health += value

    def sub_current_health(self, value: int):
        if self._current_health - value < 0:
            self._current_health = 0
            self._isdead = True
        else:
            self._current_health -= value

    def attack(self, character):
        character.sub_current_health(self.calculate_damage())

    def calculate_damage(self):
        return self.power

    def reset(self):
        self.set_current_health(self.total_health)
        self._isdead = False

    def isdead(self):
        return self._isdead


class NPC(Character):
    # ai logic 
    def act(self, character):
        self.attack(character)


class Player(Character):
    def process_turn(self, selection: BattleMenu, opponent: Character):
        if selection is BattleMenu.ATTACK:
            self.attack(opponent)
            print(f"You attack {opponent.name} for {self.power} damage!")
        elif selection is BattleMenu.USE_POTION:
            # equipment, potion classes?
            potion_strength = 15
            print(f"You've used a potion and gained {potion_strength} health points.")
            self.add_current_health(potion_strength)
