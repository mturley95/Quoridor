# Quoridor
Final project for software carpentry: quoridor game.
A Software Carpentry class solo final project that allows a user to virtually play the "Quoridor" game.
Quoridor is a 2 or 4-player intuitive strategy game designed by Mirko Marchesi and published by Gigamic Games.

## Table of Contents
- [Quoridor](#quoridor)
  - [Table of Contents](#table-of-contents)
  - [Project Description](#project-description)
  - [Introduction](#introduction)
  - [Technologies](#technologies)
    - [Libraries](#libraries)
  - [Launch](#launch)
  - [Features](#features)
  - [Status](#status)
    - [Future work:](#future-work)
  - [Credit](#credit)

## Project Description
I coded the game Quoridor for my final project as a solo project. The game may be played in 2-, 3-, or 4- player formats with local humans acting as the players. The game is played using a GUI created using the pygame library.
 
Quoridor Description (from Wikipedia with edits for brevity): 
Quoridor is a 2 or 4-player intuitive strategy game designed by Mirko Marchesi and published by Gigamic Games.
 
Rules of the Game:
Quoridor is played on a 9x9 game board. Each player has a pawn which begins at the center space of one edge of the board opposite of their opponent. The objective is to be the first player to move their pawn to any space on the opposite side of the game board from which it begins. They can move their pawn in any direction to achieve this goal.
 
All players have a combined 20 or 21 walls to place. Walls are flat two-space-wide pieces which can be placed in the groove that runs between the spaces. Walls block the path of all pawns, which must go around them. The walls are divided equally among the players at the start of the game, and once placed, cannot be moved or removed. On a turn, a player may either move their pawn, or, if possible, place a wall.
 
Pawns can be moved to any space at a right angle (but not diagonally except in a rare exception). If adjacent to another pawn, the pawn may jump over that pawn. If that square is not accessible (e.g., off the edge of the board or blocked by a third pawn or a wall), the player may move to either space that is immediately adjacent (left or right) to the first pawn (effectively diagonally). Multiple pawns may not be jumped. Walls may not be jumped, including when moving laterally due to a pawn or wall being behind a jumped pawn.
 
Walls can be placed directly between two spaces, in any groove not already occupied by a wall. However, a wall may not be placed which cuts off the only remaining path of any pawn to the side of the board it must reach.

## Introduction
This project mimics the "Quoridor" game published by Gigamic games.
It allows the user to play a game with between 2 and 4 total users on a local machine. 

The code visualizes the starting board and allows the user to make setup the game and make moves using mouse clicks for GUI control for both pawn and wall movements. It updates visualization of the board as moves are made and the game progresses. It displays the winning player once they have made a winning move.

## Technologies
Project is created with:
* Python 3.10

### Libraries
Project used the following libraries:
* pygame

## Launch and How to Use
To run this project, open __main__.py and run the code using Python 3.10.

Once the code is running, a window will pop up. First, select the number of users playing the game. Then, click start when ready to begin.

The active player will display in the info box in the top-left corner of the display. In order to make a move, first select either the active player's pawn on the game board or the wall button on the right of the screen.

If the active player's pawn is selected, the possible movement spaces will be displayed. Select one of the possible moves to make a move with the pawn.

If the wall button is selected, it will appear blue. Place a wall in an open wall space by clicking on that space while the wall button is selected.

The player may restart the game and go back to the setup screen at any time.

The player may select the quit button to exit the game window at any time.

## Features
Final project features:
1.  Use of object-oriented programming techniques including players, walls, and other class-based objects.
2.  Player movement functionality allowing pawn movement onto possible spaces.
3.  Wall placement functionality allowing walls to be placed onto possible spaces.
4.	Logic preventing placing walls in conflicting spaces (overlapping or crossing another wall).
5.	Logic for edge cases with moving pawns (when next to another pawn, near an edge, moving into a wall, or skipping into a wall).
6.	GUI to play for both game setup and game play.
7.  Display of the current player's turn.
8.  Display of each player's finish line.
9.  Imported pawn art.
10.  Live tracking and display of walls remaining including an info message when no walls are left.
11.  Display of possible move options for a player when their piece is selected.
12.  4- player support (includes more edge cases and rules for how pawns and walls must interact with each other).
13.  Display of winning player info on the GUI when winning move is made.

## Status
This release allows the for Quoridor game to be played between two to four individuals. Once a winner has been determined, it allows the user to restart the game if they want to play another game.

### Future work:
1.  Pathfinder functionality to not allow a wall to be placed that blocks a pawn from reaching their finish line.
2.  A basic bot to play against.
3.  The ability to image the game board once a player has won.
4.  A "back" button to undo the last move.
5.  User input for player names.
6.  Game record tracker: win/loss record for each player.
7.  Game record tracker: fewest turns for victorious game.
8.  Game record tracker: most walls left in inventory for victorious game.
9.  Remote play for users to play each other online using a server.
10.  Message-based plays for a player to play moves over text.
11. More complex bot strategy and difficulty levels.
12. 3D GUI.

## Credit:
* Thank you to the Pygame Tutorial for Beginners - Python Game Development Course video from the freeCodeCamp.org YouTube channel for assistance in learning pygame: https://www.youtube.com/watch?v=FfWpgLFMI7w 
* Thank you to Tech With Tim and his Python/Pygame Checkers Tutorial video series for assistance in learning pygame: https://www.youtube.com/watch?v=vnd3RfeG3NM&t=1104s 
* Thank you to Andrejs Kirma for the pawn icon: <a href="https://www.flaticon.com/free-icons/pawn" title="pawn icons">Pawn icons created by Andrejs Kirma - Flaticon</a>
* Thank you to Good Ware for the board & pawn icon: <a href="https://www.flaticon.com/free-icons/chess-board" title="chess board icons">Chess board icons created by Good Ware - Flaticon</a>