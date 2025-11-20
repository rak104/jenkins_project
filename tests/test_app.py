import os
import sys
import unittest

# Add the project root to PYTHONPATH so we can import app.py
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import greet

class TestApp(unittest.TestCase):
	def test_greet(self):
		self.assertEqual(greet("Rawad Kansoh"), "Hello, World from Rawad Kansoh!")

if __name__ == "__main__ ":
    unittest.main()
