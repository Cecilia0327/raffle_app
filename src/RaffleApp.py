import sys
import tty
import termios
import src.Player as Player
import src.Ticket as Ticket

class RaffleApp:
    def __init__(self):
        self.status = "Draw has not started"
        self.pot_size = 0
        self.players = []
        self.distribution = [0.1, 0.15, 0.25, 0.5]
        
    def display_menu(self):
        #main menu display
        print("Welcome to My Raffle App")
        if self.status == "Draw is ongoing":
            print(f"Status: {self.status}. Raffle pot size is ${self.pot_size}\n")
        else:
            print(f"Status: {self.status}\n")
        print("[1] Start a New Draw")
        print("[2] Buy Tickets")
        print("[3] Run Raffle")
        print("[4] Exit App\n")

    def get_user_choice(self):
        #capture user option
        choice = input("Enter your choice (1, 2, 3 or 4): ")
        return choice
    
    def start_new_draw(self):
        #Option 1: start a new draw
        self.pot_size += 100
        self.status = "Draw is ongoing"
        print(f"\nNew Raffle draw has been started. Initial pot size: ${self.pot_size}")
        self.return_to_menu()

    def buy_tickets(self):
        #prevent buying ticket before a draw is started
        if self.status != "Draw is ongoing":
            print("Invalid option: Start a draw before buying tickets.")
            return
        print("\nEnter your name, no of tickets to purchase")
        
        #capture purchase details
        pair = input().split(",")
        name = pair[0]
        number_of_tickets = int(pair[1])
        
        #limit the number of tickets to 5
        if number_of_tickets > 5:
            print("Invalid purchase: Maximum 5 tickets per draw")
            return
        #empty purchase
        elif number_of_tickets <= 0:
            print("No purchase happened")
            return
        
        #add player to the pool and increase pot size
        new_player = Player(name)
        new_player.buy_tickets(number_of_tickets)
        self.players.append(new_player)
        self.pot_size += number_of_tickets * 5
        self.return_to_menu()
    
    def run_raffle(self):
        #prevent running raffle before a draw is started
        if self.status != "Draw is ongoing":
            print("Invalid option: Start a draw before running the raffle.")
            return
        #warn no existing player
        if len(self.players) == 0:
            print("Warning: No player in the game")
            return
        
        print("\nRunning Raffle..\n")
        
        #generate winning ticket
        winning_ticket = Ticket()
        print(f"Winning Ticket is {winning_ticket}\n")
        
        money_left = self.pot_size
        #for each of the players, decide the winning group of all their tickets
        for player in self.players:
            player.compare_tickets(winning_ticket)
        
        #for each winning group, count no. of winners and how the reward is distributed
        for i in range(2, 6):
            print(f"\nGroup {i} Winners (Jackpot):\n" if i == 5 else f"\nGroup {i} Winners:\n")
            count = 0
            for player in self.players:
                if player.winning[i - 2] != 0:
                    count += player.winning[i - 2]
            if count != 0:
                money_left -= self.pot_size * self.distribution[i-2]
                reward = (self.pot_size * self.distribution[i-2])/count
                for player in self.players:
                    if player.winning[i - 2] != 0:
                        print(f"{player} with {player.winning[i - 2]} winning ticket(s)- ${reward*player.winning[i - 2]}")
            else:
                print("Nil")

        self.return_to_menu()
        self.status = "Draw has not started"
        self.pot_size = money_left
        self.players = []
        
    def return_to_menu(self):
        #press any key to return to main menu
        print("Press any key to return to the main menu\n")
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
    def run(self):
        #run the app
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == "1":
                self.start_new_draw()
            elif choice == "2":
                self.buy_tickets()
            elif choice == "3":
                self.run_raffle()
            elif choice =="4":
                break
            else:
                print("Invalid option, please try again.")
                self.return_to_menu()
        
if __name__ == "__main__":
    raffle_app=RaffleApp()
    raffle_app.run()