import unittest
import plus5

class TestCase(unittest.TestCase):

    def setUp(self):
        plus5._init()

    def tearDown(self):
        plus5._end()
