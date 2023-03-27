
import pygame
import random
from lab11.turn_combat import CombatPlayer

""" Create PyGameAIPlayer class here"""


class PyGameAIPlayer():
    def __init__(self, name):
        self.name = name
        self.opponent_choices = []

    def selectAction(self, percept):
        return ord(str(random.randint(0,9)))

        #No way of obtainning opponent's move, dont use for now.
        """
        # ** Previous round update **
        if percept is not None:
            self.opponent_choices.append(percept)

        # ** Current round update **
        self._action = self.weapon_selecting_strategy()
        """





""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        
        self.weapon = random.randint(0,2)
        return self.weapon

        #No way of obtainning opponent's move, dont use for now.
        """
        opponent_type = "unknown"

        # Questioning ----------------------------------------
        # Is opponent a mimic agent?
        isMimic = True
        if len(self.opponent_choices) >= 4:
            first_choice = self.opponent_choices[0]
            for current_choice in self.opponent_choices:
                if first_choice != current_choice: #Opponent is not a mimic agent
                    isMimic = False
                    break
                else:
                    isMimic = True
                if isMimic:
                    opponent_type = "mimic"

        # Is opponent a single agent?
        isSingle = True
        if len(self.opponent_choices) >= 11:
            first_choice = self.opponent_choices[0]
            for current_choice in self.opponent_choices:
                if first_choice != current_choice: #Opponent is not a single agent
                    isSingle = False
                    break
                else:
                    isSingle = True
                if isSingle:
                    opponent_type = "single"

        # Since we confirmed the opponent is not mimic nor single, it has to be switch.
        if isSingle == False and isMimic == False:
            opponent_type = "switch"

        # Action ----------------------------------------
        # Dealing with mimic or unknown opponent
        if opponent_type == "mimic" or opponent_type == "unknown":
            return random.randint(0, 2)

        # Dealing with single opponent
        if opponent_type == "single":
            if self.opponent_choices[0] == 0:
                return 1
            elif self.opponent_choices[0] == 1:
                return 2
            else:
                return 0
        # Dealing with switch opponent
        if opponent_type == "switch":
            if self.opponent_choices[len(self.opponent_choices)-1] == 0:
                return 1
            elif self.opponent_choices[len(self.opponent_choices)-1] == 1:
                return 2
            elif self.opponent_choices[len(self.opponent_choices)-1] == 2:
                return 0
        """
