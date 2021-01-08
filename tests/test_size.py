import unittest
import plus5

from plus5unittest import TestCase

class TestProcessingApi(TestCase):

    def test_size(self):
        plus5.size(300,300)
        self.assertEqual(height, 300)
        self.assertEqual(width, 300)
    
