import sys, pygame
pygame.init()

class Game:
    def __init__(self):
        self.game = False
        self.menu = True
        self.game_round = 0
        self.game_board = {i+1: "" for i in range(9)}
        self.size = 400, 475
        self.color = 255, 255, 255
        self.background = pygame.image.load("Pictures/ttbg.png")
        #self.backgroundrect = self.background.get_rect()
        self.x = pygame.image.load("Pictures/x.png")
        self.o = pygame.image.load("Pictures/o.png")
        self.home = pygame.image.load("Pictures/home.png")
        self.icon = pygame.image.load("Pictures/icon.png")
        self.red_line = pygame.image.load("Pictures/red_line.png")
        self.red_line90 = pygame.image.load("Pictures/red_line90.png")
        self.red_line45l = pygame.image.load("Pictures/red_line45l.png")
        self.red_line45p = pygame.image.load("Pictures/red_line45p.png")
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("TIC TAC TOE by Adon")
    def played_round(self):
        self.game_round += 1
    def restart_game(self):
        self.screen.fill(self.color)
        self.screen.blit(self.background, (0,25))
        self.screen.blit(self.home, ((400 - self.home.get_width()), 0))
        pygame.display.flip()
        self.game_round = 0
        self.game_board = {i+1: "" for i in range(9)}
        self.game = True
    def change_background_color(self, r, g, b):
        self.color = r, g, b
    def check_win(self):
        if self.game_board[1] == self.game_board[2] == self.game_board[3] != "":
            self.screen.blit(self.red_line, (25,90))
            pygame.display.flip()
            game.game = False
            print_winner(self, 1)
        elif self.game_board[4] == self.game_board[5] == self.game_board[6] != "":
            self.screen.blit(self.red_line, (25,190))
            pygame.display.flip()
            game.game = False
            print_winner(self, 4)
        elif self.game_board[7] == self.game_board[8] == self.game_board[9] != "":
            self.screen.blit(self.red_line, (25,300))
            pygame.display.flip()
            game.game = False
            print_winner(self, 7)
        elif self.game_board[1] == self.game_board[4] == self.game_board[7] != "":
            self.screen.blit(self.red_line90, (70,50))
            pygame.display.flip()
            game.game = False
            print_winner(self, 1)
        elif self.game_board[2] == self.game_board[5] == self.game_board[8] != "":
            self.screen.blit(self.red_line90, (170,50))
            pygame.display.flip()
            game.game = False
            print_winner(self, 2)
        elif self.game_board[3] == self.game_board[6] == self.game_board[9] != "":
            self.screen.blit(self.red_line90, (275,50))
            pygame.display.flip()
            game.game = False
            print_winner(self, 3)
        elif self.game_board[1] == self.game_board[5] == self.game_board[9] != "":
            self.screen.blit(self.red_line45l, (50,55)) 
            pygame.display.flip()
            game.game = False
            print_winner(self, 1)
        elif self.game_board[7] == self.game_board[5] == self.game_board[3] != "":
            self.screen.blit(self.red_line45p, (40,65)) 
            pygame.display.flip()
            game.game = False
            print_winner(self, 7)
        elif self.game_round == 9: 
            game.game = False 
            print_winner(self, 0)
    def place_choice(self, pos, xo_templates):
        ttc, xo = xo_templates
        x,y = pos
        if ((x >= (400 - self.home.get_width())) & (y >= 0)) & ((x <= 400) & (y <= self.home.get_height())):
            self.menu = True
            self.display_menu()
            return
        if self.menu:
            if ((x >= 0) & (y >= 0)) & ((x <= 400) & (y <= 237.5)):
                print('BOT')
                self.menu = False
                return
            elif ((x >= 0) & (y >= 237.5)) & ((x <= 400) & (y <= 475)):
                self.menu = False
                self.restart_game()
                return
        if self.game:
            if ((x >= 50) & (y >= 62)) & ((x <= 130) & (y <= 142)):
                if self.game_board[1] == "":
                    self.screen.blit(ttc, (50,62))
                    pygame.display.flip()
                    self.game_board[1] = xo
                    self.played_round()
            elif ((x >= 150) & (y >= 62)) & ((x <= 230) & (y <= 142)):
                if  self.game_board[2] == "":
                    self.screen.blit(ttc, (150,62))
                    pygame.display.flip()
                    self.game_board[2] = xo
                    self.played_round()
            elif ((x >= 255) & (y >= 62)) & ((x <= 335) & (y <= 142)):
                if self.game_board[3] == "":
                    self.screen.blit(ttc, (255,62))
                    pygame.display.flip()
                    self.game_board[3] = xo
                    self.played_round()
            elif ((x >= 50) & (y >= 165)) & ((x <= 130) & (y <= 245)):
                if self.game_board[4] == "":
                    self.screen.blit(ttc, (50,165))
                    pygame.display.flip()
                    self.game_board[4] = xo
                    self.played_round()
            elif ((x >= 150) & (y >= 165)) & ((x <= 230) & (y <= 245)):
                if self.game_board[5] == "":
                    self.screen.blit(ttc, (145,165))
                    pygame.display.flip()
                    self.game_board[5] = xo
                    self.played_round()
            elif ((x >= 255) & (y >= 165)) & ((x <= 335) & (y <= 245)):
                if self.game_board[6] == "":
                    self.screen.blit(ttc, (255,165))
                    pygame.display.flip()
                    self.game_board[6] = xo
                    self.played_round()
            elif ((x >= 50) & (y >= 275)) & ((x <= 130) & (y <= 355)):
                if self.game_board[7] == "":
                    self.screen.blit(ttc, (40,275))
                    pygame.display.flip()
                    self.game_board[7] = xo
                    self.played_round()
            elif ((x >= 150) & (y >= 275)) & ((x <= 230) & (y <= 355)):
                if self.game_board[8] == "":
                    self.screen.blit(ttc, (135,275))
                    pygame.display.flip()
                    self.game_board[8] = xo
                    self.played_round()
            elif ((x >= 255) & (y >= 275)) & ((x <= 335) & (y <= 355)):
                if self.game_board[9] == "":
                    self.screen.blit(ttc, (245,275))
                    pygame.display.flip()
                    self.game_board[9] = xo
                    self.played_round()      
    def round_move(self):
        if self.game_round % 2:
            return game.o, 'o'
        else:
            return self.x, 'x'
    def display_menu(self):
        self.restart_game()
        self.game = False
        self.screen.fill(self.color)
        game.font = pygame.font.Font('Baby Marker.ttf', 45)
        single_player = game.font.render("Player vs BOT", True, (0, 0, 0))
        multiplayer = game.font.render("Player vs Player", True, (255, 255, 255))
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, 400, 237.5))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 237.5, 400, 475))
        self.screen.blit(single_player, ((400 - (single_player.get_width())) / 2, (237.5 - single_player.get_height()) / 2))
        self.screen.blit(multiplayer, ((400 - multiplayer.get_width()) / 2, (((237.5 -  multiplayer.get_height()) / 2) + 237.5)))
        pygame.display.flip()

def print_winner(game, pos):
    game.font = pygame.font.Font('Baby Marker.ttf', 75)
    if pos != 0:        
        xo = game.font.render(f'{game.game_board[pos].upper()}', True, (255, 0 ,0), (255, 255, 255))
        is_winner = game.font.render(' IS WINNER', True, (0, 0 ,0), (255, 255, 255))
        game.screen.blit(xo, ((400 - (xo.get_width() + is_winner.get_width())) / 2, 475 - xo.get_height()))
        game.screen.blit(is_winner, (((400 + xo.get_width()) - is_winner.get_width()) / 2, 475 - xo.get_height()))
        pygame.display.flip()
    else: 
        draw = game.font.render('DRAW', True, (255, 0 ,0), (255, 255, 255))
        game.screen.blit(draw, ((400 - draw.get_width() ) / 2, 475 - draw.get_height()))
        pygame.display.flip()    

if __name__ == "__main__":
    game = Game()
    game.display_menu()
    while True: #(game.game_round < 9) & game.game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game.place_choice(event.pos, game.round_move())
                    game.check_win()
                elif (event.button == 3) & (game.menu == False):
                    game.restart_game()




    