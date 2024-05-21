import pygame
import sys
from setup import Game  # Import the Game class from setup.py
from Script.utils import load_image

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# Colors

PLAY = load_image('start.png').convert()
QUIT = load_image('quit.png').convert()
TITLE = load_image('title.png').convert()


# Fonts
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 36)

# Buttons
PLAY = pygame.transform.scale(PLAY, (220, 110))
QUIT = pygame.transform.scale(QUIT, (200, 100))
TITLE = pygame.transform.scale(TITLE, (300, 300))

play_button = PLAY.get_rect(topleft=(305, 200))
quit_button = QUIT.get_rect(topleft=(300, 300))
menu_title = TITLE.get_rect(topleft=(260, 20))


background = load_image('background.png').convert()
background = pygame.transform.smoothscale(background, screen.get_size())

pygame.mixer.music.load('Aset/sound_effect/Backsound/main_menu.mp3')  
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


def main_menu():
    while True:

        

        screen.blit(background, (0, 0))

        mouse_pos = pygame.mouse.get_pos()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    game = Game()
                    game.run()
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        

        if play_button.collidepoint(mouse_pos):
            play_img_hover = pygame.transform.scale(PLAY, (230, 115))  # Slightly larger for hover effect
            screen.blit(play_img_hover, (play_button.x - 10, play_button.y - 2))
        else:
            screen.blit(PLAY, play_button.topleft)

        if quit_button.collidepoint(mouse_pos):
            quit_img_hover = pygame.transform.scale(QUIT, (210, 105))  # Slightly larger for hover effect
            screen.blit(quit_img_hover, (quit_button.x - 10, quit_button.y - 2))
        else:
            screen.blit(QUIT, quit_button.topleft)

        screen.blit(TITLE, menu_title.topleft)


        
        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main_menu()
