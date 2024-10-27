import random

class Ticket():
    def __init__(self):
        self.numbers = self.generate_numbers()
    
    def generate_numbers(self):
        #generate 5 unique number in 1-15
        return random.sample(range(1, 16), 5)
    
    def compare(self, winning_ticket):
        #decide the winning group of current Ticket
        return len(set(self.numbers) & set(winning_ticket.numbers))
    
    def __str__(self):
        #string representation of current Ticket
        return ' '.join(map(str, self.numbers))