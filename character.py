class Character:
    def __init__(self, name, health, power):
        self.name = name
        self._current_health = health
        self.total_health = health
        self.power = power
        # gain experience every battle, level up? 
        self.level = 1
        self.experience = 0

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
        else:
            self._current_health -= value

    def attack(self, character):
        character.sub_current_health(self.calculate_damage())

    def calculate_damage(self):
        return self.power

    def reset(self):
        self.set_current_health(self.total_health)


class NPC(Character):
    # ai logic 
    def act(self, character):
        self.attack(character)


class Player(Character):
    def process_turn(self, selection: BattleMenu, opponent: Character):
        if selection == BattleMenu.ATTACK:
            self.attack(opponent)
            print(f"You attack {opponent.name} for {self.player.power} damage!")
        elif selection == BattleMenu.USE_POTION:
            # equipment, potion classes? 
            self.add_current_health(15)
