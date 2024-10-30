import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import get_shell_selection, Shell
from unittest.mock import patch

class TestGetShellSelection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_inputs = {
            "valid_cmd": "1",
            "valid_powershell": "2",
            "valid_bash": "3",
            "invalid": "4"
        }

    def test_valid_input(self):
        """Tests that the function returns the correct shell type for valid input."""
        # Mock user input sequence
        inputs = iter(["1", "2", "3"])
        
        def mock_input(prompt):
            return next(inputs)
        
        # Patch the input function and verify all shell types
        with patch('builtins.input', mock_input):
            self.assertEqual(get_shell_selection(), Shell.CMD)
            self.assertEqual(get_shell_selection(), Shell.POWERSHELL)
            self.assertEqual(get_shell_selection(), Shell.BASH)

    def test_invalid_input(self):
        """Tests that the function handles invalid input correctly."""
        # Mock user input
        def mock_input(prompt):
            return "4"  # Invalid input

        # Patch the input function
        with patch('builtins.input', mock_input):
            self.assertRaises(ValueError, get_shell_selection)

if __name__ == '__main__':
    unittest.main()


