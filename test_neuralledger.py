# test_neuralledger.py
"""
Tests for NeuralLedger module.
"""

import unittest
from neuralledger import NeuralLedger

class TestNeuralLedger(unittest.TestCase):
    """Test cases for NeuralLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuralLedger()
        self.assertIsInstance(instance, NeuralLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuralLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
