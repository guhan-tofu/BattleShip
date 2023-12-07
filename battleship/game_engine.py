from components import initialise_board, create_battleships, place_battleships


def attack(coordinates, board, battleships):
    """if given coordinates are there on board then it updates the board and battleships """
    x, y = coordinates

    if board[y][x] is not None:
        battleship_name = board[y][x]
        print("Hit!")
        hit = True
        board[y][x] = None
        battleships[battleship_name] -= 1
        if battleships[battleship_name] == 0:
            print(f"You've sunk the {battleship_name}!")
        else:
            pass
    else:
        hit=False
        print("Miss.")
    return hit

def cli_coordinates_input(board):
    """returns coordinates given by player"""
    ch="y"
    while ch=="y":
        try:
            x=int(input("Enter X coordinate:"))
            y=int(input("Enter Y coordinate:"))
            if not (0 <= x < len(board)) or not (0 <= y < len(board[0])): # ensures given coordinates are within the range of board
                raise ValueError("Coordinates out of range. Please enter valid coordinates.")
            else:
                ch=="n"
                coordinates=(x,y)
                return coordinates
        except ValueError:
            print("Invalid input. Please enter valid numerical coordinates.")

def simple_game_loop():
    """A simple version of battleship game where there is only one player and one board"""
    print("Welcome to the Battleships game!")
    board = initialise_board()
    battleships = create_battleships(filename="battleships.txt")
    place_battleships(board, battleships)

    while any(size > 0 for size in battleships.values()): # when all of the ships have size=0, it breaks the loop and ends game
        print_board(board)
        print("Your turn:")
        coordinates = cli_coordinates_input(board)
        attack(coordinates, board, battleships)

    print_board(board)
    print("Game over. You've sunk all battleships!")

def print_board(board):
    """prints the board in ascii format"""
    for row in board:
        print(" ".join(cell if cell is not None else "-" for cell in row))

if __name__ == "__main__":
    simple_game_loop()