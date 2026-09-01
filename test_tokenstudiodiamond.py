# test_tokenstudiodiamond.py
"""
Tests for TokenStudioDiamond module.
"""

import unittest
from tokenstudiodiamond import TokenStudioDiamond

class TestTokenStudioDiamond(unittest.TestCase):
    """Test cases for TokenStudioDiamond class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenStudioDiamond()
        self.assertIsInstance(instance, TokenStudioDiamond)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenStudioDiamond()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
