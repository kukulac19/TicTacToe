import pygame
from scripts.agent import Bot
from scripts.game import TicTacToe

class Window:
    def __init__(self): 
        pygame.init()
        #WINDOW SETTINGS
        self.window_size = 400, 475
        self.window_color = 255, 255, 255
        self.window_font_menu = pygame.font.Font('font/Baby Marker.ttf', 45)
        self.window_font_winner = pygame.font.Font('font/Baby Marker.ttf', 75)
        self.window_screen = pygame.display.set_mode(self.window_size)
        #IMAGES
        self.image_icon = pygame.image.load("images/icon.png")
        self.image_home = pygame.image.load("images/home.png")
        self.image_x = pygame.image.load("images/x.png")
        self.image_o = pygame.image.load("images/o.png")
        self.image_background = pygame.image.load("images/ttbg.png")
        self.image_red_line_horizontal = pygame.image.load("images/red_line.png")
        self.image_red_line_vertical = pygame.image.load("images/red_line90.png")
        self.image_red_line_diagonal_growing = pygame.image.load("images/red_line45l.png")
        self.image_red_line_diagonal_declining = pygame.image.load("images/red_line45p.png")
        #PYGAME SETTINGS
        pygame.display.set_icon(self.image_icon)
        pygame.display.set_caption("TIC TAC TOE by Adon")
        #BASIC SETTINGS
        self._display_loading()
        self.bot = Bot()
        self.game = TicTacToe(self.bot)
        self.menu_is_displayed = True 
        self.position_of_symbols = {(0,0):(50,62), 
                                    (0,1):(150,62), 
                                    (0,2):(255,62), 
                                    (1,0):(50,165), 
                                    (1,1):(145,165), 
                                    (1,2):(255,165), 
                                    (2,0):(40,275), 
                                    (2,1):(135,275), 
                                    (2,2):(245,275)}
    #PRIVATE METHODS
    def _display_loading(self):
        self.window_screen.fill(self.window_color)
        loading = self.window_font_menu.render('LOADING', True, (0, 0 ,0), (255, 255, 255))
        self.window_screen.blit(loading, ((400 - (loading.get_width())) / 2, (475 - loading.get_height()) / 2))
        pygame.display.flip()
    def _recognizing_event_in_game(self, position):
        x,y = position
        if ((x >= (400 - self.image_home.get_width())) and \
           (y <= self.image_home.get_height())):
            self.display_menu()
        if self.game.game_over: return 
        if ((x >= 50) & (y >= 62)) & ((x <= 130) & (y <= 142)):
            if self.game.game_board[0][0] == 0:
                self.game.play_one_round_without_window((0,0))
                return True
        elif ((x >= 150) & (y >= 62)) & ((x <= 230) & (y <= 142)):
            if self.game.game_board[0][1] == 0:
                self.game.play_one_round_without_window((0,1))    
                return True             
        elif ((x >= 255) & (y >= 62)) & ((x <= 335) & (y <= 142)):
            if self.game.game_board[0][2] == 0:
                self.game.play_one_round_without_window((0,2))  
                return True      
        elif ((x >= 50) & (y >= 165)) & ((x <= 130) & (y <= 245)):
            if self.game.game_board[1][0] == 0:
                self.game.play_one_round_without_window((1,0)) 
                return True              
        elif ((x >= 150) & (y >= 165)) & ((x <= 230) & (y <= 245)):
            if self.game.game_board[1][1] == 0:
                self.game.play_one_round_without_window((1,1)) 
                return True                     
        elif ((x >= 255) & (y >= 165)) & ((x <= 335) & (y <= 245)):
            if self.game.game_board[1][2] == 0:
                self.game.play_one_round_without_window((1,2)) 
                return True                  
        elif ((x >= 50) & (y >= 275)) & ((x <= 130) & (y <= 355)):
            if self.game.game_board[2][0] == 0:
                self.game.play_one_round_without_window((2,0))    
                return True              
        elif ((x >= 150) & (y >= 275)) & ((x <= 230) & (y <= 355)):
            if self.game.game_board[2][1] == 0:
                self.game.play_one_round_without_window((2,1))  
                return True                   
        elif ((x >= 255) & (y >= 275)) & ((x <= 335) & (y <= 355)):
            if self.game.game_board[2][2] == 0:
                self.game.play_one_round_without_window((2,2)) 
                return True
    def _draw_symbol_on_game_board(self):
        def image_generator():
            if self.game.game_round % 2:
                return self.image_x                  
            else:
                return self.image_o
        def display_on_screen(coordinates):
            image = image_generator()
            self.window_screen.blit(image, coordinates)
            pygame.display.flip() 
        for key in self.game.game_board_for_displaying:
            if not self.game.game_board_for_displaying[key]:
                display_on_screen(self.position_of_symbols[key])
                self.game.game_board_for_displaying[key] = True   
    def _draw_winner(self):
        def display_on_screen(image, coordinates):
            self.window_screen.blit(image, coordinates)
            pygame.display.flip()
        def print_winner():
            if self.game.winner:        
                symbol = self.window_font_winner.render(f'{self.game.winner}', True, (255, 0 ,0), (255, 255, 255))
                is_winner = self.window_font_winner.render(' IS WINNER', True, (0, 0 ,0), (255, 255, 255))
                self.window_screen.blit(symbol, ((400 - (symbol.get_width() + is_winner.get_width())) / 2, 475 - symbol.get_height()))
                self.window_screen.blit(is_winner, (((400 + symbol.get_width()) - is_winner.get_width()) / 2, 475 - symbol.get_height()))
                pygame.display.flip()
            else: 
                draw = self.window_font_winner.render('DRAW', True, (255, 0 ,0), (255, 255, 255))
                self.window_screen.blit(draw, ((400 - draw.get_width() ) / 2, 475 - draw.get_height()))
                pygame.display.flip() 
        if not self.game.game_over: return
        #HORIZONTALLY
        if abs(sum(self.game.game_board[0])) == 3:
            display_on_screen(self.image_red_line_horizontal, (25,90))      
        elif abs(sum(self.game.game_board[1])) == 3:
            display_on_screen(self.image_red_line_horizontal, (25,190)) 
        elif abs(sum(self.game.game_board[2])) == 3:
            display_on_screen(self.image_red_line_horizontal, (25,300)) 
        #VERTICALLY
        elif abs(self.game.game_board[0][0] + self.game.game_board[1][0] + self.game.game_board[2][0]) == 3:
            display_on_screen(self.image_red_line_vertical, (70,50))      
        elif abs(self.game.game_board[0][1] + self.game.game_board[1][1] + self.game.game_board[2][1]) == 3:
            display_on_screen(self.image_red_line_vertical, (170,50))          
        elif abs(self.game.game_board[0][2] + self.game.game_board[1][2] + self.game.game_board[2][2]) == 3:
            display_on_screen(self.image_red_line_vertical, (275,50))     
        #DIAGONALLY
        elif abs(self.game.game_board[0][0] + self.game.game_board[1][1] + self.game.game_board[2][2]) == 3:
            display_on_screen(self.image_red_line_diagonal_growing, (50,55))    
        elif abs(self.game.game_board[0][2] + self.game.game_board[1][1] + self.game.game_board[2][0]) == 3:
           display_on_screen(self.image_red_line_diagonal_declining, (40,65))  
        print_winner()  
    #PUBLIC METHODS
    #USED BY MAIN APP
    def display_menu(self):
        self.game.reinitializing_variables()
        self.menu_is_displayed = True
        single_player = self.window_font_menu.render("Player vs Bot", True, (0, 0, 0))
        multiplayer = self.window_font_menu.render("Player vs Player", True, (255, 255, 255))
        pygame.draw.rect(self.window_screen, (255, 255, 255), (0, 0, 400, 237.5))
        pygame.draw.rect(self.window_screen, (0, 0, 0), (0, 237.5, 400, 475))
        self.window_screen.blit(single_player, ((400 - (single_player.get_width())) / 2, (237.5 - single_player.get_height()) / 2))
        self.window_screen.blit(multiplayer, ((400 - multiplayer.get_width()) / 2, (((237.5 -  multiplayer.get_height()) / 2) + 237.5)))
        pygame.display.flip()
    #USED BY MAIN APP
    def menu_choice(self, position):
        x,y = position
        self.menu_is_displayed = False
        if ((x <= 400) and (y <= 237.5)):
            self.bot_game = True
        else:
            self.bot_game = False
        self.start_new_game()
    #USED BY MAIN APP
    def play_one_round(self, position):
        if not self.bot_game:
            self._recognizing_event_in_game(position)
            self._draw_symbol_on_game_board()
            self._draw_winner()
            return
        else: 
            flag = self._recognizing_event_in_game(position)
            self._draw_symbol_on_game_board()
            self._draw_winner()
            if not flag: return
            if self.game.game_over: return
            action = self.bot.get_action(str(self.game.game_board), self.game.get_valid_actions())
            self.game.play_one_round_without_window(action)
            self._draw_symbol_on_game_board()
            self._draw_winner() 
    #USED BY MAIN APP    
    def start_new_game(self):
        self.game.reinitializing_variables()
        self.menu_is_displayed = False
        self.window_screen.fill(self.window_color)
        self.window_screen.blit(self.image_background, (0, 25))
        self.window_screen.blit(self.image_home, ((400 - self.image_home.get_width()), 0))
        pygame.display.flip()
                   