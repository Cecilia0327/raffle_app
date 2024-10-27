import src.Ticket as Ticket

class Player():
    def __init__(self, name):
        self.name = name
        self.tickets = []
        self.winning = [0] * 4
        
    def buy_tickets(self, number_of_tickets):
        #generate new tickets and assign to current Player
        print(f"\nHi {self.name}, you have purchased {number_of_tickets} ticket(s)-")
        for i in range(number_of_tickets):
            ticket = Ticket()
            self.tickets.append(ticket)
            print(f"Ticket {i}: {ticket}")
    
    def compare_tickets(self, winning_ticket):
        #decide the winning group all tickets of current Player
        matches = []
        for ticket in self.tickets:
            matches.append(ticket.compare(winning_ticket))
        
        self.winning[0] = matches.count(2)
        self.winning[1] = matches.count(3)
        self.winning[2] = matches.count(4)
        self.winning[3] = matches.count(5)
    
    def __str__(self):
        return self.name