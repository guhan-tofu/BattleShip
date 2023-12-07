from components import initialise_board, create_battleships, place_battleships, try_place_ship
from game_engine import attack, cli_coordinates_input, print_board

players={}
import random
import json

points=[]

def generate_attack(user_board):
    """function used by AI opponent to generate attack coordinates"""
    global points # change the list values outside of its current scope.
    while True:
        x_ai = random.randint(0, len(user_board) - 1)
        y_ai = random.randint(0, len(user_board[0]) - 1)
        
        if (x_ai, y_ai) not in points: # ensures the random function gives new coordinates everytime
            points.append((x_ai, y_ai))
            break
    return (x_ai, y_ai)



def ai_opponent_game_loop():
    """Function which implements a simple version of battleship game"""
    def update_placement_file(placement_data="placement.json"):
        """A function which allows us to update the custom positions of player ships"""
        with open("placement.json", "w") as json_file:
            json.dump(placement_data, json_file)

    user_name = input("Enter your username: ")
    pl_board=initialise_board()
    ai_board=initialise_board()
    pl_ships=create_battleships()
    ai_ships=create_battleships()
    place_battleships(ai_board, ai_ships, algorithm='random')
    place_battleships(pl_board, pl_ships, algorithm='custom',placement_file="placement.json")
    print("Your current board status: \n")
    print_board(pl_board)
    choice=input("Do you want to update your battleship placement? (yes/no): ").lower()
    if choice == "yes":
        pl_board=initialise_board()
        placement_data = {}
        for ship, size in pl_ships.items():
            while True:
                try:
                    print(f"Enter placement for {ship} (size: {size}):")
                    x = int(input("Enter x-coordinate: "))
                    y = int(input("Enter y-coordinate: "))
                    orientation = input("Enter orientation (h/v):")
                    if not (0 <= x < len(pl_board)) or not (0 <= y < len(pl_board[0])):
                        raise ValueError("Coordinates out of range. Please enter valid coordinates.")
                    else:
                        try_place_ship(pl_board, ship, size, x, y, orientation)
                        placement_data[ship] = placement_data.get(ship, []) + [(x, y, orientation)]
                        update_placement_file(placement_data) # updates the placement.json file
                    
                except ValueError as e:
                    print(f"Error: {e}")
    else:
        pass

    players[user_name] = {'board': pl_board, 'battleships': pl_ships}
    players["AI Opponent"] = {'board': ai_board, 'battleships': ai_ships}
    
    while any(size > 0 for size in pl_ships.values()) and any(size > 0 for size in ai_ships.values()): # runs game until all ships of either the player or ai is sunk
        print(f"{user_name}'s board:'")
        print_board(pl_board)
        print("\nYour Turn:")
        pl_coordinates = cli_coordinates_input(ai_board)
        attack(pl_coordinates, ai_board, ai_ships)
        
        print("\nAI is making a move")
        ai_coordinates = generate_attack(pl_board)
        attack(ai_coordinates, pl_board, pl_ships)
        
        if all(size == 0 for size in pl_ships.values()): # prints the message if player's ships have all been sunk
            print("Game Over! AI Opponent has sunk all your battleships.")
            break
        elif all(size == 0 for size in ai_ships.values()): # prints the message if AI's ships have all been sunk
            print("Game Over! You have sunk all AI opponent's battleships.")
            break
    

if __name__ == "__main__":
    ai_opponent_game_loop()
    
    
    