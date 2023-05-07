'''
Quoridor
Mitch Turley

This project will allow the user to virtually play the Quoridor game published by Gigamic games.
The user may play against another user one-on-one or against a simple bot.
This is the main codeblock to be run when the user desires to play.
'''

# Import necessary libraries.
import os
import sys
import pygame

# Controls window class object.
from src.window import *

# Various constants such as colors and window sizes.
from src.const import *

# Control over the buttons on the sidebar on the right of the screen.
from src.sidebar import *

# Controls walls.
from src.wall import Walls

# Controls game mechanics.
from src.game import Game

# Controls the board coordinates
from src.board import Coord

# from pathfinder import *


# Start the quoridor game.
def play_game():
    '''
    Start the quoridor game.
    
    Add better description of function.
    '''

    # Print welcome message in the terminal.
    print("Welcome to Quoridor!")

    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Initialize the game.
    # Open the window and display the playing board.
    player_count = 0
    win = Window()
    coords = win.coords
    players = Players(player_count, coords, win)
    current_p = None
    walls = Walls()
    game = Game(players.player_count)

    win_open = True
    while win_open == True:
        # Setup game loop
        setup = True
        running = False
        end = False
        game.running = running

        while setup == True:
            # Set the game clock to tick/refresh at the frames per second set
            # in the constants file.
            clock.tick(FPS)

            # # Check to see if either player has won the game before continuing.
            # # Consider if this should be here or if the game should stop
            # # if the player has won at the end.
            # if game.winner != None:
            #     print(game.winner)
            #     running = False

            pos = pygame.mouse.get_pos()
            
            # Handle events as the user interacts with the window.
            for event in pygame.event.get():

                # Check to see if the user closed the window.
                if event.type == pygame.QUIT:
                    # Stop the program running.
                    setup = False
                    running = False
                    end = False
                    win_open = False

                # Identify if the user clicks the mouse.
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position at the time of the mouse click.
                    pos = pygame.mouse.get_pos()

                    # Check to see if they clicked on the "Quit" button.
                    if win.button_quit.click(pos):
                        # Stop the program running.
                        setup = False
                        running = False
                        end = False
                        win_open = False

                    # Check to see if the user clicked the button determining the
                    # number of players that will play and perform associated tasks.
                    elif win.button_2_players.show == True and \
                        win.button_2_players.click(pos) == True:

                        players = click_button_2_players(win, coords)

                    elif win.button_3_players.show == True and \
                        win.button_3_players.click(pos) == True:

                        players = click_button_3_players(win, coords)

                    elif win.button_4_players.show == True and \
                        win.button_4_players.click(pos) == True:

                        players = click_button_4_players(win, coords)

                    # Check to see if the user clicked the button determining whether
                    # a players will be a human or bot.
                    elif win.button_hb_player_1.show == True and \
                        win.button_hb_player_1.click(pos) == True:

                        click_button_hb_player_1(win)

                    elif win.button_hb_player_2.show == True and \
                        win.button_hb_player_2.click(pos) == True:

                        click_button_hb_player_2(win)

                    elif win.button_hb_player_3.show == True and \
                        win.button_hb_player_3.click(pos) == True:

                        click_button_hb_player_3(win)

                    elif win.button_hb_player_4.show == True and \
                        win.button_hb_player_4.click(pos) == True:

                        click_button_hb_player_4(win)

                    # Check to see if they clicked the "Start" button and perform associated tasks.
                    elif win.button_start.show == True and \
                        players.player_count > 0 and \
                        win.button_start.click(pos) == True:
                        
                        player_types = click_button_start(win)
                        game.set_player_count(players.player_count)
                        game.start()
                        players.set_names()
                        running = game.running
                        setup = False

            # Update the display with any new actions or events.
            win.redraw_window(game, current_p, players, walls, pos)


        # Main game loop
        while running == True:
            # Set the game clock to tick/refresh at the frames per second set
            # in the constants file.
            clock.tick(FPS)

            # Start a game and record player plays
            current_p = players.players[game.current_player]

            pos = pygame.mouse.get_pos()
            
            # Handle events as the user interacts with the window.
            for event in pygame.event.get():

                # Check to see if the user closed the window.
                if event.type == pygame.QUIT:
                    # Stop the program running.
                    setup = False
                    running = False
                    end = False
                    win_open = False

                # Identify if the user clicks the mouse.
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position at the time of the mouse click.
                    pos = pygame.mouse.get_pos()

                    # Check to see if they clicked on the "Quit" button.
                    if win.button_quit.click(pos) == True:
                        # Stop the program running.
                        setup = False
                        running = False
                        end = False
                        win_open = False

                    # Check to see if they clicked the "Restart" button.
                    elif win.button_restart.show == True and \
                        win.button_restart.click(pos) == True:
                        
                        # Perform the restart button actions.
                        setup, running, end, players = \
                            click_restart(win, coords, players, walls)

                    # Check to see if they selected to play wall.
                    elif win.button_wall.show == True and \
                        current_p.can_play_wall(game) == True and \
                        win.button_wall.click(pos) == True:
                        
                        click_button_wall(win)
                        current_p.set_selected(False, win, walls, players)

                    # Check to see if they selected to play a wall but are out of walls.
                    elif win.button_wall.show == True and \
                        current_p.can_play_wall(game) != True and \
                        win.button_wall.click(pos) == True:
                        
                        win.update_info(f"Player {current_p.num_player+1}'s out of walls!", \
                                        current_p.color)
                        
                    # Check to see if they selected their piece and show possible moves.
                    elif players.player_count > 0 and \
                        current_p.can_play(game) == True and \
                        current_p.click(pos) == True:
                        
                        current_p.set_selected(True, win, walls, players)
                        
                        if win.button_wall.selected == True:
                            click_button_wall(win)
                        
                    # Check to see if they attempted to play a wall.
                    elif win.button_wall.selected == True:
                        
                        # wall_select = player.play_put_wall(pos, coords, walls, n, pf, players)
                        wall_select = current_p.play_put_wall(pos, coords, walls, players)

                        if wall_select != None:
                            win.update_info(wall_select, current_p.color)
                            if wall_select != "You can't block players!":
                                click_button_wall(win)
                                running, end = game.play(players)

                    elif players.player_count > 0 and \
                        current_p.selected == True and \
                        current_p.click(pos):

                        current_p.set_selected(False, win, walls, players)

                    elif players.player_count > 0 and \
                        current_p.selected == True:

                        for pos_coord in current_p.pos_moves(current_p.coord, walls, players):
                            if pos_coord.click(pos):
                                current_p.play_move(pos_coord)
                                current_p.set_selected(False, win, walls, players)
                                running, end = game.play(players)
                                if end == True:
                                    win.update_info(f"{current_p.name} wins!!! :)", current_p.color)
                                    win.button_wall.set_show(False)
                                
            # Update the display with any new actions or events.
            win.redraw_window(game, current_p, players, walls, pos)

        # End game loop
        while end == True:
            # Set the game clock to tick/refresh at the frames per second set
            # in the constants file.
            clock.tick(FPS)

            pos = pygame.mouse.get_pos()
            
            # Handle events as the user interacts with the window.
            for event in pygame.event.get():

                # Check to see if the user closed the window.
                if event.type == pygame.QUIT:
                    # Stop the program running.
                    setup = False
                    running = False
                    end = False
                    win_open = False

                # Identify if the user clicks the mouse.
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position at the time of the mouse click.
                    pos = pygame.mouse.get_pos()

                    # Check to see if they clicked on the "Quit" button.
                    if win.button_quit.click(pos) == True:
                        # Stop the program running.
                        setup = False
                        running = False
                        end = False
                        win_open = False

                    # Check to see if they clicked the "Restart" button.
                    elif win.button_restart.show == True and \
                        win.button_restart.click(pos) == True:
                        
                        # Perform the restart button actions.
                        setup, running, end, players = \
                            click_restart(win, coords, players, walls)
                                
            # Update the display with any new actions or events.
            win.redraw_window(game, current_p, players, walls, pos)


    # Quit Pygame if the loop is broken.
    pygame.quit()

    # Print a parting message in the terminal.
    print("Good bye!")


# Run the main code.
if __name__ == "__main__":
    # Run the play_game() function to initiate the game.
    play_game()