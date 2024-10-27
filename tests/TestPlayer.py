import unittest
from unittest.mock import patch
from src.Player import Player
from src.Ticket import Ticket

class TestPlayer(unittest.TestCase):

    def test_player_creation(self):
        player = Player("Alice")
        self.assertEqual(player.name, "Alice")
        # Assert that the player initially has no tickets
        self.assertEqual(len(player.tickets), 0)

    def test_buy_tickets(self):
        player = Player("Alice")
        player.buy_tickets(3)
        # Assert that 3 tickets were added
        self.assertEqual(len(player.tickets), 3)
        # Ensure that each item in tickets is an instance of Ticket
        for ticket in player.tickets:
            self.assertIsInstance(ticket, Ticket)
    
    @patch.object(Ticket, 'compare')
    def test_compare_tickets(self, mock_compare):
        # Set up a Player with 3 tickets
        player = Player("Alice")
        player.tickets = [Ticket(), Ticket(), Ticket()]
        player.winning = [0, 0, 0, 0]
        # Set up a winning ticket
        winning_ticket = Ticket()
        # Ticket 1 has 2 matches, Ticket 2 has 3 matches, Ticket 3 has 5 matches
        mock_compare.side_effect = [2, 3, 5]
        # Call compare_tickets with the winning ticket
        player.compare_tickets(winning_ticket)
        # Assert the winning array is updated correctly
        self.assertEqual(player.winning, [1, 1, 0, 1])

if __name__ == '__main__':
    unittest.main()
