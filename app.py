import sys, pygame
from scripts.gui import Window

if __name__ == "__main__":
    app = Window()
    app.display_menu()
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and app.menu_is_displayed:
                app.menu_choice(event.pos)
                continue
            if event.button == 1 and not app.menu_is_displayed:
                app.play_one_round(event.pos)
                continue
            if event.button == 3 and not app.menu_is_displayed: 
                app.start_new_game()
                continue

      
    




    