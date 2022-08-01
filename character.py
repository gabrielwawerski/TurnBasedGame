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
    # ai logic here
    def act(self, character):
        self.attack(character)


class Player(Character):
    def process_turn(self, opponent: Character):
        pass
