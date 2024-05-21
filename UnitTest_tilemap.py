import unittest
from unittest.mock import Mock, patch
import json
import pygame
from io import StringIO

# Mock game assets for rendering
mock_assets = {
    'grass': [Mock(), Mock(), Mock()],
    'stone': [Mock(), Mock(), Mock()],
    'brick': [Mock(), Mock(), Mock()],
    'flag': [Mock(), Mock(), Mock()],
    'trap': [Mock(), Mock(), Mock()],
}

class MockGame:
    def __init__(self):
        self.assets = mock_assets

# Import the TileMap class from your module (assuming it is named tilemap_module)
from Script.tilemap import TileMap

class TestTileMap(unittest.TestCase):

    def setUp(self):
        self.game = MockGame()
        self.tile_map = TileMap(self.game)
        
    def test_extract(self):
        self.tile_map.offgrid_tiles = [
            {'type': 'grass', 'variant': 0, 'pos': [10, 10]},
            {'type': 'stone', 'variant': 1, 'pos': [20, 20]}
        ]
        self.tile_map.tilemap = {
            '1;1': {'type': 'grass', 'variant': 0, 'pos': [1, 1]},
            '2;2': {'type': 'brick', 'variant': 2, 'pos': [2, 2]}
        }
        extracted = self.tile_map.extract([('grass', 0)])
        self.assertEqual(len(extracted), 2)
        self.assertIn({'type': 'grass', 'variant': 0, 'pos': [10, 10]}, extracted)
        self.assertIn({'type': 'grass', 'variant': 0, 'pos': [16, 16]}, extracted)

    def test_tiles_around(self):
        self.tile_map.tilemap = {
            '0;0': {'type': 'grass', 'variant': 0, 'pos': [0, 0]},
            '1;0': {'type': 'stone', 'variant': 1, 'pos': [1, 0]},
            '0;1': {'type': 'brick', 'variant': 2, 'pos': [0, 1]}
        }
        tiles = self.tile_map.tiles_around((8, 8))
        self.assertEqual(len(tiles), 3)
        self.assertIn({'type': 'grass', 'variant': 0, 'pos': [0, 0]}, tiles)

    @patch('tilemap_module.open', create=True)
    def test_save(self, mock_open):
        mock_open.return_value = StringIO()
        self.tile_map.tilemap = {'1;1': {'type': 'grass', 'variant': 0, 'pos': [1, 1]}}
        self.tile_map.save('dummy_path')
        mock_open.assert_called_with('dummy_path', 'w')
        mock_open.return_value.write.assert_called()

    @patch('tilemap_module.open', create=True)
    def test_load(self, mock_open):
        mock_open.return_value = StringIO(json.dumps({
            'tilemap': {'1;1': {'type': 'grass', 'variant': 0, 'pos': [1, 1]}},
            'tile_size': 16,
            'offgrid': [{'type': 'stone', 'variant': 1, 'pos': [10, 10]}]
        }))
        self.tile_map.load('dummy_path')
        mock_open.assert_called_with('dummy_path', 'r')
        self.assertEqual(self.tile_map.tilemap, {'1;1': {'type': 'grass', 'variant': 0, 'pos': [1, 1]}})
        self.assertEqual(self.tile_map.tile_size, 16)
        self.assertEqual(self.tile_map.offgrid_tiles, [{'type': 'stone', 'variant': 1, 'pos': [10, 10]}])

    def test_solid_check(self):
        self.tile_map.tilemap = {'1;1': {'type': 'grass', 'variant': 0, 'pos': [1, 1]}}
        result = self.tile_map.solid_check((16, 16))
        self.assertEqual(result, {'type': 'grass', 'variant': 0, 'pos': [1, 1]})

    def test_physics_rect_around(self):
        self.tile_map.tilemap = {
            '0;0': {'type': 'grass', 'variant': 0, 'pos': [0, 0]},
            '1;0': {'type': 'stone', 'variant': 1, 'pos': [1, 0]}
        }
        rects = self.tile_map.physics_rect_around((8, 8))
        self.assertEqual(len(rects), 2)
        self.assertIn(pygame.Rect(0, 0, 16, 16), rects)
        self.assertIn(pygame.Rect(16, 0, 16, 16), rects)

    def test_autotile(self):
        self.tile_map.tilemap = {
            '0;0': {'type': 'grass', 'variant': 0, 'pos': [0, 0]},
            '1;0': {'type': 'grass', 'variant': 0, 'pos': [1, 0]},
            '0;1': {'type': 'grass', 'variant': 0, 'pos': [0, 1]}
        }
        self.tile_map.autotile()
        self.assertEqual(self.tile_map.tilemap['0;0']['variant'], 1)  # Example variant
        self.assertEqual(self.tile_map.tilemap['1;0']['variant'], 6)  # Example variant
        self.assertEqual(self.tile_map.tilemap['0;1']['variant'], 4)  # Example variant

    @patch('tilemap_module.pygame.Surface')
    def test_render(self, mock_surface):
        mock_surf = mock_surface.return_value
        self.tile_map.offgrid_tiles = [{'type': 'grass', 'variant': 0, 'pos': [10, 10]}]
        self.tile_map.tilemap = {'0;0': {'type': 'grass', 'variant': 0, 'pos': [0, 0]}}
        self.tile_map.render(mock_surf)
        self.assertTrue(mock_surf.blit.called)

if __name__ == "__main__":
    unittest.main()
