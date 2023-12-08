from flask import Flask, render_template, request, jsonify
from components import (
    initialise_board,
    create_battleships,
    place_battleships,try_place_ship)
from game_engine import attack
from mp_game_engine import generate_attack
app = Flask(__name__)
points=[]
pl_board = initialise_board()
ai_board = initialise_board()
pl_ships = create_battleships()
ai_ships = create_battleships()
place_battleships(ai_board, ai_ships, algorithm='random')


@app.route("/placement", methods=["GET", "POST"])
def placement_interface():
    global pl_board
    if request.method == 'POST':
        data = request.get_json()
        print("Received JSON data:", data)
        for ship, placement in data.items():
            x, y, orientation = placement  # No need to convert orientation to int
            x, y = int(x), int(y)  # Convert only x and y to integers
            try_place_ship(pl_board, ship, pl_ships[ship], x, y, orientation)
        return jsonify({'message': 'Received'}), 200
    else:
        return render_template('placement.html', ships=pl_ships, board_size=len(pl_board))

@app.route("/", methods=["GET"])
def root():
    global pl_board
    return render_template("main.html", player_board=pl_board)

@app.route("/attack", methods=["GET"])
def process_attack():
    global pl_board, ai_board,points
    # Retrieve attack coordinates from request arguments
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    coordinates = (x,y)
    hit = attack(coordinates,ai_board,ai_ships)
    ai_turn = generate_attack(pl_board)
    attack(ai_turn,pl_board,pl_ships)

    print(ai_board)
    print(pl_ships)
    print(ai_ships)
    
    if not any(ship for row in ai_board for ship in row):
        # Game is finished
        return jsonify({'hit': hit, 'AI_Turn': ai_turn, 'finished': 'Game Over! Player wins'}), 200
    elif not any(ship for row in pl_board for ship in row):
        # AI wins
        return jsonify({'hit': hit, 'AI_Turn': ai_turn, 'finished': 'Game Over! AI wins'}), 200
    else:
        # Game is not finished
        return jsonify({'hit': hit, 'AI_Turn': ai_turn}), 200

if __name__ == '__main__':
    app.run(debug=True)