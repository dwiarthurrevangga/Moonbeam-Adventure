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
        
        

        self.player = EntityPhysics(self, 'player', (50, 50), (8, 15))
        self.tilemap = TileMap(self, tile_size=16)
        self.scroll = [0, 0]

    def run(self):
        while True :
            
            self.display.fill((100, 100, 100))

            self.tilemap.render(self.display)

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)
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
                        self.player.velocity[1] = -3


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT :
                        self.movement [1] = False
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()



