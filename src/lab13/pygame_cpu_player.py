import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab11.turn_combat import CombatPlayer

class PyGameComputerCombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        if 30 < self.health < 50:
            self.weapon = 2
        elif self.health < 30:
            self.weapon = 1
        else:
            self.weapon = 0
        return self.weapon