import unittest
import sys
import os

# Ensure the src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import get_hello_world
from app import swap_case_and_reverse

class TestApp(unittest.TestCase):
    def test_get_hello_world(self):
        self.assertEqual(get_hello_world(), 'Hello, World!')
    def test_swap_case_and_reverse(self):
        self.assertEqual(swap_case_and_reverse("Hello, World! 123"), "321 !DLROw ,OLLEh")
        self.assertEqual(swap_case_and_reverse("abcdef"), "FEDCBA")
        self.assertEqual(swap_case_and_reverse("XYZ"), "zyx")
        self.assertEqual(swap_case_and_reverse("123!@#"), "#@!321")
        self.assertEqual(swap_case_and_reverse(""), "")
        
if __name__ == '__main__':
    unittest.main()