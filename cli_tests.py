import unittest
from unittest.mock import patch
from cli import CLI

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.cli = CLI("Test Menu")
    
    def test_add_option(self):
        def dummy_function():
            pass
        self.cli.add_option("Test Option", dummy_function)
        self.assertEqual(len(self.cli.options), 1)
        self.assertEqual(self.cli.options[0][0], "Test Option")
        self.assertEqual(self.cli.options[0][1], dummy_function)

    @patch('builtins.input', side_effect=['1'])
    def test_choose_valid_option(self, mock_input):
        def dummy_function():
            pass
        self.cli.add_option("Test Option", dummy_function)
        choice = self.cli._CLI__choose()
        self.assertEqual(choice, 1)

    @patch('builtins.input', side_effect=['invalid', '1'])
    def test_choose_invalid_option(self, mock_input):
        def dummy_function():
            pass
        self.cli.add_option("Test Option", dummy_function)
        with patch('builtins.print') as mock_print:
            choice = self.cli._CLI__choose()
            self.assertEqual(choice, 1)
            mock_print.assert_called_with('\x1b[31mERROR! Invalid input. Please enter a number.')

    @patch('builtins.input', side_effect=['0'])
    def test_choose_back_sub_menu(self, mock_input):
        sub_menu = CLI("Sub Menu", False)
        def dummy_function():
            pass
        sub_menu.add_option("Test Option", dummy_function)
        with patch.object(sub_menu, 'run', return_value=None) as mock_run:
            sub_menu.run()
            mock_run.assert_called()

if __name__ == '__main__':
    unittest.main()