import unittest
from unittest.mock import patch, MagicMock
import os
import src

class TestRaffleApp(unittest.TestCase):
    def setUp(self):
        # Mute the output for all tests in this class
        patcher = patch('sys.stdout', new_callable=lambda: open(os.devnull, 'w'))
        self.addCleanup(patcher.stop)
        self.mock_stdout = patcher.start()
    
    def test_initial_state(self):
        raffle_app = src.RaffleApp()
        # Assert that the initial status is "Draw has not started"
        self.assertEqual(raffle_app.status, "Draw has not started")
        # Assert that the initial pot_size is 0
        self.assertEqual(raffle_app.pot_size, 0)
        # Assert that the players list is initially empty
        self.assertEqual(raffle_app.players, [])
        # Assert that the distribution is set to [0.1, 0.15, 0.25, 0.5]
        self.assertEqual(raffle_app.distribution, [0.1, 0.15, 0.25, 0.5])
    
    @patch('builtins.print')
    def test_display_menu_draw_not_started(self, mock_print):
        # Test if the display_menu() shows the correct output when status == not started
        raffle_app = src.RaffleApp()
        raffle_app.display_menu()
        mock_print.assert_any_call("Welcome to My Raffle App")
        mock_print.assert_any_call("[1] Start a New Draw")
        mock_print.assert_any_call("[2] Buy Tickets")
        mock_print.assert_any_call("[3] Run Raffle")
        mock_print.assert_any_call("[4] Exit App\n")
        
    @patch('builtins.print')
    def test_display_menu_draw_ongoing(self, mock_print):
        # Test if the display_menu() shows the correct output when status == ongoing
        # Mock the RaffleApp object
        mock_raffle_app = MagicMock()
        mock_raffle_app.status = "Draw is ongoing"
        mock_raffle_app.pot_size = 150
        src.RaffleApp.display_menu(mock_raffle_app)
        mock_print.assert_any_call("Welcome to My Raffle App")
        mock_print.assert_any_call("Status: Draw is ongoing. Raffle pot size is $150\n")
        mock_print.assert_any_call("[1] Start a New Draw")
        mock_print.assert_any_call("[2] Buy Tickets")
        mock_print.assert_any_call("[3] Run Raffle")
        mock_print.assert_any_call("[4] Exit App\n")
        
    @patch('builtins.input', return_value="1")
    def test_get_user_choice_valid_input_1(self, mock_input):
        # Test if valid input '1' is captured correctly
        raffle_app = src.RaffleApp()
        choice = raffle_app.get_user_choice()
        self.assertEqual(choice, "1")
    

    @patch('builtins.input', side_effect=["1", "4"])
    @patch.object(src.RaffleApp, 'start_new_draw')
    def test_choice_1_triggers_start_new_draw(self, mock_start_new_draw, mock_input):
        # Test start_new_draw was called when "1" was entered
        raffle_app = src.RaffleApp()
        raffle_app.run()
        mock_start_new_draw.assert_called_once()

    @patch('builtins.input', side_effect=["2", "4"])
    @patch('builtins.print')
    def test_buy_tickets_invalid_when_no_draw(self, mock_print, mock_input):
        raffle_app = src.RaffleApp()
        raffle_app.run()
        mock_print.assert_any_call("Invalid option: Start a draw before buying tickets.")

    @patch('builtins.input', side_effect=["3", "4"])
    @patch('builtins.print')
    def test_run_raffle_invalid_when_no_draw(self, mock_print, mock_input):
        raffle_app = src.RaffleApp()
        raffle_app.run()
        mock_print.assert_any_call("Invalid option: Start a draw before running the raffle.")


    @patch.object(src.RaffleApp, 'return_to_menu')  # Mock return_to_menu
    def test_start_new_draw_changes_status_and_pot_size(self, mock_return_to_menu):
        raffle_app = src.RaffleApp()
        raffle_app.start_new_draw()
        self.assertEqual(raffle_app.status, "Draw is ongoing")
        self.assertEqual(raffle_app.pot_size, 100)
        
    @patch('builtins.input', return_value="Alice,6")
    @patch('builtins.print')
    def test_buy_tickets_invalid_purchase(self, mock_print, mock_input):
        # Create a new instance of RaffleApp with an ongoing draw
        raffle_app = src.RaffleApp()
        raffle_app.status = "Draw is ongoing"
        raffle_app.buy_tickets()
        # Assert that no player was added
        self.assertEqual(len(raffle_app.players), 0)
        # Assert that the invalid purchase message was printed
        mock_print.assert_any_call("Invalid purchase: Maximum 5 tickets per draw")