# test_heartlong.py
"""
Tests for HeartLong module.
"""

import unittest
from heartlong import HeartLong

class TestHeartLong(unittest.TestCase):
    """Test cases for HeartLong class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HeartLong()
        self.assertIsInstance(instance, HeartLong)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HeartLong()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
