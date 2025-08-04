# test_checkercompliance.py
"""
Tests for CheckerCompliance module.
"""

import unittest
from checkercompliance import CheckerCompliance

class TestCheckerCompliance(unittest.TestCase):
    """Test cases for CheckerCompliance class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CheckerCompliance()
        self.assertIsInstance(instance, CheckerCompliance)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CheckerCompliance()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
