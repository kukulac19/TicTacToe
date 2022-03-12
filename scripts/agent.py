#https://towardsdatascience.com/creating-a-tic-tac-toe-game-with-a-q-learning-ai-which-masters-the-game-9b0567d24de
import random
import dill 
import os
from time import sleep
from scripts.learning_algorithm import QLearningAlgorithm
from scripts.game import TicTacToe

class Bot:
    def __init__(self):
        self.eps = 1.0
        self.q_table = QLearningAlgorithm()
        if os.path.isfile('./q_table.bfile'):
            with open("q_table.bfile", "rb") as q_table:
                self.q_table = dill.load(q_table)
            sleep(1)
        else:
            self._learn()
    #PRIVATE METHODS
    def _learn_one_game(self):
        game = TicTacToe(bot_is_learning=True)
        while True:
            state = str(game.game_board)
            action = self.get_action(state, game.get_valid_actions())
            game.play_one_round_without_window(action)
            if game.winner or game.game_over:
                self.q_table.update(state, action, str(game.game_board), 100)
                break
            game.play_one_round_without_window(random.choice(game.get_valid_actions()))
            if game.winner or game.game_over:
                self.q_table.update(state, action, str(game.game_board), -100)
                break
            self.q_table.update(state, action, str(game.game_board), 0)
    def _learn(self, n=20000):
        for _ in range(n):
            self._learn_one_game()
            self.eps -= 0.0001
        with open("q_table.bfile", "wb") as q_table:
            dill.dump(self.q_table, q_table)
    #PUBLIC METHODS
    #USED BY Window.play_one_round()        
    def get_action(self, state, valid_actions):
        if random.random() < self.eps:
            return random.choice(list(valid_actions))
        best_action = self.q_table.get_best_action(state)
        if best_action is None:
            return random.choice(list(valid_actions))
        return best_action


