class TicTacToe:
    def __init__(self, bot=None, bot_is_learning=False):
        if not bot_is_learning:
            self.bot = bot
        self.reinitializing_variables()
    #PRIVATE METHODS
    def _set_symbol_on_board(self, index): 
        def symbol_generator():
            if self.game_round % 2:
                return -1   #'O'
            else:
                return 1    #'X'
        def increment_game_round(): 
            self.game_round += 1
        x,y = index
        symbol = symbol_generator()
        self.game_board[x][y] = symbol
        self.game_board_for_displaying[(x,y)] = False
        increment_game_round()
    def _check_winner(self):
        def set_winner(index):
            x,y = index
            self.game_over = True
            self.winner = "X" if self.game_board[x][y] == 1 else "O"
        #HORIZONTALLY
        if abs(sum(self.game_board[0])) == 3:
            set_winner((0,0))     
        elif abs(sum(self.game_board[1])) == 3:
            set_winner((1,0))     
        elif abs(sum(self.game_board[2])) == 3:
            set_winner((2,0))    
        #VERTICALLY
        elif abs(self.game_board[0][0] + self.game_board[1][0] + self.game_board[2][0]) == 3:
            set_winner((0,0))     
        elif abs(self.game_board[0][1] + self.game_board[1][1] + self.game_board[2][1]) == 3:
            set_winner((0,1))        
        elif abs(self.game_board[0][2] + self.game_board[1][2] + self.game_board[2][2]) == 3:
            set_winner((0,2))     
        #DIAGONALLY
        elif abs(self.game_board[0][0] + self.game_board[1][1] + self.game_board[2][2]) == 3:
            set_winner((0,0))    
        elif abs(self.game_board[0][2] + self.game_board[1][1] + self.game_board[2][0]) == 3:
            set_winner((0,2))
        #DRAW     
        elif self.game_round == 9: 
            self.game_over = True
    #PUBLIC METHODS
    #USED BY Window.start_new_game()
    #USED BY Window.display_menu()
    def reinitializing_variables(self):
        self.winner = None
        self.game_round = 0
        self.game_over = False        
        self.game_board = [[0,0,0] for _ in range(3)] 
        self.game_board_for_displaying = dict()
    #USED BY Window.play_one_round()
    def get_valid_actions(self):
        valid_actions = list()
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):
                if self.game_board[i][j] == 0:
                    valid_actions.append((i,j))
        return valid_actions
    #USED BY Bot._learn_one_game()
    #USED BY Window.play_one_round()
    def play_one_round_without_window(self, position):
        self._set_symbol_on_board(position)
        self._check_winner()



    





