# Quoridor
Final project for software carpentry: quoridor game.
A Software Carpentry class solo final project that allows a user to virtually play the "Quoridor" game.
Quoridor is a 2 or 4-player intuitive strategy game designed by Mirko Marchesi and published by Gigamic Games.

## Table of Contents
- [Quoridor](#quoridor)
  - [Table of Contents](#table-of-contents)
  - [Project Proposal](#project-proposal)
  - [Introduction](#introduction)
  - [Technologies](#technologies)
    - [Libraries](#libraries)
  - [Launch](#launch)
  - [Features](#features)
  - [Status](#status)
    - [Future work:](#future-work)
  - [Credit](#credit)

## Project Proposal
I would like to propose coding the game Quoridor for my final project as a solo project. I expect the game to be able to be played in a 2- player format with either two in-person players determining moves or with a basic bot. The bot will determine the shortest path to the other side of the board for each player and move its pawn in that direction if they posses the shortest path to finish; otherwise, they will block the player with the shortest path with a wall. The game will be played using a basic GUI.
 
Quoridor Description (from Wikipedia with minor edits for brevity):
Quoridor is a 2 or 4-player intuitive strategy game designed by Mirko Marchesi and published by Gigamic Games.
 
Rules of the Game:
Quoridor is played on a 9x9 game board. Each player has a pawn which begins at the center space of one edge of the board opposite of their opponent. The objective is to be the first player to move their pawn to any space on the opposite side of the game board from which it begins. They can move their pawn in any direction to achieve this goal.
 
Each player has twenty walls to place. Walls are flat two-space-wide pieces which can be placed in the groove that runs between the spaces. Walls block the path of all pawns, which must go around them. The walls are divided equally among the players at the start of the game, and once placed, cannot be moved or removed. On a turn, a player may either move their pawn, or, if possible, place a wall.
 
Pawns can be moved to any space at a right angle (but not diagonally). If adjacent to another pawn, the pawn may jump over that pawn. If that square is not accessible (e.g., off the edge of the board or blocked by a third pawn or a wall), the player may move to either space that is immediately adjacent (left or right) to the first pawn (effectively diagonally). Multiple pawns may not be jumped. Walls may not be jumped, including when moving laterally due to a pawn or wall being behind a jumped pawn.
 
Walls can be placed directly between two spaces, in any groove not already occupied by a wall. However, a wall may not be placed which cuts off the only remaining path of any pawn to the side of the board it must reach.
 
Final project features:
1.	Pawns as classes
2.	Walls as classes
3.	Logic preventing impossible moves with placing walls (overlapping another wall or making all paths impossible)
4.	Logic for edge cases with moving pawns (when next to another pawn or near an edge)
5.	GUI to play
6.	Basic bot with at least beginner-level strategy (described above)
7.	Game record tracker
1.	Win/loss record
2.	Fewest turns for a victorious game
3.	Most walls left in inventory for a victorious game
 
 
Optional features I hope to include:
8.	4- player support (includes more edge cases and rules for how pawns and walls must interact with each other)
9.	Remote play (both players don’t have to be at the same computer)
10.	Message-based plays for playing over test or some messaging service
11.	More complex bot strategy including reinforcement learning for the bot
12.	3D GUI


## Introduction
This project mimics the "Quoridor" game published by Gigamic games.
It allows the user to play a one-on-one game with another user or to play against a bot. 

The code visualizes the starting board and then allows the user to make moves using mouse clicks for the GUI. It updates visualization of the board as moves are made and the game progresses and eventually declares a winner once it has been determined.

## Technologies
Project is created with:
* Python 3.10

### Libraries
Project used the following libraries:
* pygame

## Launch
To run this project, open quoridor.py and run the code using Python 3.10.

Once the code is running, a window will pop up. First, 

## Features
Add features here

## Status
This release allows the for quoridor game to be played between two individuals or one individual and a basic bot. Once a winner has been determined, it allows the user to save the final board as a PNG image.

### Future work:
* Add functionality to do more stuff.

## Credit:
* Thank you to the Pygame Tutorial for Beginners - Python Game Development Course video from the freeCodeCamp.org YouTube channel for assistance in learning pygame: https://www.youtube.com/watch?v=FfWpgLFMI7w 
* Thank you to Andrejs Kirma for the pawn icon: <a href="https://www.flaticon.com/free-icons/pawn" title="pawn icons">Pawn icons created by Andrejs Kirma - Flaticon</a>
* Thank you to Good Ware for the board & pawn icon: <a href="https://www.flaticon.com/free-icons/chess-board" title="chess board icons">Chess board icons created by Good Ware - Flaticon</a>