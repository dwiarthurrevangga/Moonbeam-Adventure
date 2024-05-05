import pygame
import sys

from Script.tilemap import TileMap
from Script.entities import EntityPhysics
from Script.utils import load_image, load_images
class Game :
    def __init__(self):
        pygame.init()
        width = 960
        height = 540

        self.screen = pygame.display.set_mode((width, height))
        self.display = pygame.Surface((480 , 270))
        self.clock = pygame.time.Clock()
        self.movement = [False, False]
        
        self.assets = {
            'player' : load_image('player/cloud.gif'),
            'stone' : load_images('tiles/stone'),
            #'itembox' : load_images('tiles/itembox')
            


        }
        print(self.assets)
        

        self.player = EntityPhysics(self, 'player', (50, 50), (1, 1))
        self.tilemap = TileMap(self, tile_size=16)

    def run(self):
        while True :
            bg = load_image('/background/io.jpg')
            self.display.fill((100, 100, 100))

            self.tilemap.render(self.display)
            
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    sys.exit()
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT :
                        self.movement [1] = True
                    if event.key == pygame.K_UP:
                        event.player.velocity[1] = -3


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT :
                        self.movement [1] = False
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()



