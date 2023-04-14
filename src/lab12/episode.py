''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygrame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab11.turn_combat import Combat
from lab11.pygame_ai_player import PyGameAICombatPlayer
from lab13.pygame_cpu_player import PyGameComputerCombatPlayer

def run_episode(player1, player2):
    episode_log = []

    currentGame = Combat()

    battle_ground = [player1, player2]

    while not currentGame.gameOver:

        states_player1 = list(reversed([(player1.health, player1.weapon) for player1 in battle_ground]))
        states_player2 = list(reversed([(player2.health, player2.weapon) for player2 in battle_ground]))

        for player1, state in zip(battle_ground, states_player1):
            player1.selectAction(state)

        for player2, state in zip(battle_ground, states_player2):
            player2.selectAction(state)

        currentGame.newRound()
        currentGame.takeTurn(player1, player2)

        print("%s's health = %d" % (player1.name, player1.health))
        print("%s's health = %d" % (player2.name, player2.health))

        observation = (player1.health, player2.health)
        action = (player1.weapon, player2.weapon)
        reward = currentGame.checkWin(player1, player2)

        episode_log.append((observation, action, reward))

    return episode_log

if __name__ == "__main__":
    player1 = PyGameAICombatPlayer("AI_Adam")
    player2 = PyGameComputerCombatPlayer("CPU_Vasu")
    
    log = run_episode(player1, player2)
    print(log)
        