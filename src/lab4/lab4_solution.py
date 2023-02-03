'''
Lab 4: Rock-Paper-Scissor AI Agent

In this lab you will build one AI agent for the game of Rock-Paper-Scissors, that can defeat a few different kinds of 
computer players.

You will update the AI agent class to create your first AI agent for this course.
Use the precept sequence to find out which opponent agent you are facing, 
so that it can beat these three opponent agents:

    Agent Single:  this agent picks a weapon at random at the start, 
                   and always plays that weapon.  
                   For example: 2,2,2,2,2,2,2,.....

    Agent Switch:  this agent picks a weapon at random at the start,
                   and randomly picks a weapon once every 10 rounds.  
                   For example:  2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,...

    Agent Mimic:  this agent picks a weapon at random in the first round, 
                  and then always does what you did the previous round.  
                  For example:  if you played 1,2,0,1,2,0,1,2,0,...  
                   then this agent would play 0,1,2,0,1,2,0,1,2,...

Discussions in lab:  You don't know ahead of time which opponent you will be facing, 
so the first few rounds will be used to figure this out.   How?

Once you've figured out the opponent, apply rules against that opponent. 
A model-based reflex agent uses rules (determined by its human creator) to decide which action to take.

If your AI is totally random, you should be expected to win about 33% of the time, so here is the requirement:  
In 100 rounds, you should consistently win at least 85 rounds to be considered a winner.

You get a 1 point for beating the single agent, 2 points for beating the switch agent, 
and 2 points for beating the mimic agent.

'''

from rock_paper_scissor import Player
from rock_paper_scissor import run_game
from rock_paper_scissor import random_weapon_select
import random

class AiPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.initial_weapon = random_weapon_select()
    
    def weapon_selecting_strategy(self):
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

        



if __name__ == '__main__':
    final_tally = [0]*3
    for agent in range(3):
        for i in range(100):
            tally = [score for _, score in run_game(AiPlayer("AI"), 100, agent)]
            if sum(tally) == 0:
                final_tally[agent] = 0
            else:
                final_tally[agent] += tally[0]/sum(tally)

    print("Final tally: ", final_tally)  