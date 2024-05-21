import unittest
import pygame
from unittest.mock import Mock
from Script.entities import EntityPhysics, Player, Enemy
from Script.particle import Particle
from Script.spark import Spark
from Script.tilemap import TileMap

class TestEntityPhysics(unittest.TestCase):

    def setUp(self):
        self.game = Mock()
        self.game.assets = {
            'enemy/idle': Mock(),
            'enemy/run': Mock(),
            'player/idle': Mock(),
            'player/run': Mock(),
            'player/jump': Mock(),
            'player/slide': Mock(),
            'player/wall_slide': Mock()
        }
        self.tilemap = Mock(spec=TileMap)
        self.tilemap.physics_rect_around.return_value = []

    def test_entity_physics_initialization(self):
        entity = EntityPhysics(self.game, 'player', (50, 50), (10, 10))
        self.assertEqual(entity.pos, [50, 50])
        self.assertEqual(entity.size, (10, 10))
        self.assertEqual(entity.velocity, [0, 0])
        self.assertEqual(entity.collisions, {'up': False, 'down': False, 'right': False, 'left': False})

    def test_entity_physics_update(self):
        entity = EntityPhysics(self.game, 'player', (50, 50), (10, 10))
        entity.update(self.tilemap, movement=(1, 0))
        self.assertEqual(entity.pos[0], 51)
        self.assertEqual(entity.pos[1], 50)

    def test_entity_physics_collision(self):
        entity = EntityPhysics(self.game, 'player', (50, 50), (10, 10))
        self.tilemap.physics_rect_around.return_value = [pygame.Rect(60, 50, 10, 10)]
        entity.update(self.tilemap, movement=(1, 0))
        self.assertTrue(entity.collisions['right'])
        self.assertEqual(entity.pos[0], 50)

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.game = Mock()
        self.game.assets = {
            'player/idle': Mock(),
            'player/run': Mock(),
            'player/jump': Mock(),
            'player/slide': Mock(),
            'player/wall_slide': Mock()
        }
        self.tilemap = Mock(spec=TileMap)
        self.tilemap.physics_rect_around.return_value = []

    def test_player_initialization(self):
        player = Player(self.game, (50, 50), (10, 10))
        self.assertEqual(player.pos, [50, 50])
        self.assertEqual(player.size, (10, 10))
        self.assertEqual(player.velocity, [0, 0])
        self.assertEqual(player.air_time, 0)
        self.assertEqual(player.jumps, 1)

    def test_player_jump(self):
        player = Player(self.game, (50, 50), (10, 10))
        player.jumps = 1
        jumped = player.jump()
        self.assertTrue(jumped)
        self.assertEqual(player.velocity[1], -4)
        self.assertEqual(player.jumps, 0)

    def test_player_dash(self):
        player = Player(self.game, (50, 50), (10, 10))
        player.dash()
        self.assertEqual(player.dashing, 60 if not player.flip else -60)

class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.game = Mock()
        self.game.assets = {
            'enemy/idle': Mock(),
            'enemy/run': Mock(),
            'gun': Mock()
        }
        self.tilemap = Mock(spec=TileMap)
        self.tilemap.physics_rect_around.return_value = []

    def test_enemy_initialization(self):
        enemy = Enemy(self.game, (50, 50), (10, 10))
        self.assertEqual(enemy.pos, [50, 50])
        self.assertEqual(enemy.size, (10, 10))
        self.assertEqual(enemy.velocity, [0, 0])
        self.assertEqual(enemy.walking, 0)

    def test_enemy_update(self):
        enemy = Enemy(self.game, (50, 50), (10, 10))
        enemy.walking = 10
        enemy.update(self.tilemap, movement=(1, 0))
        self.assertTrue(enemy.walking <= 10)
        self.assertEqual(enemy.pos[0], 51)

if __name__ == "__main__":
    unittest.main()
