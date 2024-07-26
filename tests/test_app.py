import unittest
import sys
import os

# Ensure the src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import get_hello_world

class TestApp(unittest.TestCase):
    def test_get_hello_world(self):
        self.assertEqual(get_hello_world(), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()