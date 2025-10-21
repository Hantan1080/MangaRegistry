# test_mangaregistry.py
"""
Tests for MangaRegistry module.
"""

import unittest
from mangaregistry import MangaRegistry

class TestMangaRegistry(unittest.TestCase):
    """Test cases for MangaRegistry class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaRegistry()
        self.assertIsInstance(instance, MangaRegistry)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaRegistry()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
