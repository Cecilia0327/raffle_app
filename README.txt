Design Overview:
The Raffle App is designed to simulate a simple lottery system, where users can purchase tickets, and a winning ticket is generated randomly. The application follows an object-oriented design with core components structured into distinct classes:
RaffleApp Class: Manages the overall flow of the application, including starting a new draw, processing ticket purchases, running the raffle, and distributing prizes. It interacts with the Player and Ticket classes to facilitate these actions.
Player Class: Represents individual players in the raffle. Each player can purchase multiple tickets (up to 5 per draw) and has a list of tickets that can be compared against the winning ticket.
Ticket Class: Represents a single raffle ticket. Each ticket contains a set of 5 unique numbers between 1 and 15. It has a method (compare) to check how many of its numbers match the winning ticket’s numbers.
Prize Distribution: The total prize pot is distributed based on the number of matching numbers (2, 3, 4, or 5) according to the prize group. If multiple players match the same number of winning numbers, the prize is shared equally among them.

Key Assumptions:
Ticket Purchase Limit: Each player can purchase a maximum of 5 tickets per draw and cannot purchase 0 or negative number of tickets (Player will not be added to the pool).
Order of Actions: Cannot buy tickets before start a draw; Cannot run raffle before start a draw; Cannot run raffle with an empty pool.
Unique Ticket Numbers: Each ticket consists of 5 unique numbers between 1 and 15.
Prize Distribution: The prize pool is divided into four prize groups, where the percentage of the total prize pot increases with the number of matches:


Test Coverage:
The Raffle App follows a test-driven development approach, with extensive unit tests written to cover key functionalities of the app. These tests ensure that the core components (e.g., ticket comparison, raffle execution, and prize distribution) work as expected under various conditions.

Ticket Class:
compare() method: Tests cover scenarios where tickets have no matches, partial matches (2, 3, or 4 numbers), and complete matches (5 numbers for the jackpot).
Different test cases simulate varying levels of matching to ensure the comparison logic is correct.

Player Class:
compare_tickets() method: Verifies that the player’s tickets are correctly compared against the winning ticket, and that the correct number of winning tickets (per prize group) is counted.
Tests include scenarios with no winning tickets, partial wins, and multiple tickets in various prize groups.

RaffleApp Class:
Starting a new draw: Ensures the prize pot is initialized correctly, and the draw status changes as expected.
Buying tickets: Tests ensure that the correct number of tickets is purchased, the pot size is updated accordingly, and restrictions (like the maximum number of tickets per draw) are enforced.
Running the raffle: The key method is tested under various conditions
Returning to menu: Tests verify that after each action (buying tickets or running the raffle), users are correctly returned to the main menu.


To Run the App:
python version: 3.10
OS: macOS
    1.Set up a virtual environment 
        python3 -m venv .venv
        source .venv/bin/activate
    2.Install the required dependencies:
        pip install -r requirements.txt
    3.To run the RaffleApp
        python -m src.RaffleApp
    4.TO run the unit tests
        python -m unittest discover -s tests -p "*.py"


