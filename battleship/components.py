

import random
import json
def try_place_ship(board, ship, size, x, y, orientation):
        """A function which takes coordinates and tries to place given ship in given coordinate in given board"""
        try:
            if orientation.lower().startswith('h') and x + size <= len(board[0]): 
                for i in range(size):
                    if board[y][x + i] is not None:
                        print("Position already taken, try another position")
                        return False
                for i in range(size):
                    board[y][x + i] = ship
                return True
            elif orientation.lower().startswith('v') and y + size <= len(board):
                for i in range(size):
                    if board[y + i][x] is not None:
                        print("Position already taken, try another position")
                        return False
                for i in range(size):
                    board[y + i][x] = ship
                return True
            return False
        except IndexError as e:
            raise IndexError(f"Error placing battleship {ship}: {e}")

def initialise_board(size=10):
    """Creates a board of default size 10x10 with None values"""
    print("    0     1     2     3     4     5     6     7     8     9")
    board=[]
    for i in range(size):
      board.append([None]*size)
    return board

def create_battleships(filename="battleships.txt"):
    with open(filename, 'r') as file:
        content = file.read()
    ship_sizes = {}
    lines = content.strip().split('\n')
    for line in lines:
        ship, size = line.split(':')
        ship_sizes[ship.strip()] = int(size.strip())
    return ship_sizes

def place_battleships(board, ships, algorithm='simple',placement_file="placement.json"):
    """A function which places ships in one of the three algorithms"""
    def place_battleship_simple(board, ship, size):
        """places ship in simple algorithm"""
        try:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if j + size <= len(board[0]) and all(board[i][j + k] is None for k in range(size)):
                        for k in range(size):
                            board[i][j + k] = ship
                        return
        except IndexError as e:
            raise IndexError(f"Error placing battleship {ship}: {e}")

    def place_battleship_random(board, ship, size):
        """places ship in random algorithm"""
        try:
            placed = False
            while not placed:
                x = random.randint(0, len(board) - 1)
                y = random.randint(0, len(board[0]) - 1)
                orientation = random.choice(['horizontal', 'vertical'])
                if try_place_ship(board, ship, size, x, y, orientation): # To ensure that x and y coordinates do not overlap
                    placed = True
        except IndexError as e:
            raise IndexError(f"Error placing battleship {ship}: {e}")
            



    def place_battleship_custom(board, ship, size, placement_file="placement.json"):
        """places ship in custom algorithm"""
        try:
            with open(placement_file, 'r') as file:
                placement_data = json.load(file)

            for ship, info in placement_data.items(): # gives ship and positions seperately
                x, y, orientation = info # gives x,y and orientation from the positions list
                try_place_ship(board, ship, size, int(x), int(y), orientation)# To ensure that x and y coordinates do not overlap
                
        except FileNotFoundError:
            print(f"Custom placement file '{placement_file}' not found. Using default placement.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in '{placement_file}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred:{e}") 

            
            


    if algorithm == 'simple':
        for ship,size in ships.items():
            place_battleship_simple(board, ship, size)
    elif algorithm == 'random':
        for ship,size in ships.items():
            place_battleship_random(board, ship, size)
    elif algorithm == 'custom':
        for ship,size in ships.items():
            place_battleship_custom(board, ship, size)
       
    return board

