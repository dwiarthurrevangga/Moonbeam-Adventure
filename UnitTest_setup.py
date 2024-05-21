import unittest
import pygame
from Script.tilemap import TileMap
from Script.entities import Player, Enemy
from Script.utils import load_image, load_images, Animation
from Script.particle import Particle
from Script.spark import Spark
from setup import Game

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game()
        
    def test_player_initial_position(self):
        initial_position = (50, 50)
        self.assertEqual(self.game.player.pos, initial_position, "Player initial position should be (50, 50)")

    def test_player_jump(self):
        initial_air_time = self.game.player.air_time
        self.game.player.jump()
        self.assertNotEqual(self.game.player.air_time, initial_air_time, "Player air_time should change after jumping")
        
    def test_load_level(self):
        initial_level = self.game.level
        self.game.load_level(initial_level)
        self.assertEqual(self.game.level, initial_level, f"Level should be {initial_level} after loading")

    def test_enemy_spawn(self):
        self.game.load_level(0)
        initial_enemy_count = len(self.game.enemies)
        self.assertGreater(initial_enemy_count, 0, "There should be enemies spawned in the level")
        
    def test_projectile_collision(self):
        self.game.projectiles.append([[100, 100], 1, 0])
        self.game.player.pos = [100, 100]
        self.game.player.rect = lambda: pygame.Rect(100, 100, 10, 10)
        self.game.run_one_frame()
        self.assertEqual(len(self.game.projectiles), 0, "Projectile should be removed on collision with player")

if __name__ == "__main__":
    unittest.main()
