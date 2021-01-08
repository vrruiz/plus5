import unittest
import plus5

from plus5unittest import TestCase

class TestProcessingApi(TestCase):

    """
    def test_size_default(self):
        self.assertEqual(height, 100)
        self.assertEqual(width, 100)

    def test_size(self):
        plus5.size(300,300)
        self.assertEqual(height, 300)
        self.assertEqual(width, 300)
    """

    def test_color(self):
        gray = plus5.color(127)
        self.assertEqual(gray, (127, 127, 127))
        rgb = plus5.color(0, 0, 0)
        self.assertEqual(rgb, (0, 0, 0))
        rgba = plus5.color(255, 255, 255, 0)
        self.assertEqual(rgba, (255, 255, 255, 0))

if __name__ == '__main__':
    unittest.main()
