import unittest
from main import get_shell_selection, Shell
from unittest.mock import patch

class TestGetShellSelection(unittest.TestCase):

    def test_valid_input(self):
        """Tests that the function returns the correct shell type for valid input."""
        # Mock user input
        def mock_input(prompt):
            if prompt.endswith("(1-3): "):
                return "1"
            return "2"
        
        # Patch the input function
        with patch('builtins.input', mock_input):
            self.assertEqual(get_shell_selection(), Shell.CMD)
            self.assertEqual(get_shell_selection(), Shell.POWERSHELL)

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
