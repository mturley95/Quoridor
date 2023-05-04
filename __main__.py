'''
Quoridor
Mitch Turley

This project will allow the user to virtually play the Quoridor game published by Gigamic games.
The user may play against another user one-on-one or against a simple bot.
This is the main codeblock to be run when the user desires to play.
'''

import os
import sys
import pygame

sys.path.append('src/')

from window import *
from const import *
from game import Game
from wall import Wall
from pathfinder import PathFinder


def play_game():
    '''Start the quoridor game.'''
    print("Welcome to Quoridor!")

    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Initialize the game.
    win = Window()
    coords = win.coords
    players = Players(player_count, coords)
    player = players.players[num_player]
    walls = Walls()
    pf = PathFinder()

    # Main game loop
    running = True
    while running == True:
        clock.tick(FPS)

        # Check to see if either player has won the game.
        if game.winner() != None:
            print(game.winner())
            run = False
        
        # Handle events
        for event in pygame.event.get():

            # Check to see if the user closed the window.
            if event.type == pygame.QUIT:
                running = False

            # Check to see what the user clicked on.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Check to see if they clicked the "Quit" button.
                if win.button_quit.click(pos):
                    running = False

                # Check to see if they clicked the "Restart" button.
                elif win.button_restart.click(pos):
                    coords.reset()
                    players.reset(coords)
                    walls.reset()

                # Check to see if they selected a wall.
                elif win.button_wall.click(pos) and player.can_play_wall(game):
                    pass

                # Check to see if they selected their piece
                elif win.button_piece.click(pos):
                    pass


        # Update the display
        win.redraw_window(game, players, walls, pos)

    # Quit Pygame
    pygame.quit()

    print("Good bye!")


if __name__ == "__main__":
    pygame.init()
    win = Window()
    
    # Game Loop
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    # play_game()