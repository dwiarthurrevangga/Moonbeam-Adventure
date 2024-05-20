import pygame
import sys
from Script.utils import load_image
from main_menu import main_menu




pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pause Menu")


BG_COLOR = (52, 78, 91)



resume_img = load_image("resume.png").convert()
backToMenu_img = load_image("menu.png").convert()

resume_img = pygame.transform.scale(resume_img, (200, 120))
backToMenu_img = pygame.transform.scale(backToMenu_img, (200, 120))

resume_button = resume_img.get_rect(topleft=(305, 200))
menu_button = backToMenu_img.get_rect(topleft=(300, 300))



# game loop
def pause_menu(game):
    paused = True
    while paused :
        screen.fill(BG_COLOR)

        mouse_pos = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.collidepoint(event.pos):
                    paused = False
                    game.run()
                elif menu_button.collidepoint(event.pos):
                    main_menu()

        if resume_button.collidepoint(mouse_pos):
            resume_img_hover = pygame.transform.scale(resume_img, (210, 125))  # Slightly larger for hover effect
            screen.blit(resume_img_hover, (resume_button.x - 10, resume_button.y - 5))
        else:
            screen.blit(resume_img, resume_button.topleft)

        if menu_button.collidepoint(mouse_pos):
            menu_img_hover = pygame.transform.scale(backToMenu_img, (210, 125))  # Slightly larger for hover effect
            screen.blit(menu_img_hover, (menu_button.x - 10, menu_button.y - 5))
        else:
            screen.blit(backToMenu_img, menu_button.topleft)

        pygame.display.flip()
        pygame.time.Clock().tick(60)
        
if __name__ == "__main__":
    from setup import Game  # Import Game class for standalone testing
    game = Game()
    pause_menu(game)