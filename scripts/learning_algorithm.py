#https://towardsdatascience.com/creating-a-tic-tac-toe-game-with-a-q-learning-ai-which-masters-the-game-9b0567d24de
from collections import defaultdict

class QLearningAlgorithm:
    def __init__(self, alpha=0.5, discount=0.5):
        self.alpha = alpha
        self.discount = discount
        self.values = defaultdict(lambda: defaultdict(lambda: 0.0))
    #PUBLIC METHODS
    #USED BY Bot._learn_one_game()
    def update(self, state, action, next_state, reward):
        value = self.values[state][action]
        values = list(self.values[next_state].values())
        next_q = max(values) if values else 0
        value = value + self.alpha * (reward + self.discount * next_q - value)
        self.values[state][action] = value
    #USED BY Bot.get_action()
    def get_best_action(self, state):
        keys = list(self.values[state].keys())
        if not keys:
            return None
        return max(keys, key=lambda x: self.values[state][x])