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
WHITE = (255, 255, 255)
PURPLE = (113, 31, 128)
BLACK = (0, 0, 0)
PINK = (179, 89, 194)

# Fonts
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 36)

# Buttons
play_button = pygame.Rect(300, 200, 200, 50)
quit_button = pygame.Rect(300, 300, 200, 50)

background = load_image('background.png').convert()
background = pygame.transform.smoothscale(background, screen.get_size())


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
            pygame.draw.rect(screen, PURPLE, play_button)
        else:
            pygame.draw.rect(screen, PINK, play_button)

        if quit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, PURPLE, quit_button)
        else:
            pygame.draw.rect(screen, PINK, quit_button)

        play_text = font.render("Play", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)

        screen.blit(play_text, (play_button.x + 70, play_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 70, quit_button.y + 10))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main_menu()
