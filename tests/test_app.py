import unittest
from app import greet

class TestApp(unittest.TestCase):
	def test_greet(self):
		self.assertEqual(greet("World"), "Hello, World from Rawad Kansoh!")

if name == " main ":
    unittest.main()
