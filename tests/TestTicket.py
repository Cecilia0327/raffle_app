import unittest
from src.Ticket import Ticket

class TestTicket(unittest.TestCase):

    def test_ticket_generation(self):
        ticket = Ticket()
        # Assert that the ticket contains 5 numbers
        self.assertEqual(len(ticket.numbers), 5)
        # Assert that the numbers are within the expected range (1-15)
        for number in ticket.numbers:
            self.assertTrue(1 <= number <= 15)

    def test_ticket_unique_numbers(self):
        ticket = Ticket()
        # Assert that all numbers in the ticket are unique
        self.assertEqual(len(ticket.numbers), len(set(ticket.numbers)))
        
    def test_ticket_str_method(self):
        ticket = Ticket()
        ticket.numbers = [1, 2, 3, 4, 5]
        result = str(ticket)
        expected = "1 2 3 4 5"
        # Assert that the __str__ method returns the expected value
        self.assertEqual(result, expected)
    
    def test_compare_tickets(self):
        ticket = Ticket()
        ticket.numbers = [1, 2, 3, 4, 5]
        winning_ticket = Ticket()
        winning_ticket.numbers = [3, 4, 5, 6, 7]
        matches = ticket.compare(winning_ticket)
        self.assertEqual(matches, 3)

    def test_compare_no_match(self):
        ticket = Ticket()
        ticket.numbers = [1, 2, 3, 4, 5]
        winning_ticket = Ticket()
        winning_ticket.numbers = [6, 7, 8, 9, 10]
        matches = ticket.compare(winning_ticket)
        self.assertEqual(matches, 0)

    def test_compare_all_match(self):
        ticket = Ticket()
        ticket.numbers = [1, 2, 3, 4, 5]
        winning_ticket = Ticket()
        winning_ticket.numbers = [1, 2, 3, 4, 5]
        matches = ticket.compare(winning_ticket)
        self.assertEqual(matches, 5)

if __name__ == '__main__':
    unittest.main()
