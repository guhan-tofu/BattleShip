# BattleShip

## Introduction
This project is an application of the classic Battleship game. It allows a player to place their battleships on a grid and take turns attacking the AI opponent's grid to sink their ships until one of the players have sunk all the ships.



## Prerequisites

- Python 3.7 or higher

## Installation
Flask is an external python library and so needs to be installed using pip

`pip install -U Flask`

## Getting started
To play the Battleship game, follow these steps:
1) Type cd followed by a space in the command prompt window
2) Drag and drop the folder you want to browse into the window and press Enter

Windows:

   `cd C:\Users\user\Downloads\battleship`
   
MacOS:

   `cd /Users/username/Downloads/battleship`

3) Run the main application:

   `flask --app main run`
4) Open your web browser and navigate to http://localhost:5000/placement
5) Follow the on-screen instructions to place your battleships and start the game.

## Testing
All test is present in a tests folder where each file contains the keyword "test". 

Pytest is an external python library and so needs to be installed using pip

`pip install pytest`

You will also need to install these plugins

`pip install pytest-depends`

`pip install pytest-cov`

To run the tests, use the following command in terminal:

Windows:

`python -m pytest` 

MacOS:

`pytest`

## Details

* **Authors:** Sri Guhan
* **License:** This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
* **Source:** [GitHub Repository](https://github.com/guhan-tofu/BattleShip)
