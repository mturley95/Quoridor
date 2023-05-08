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

# from src.pathfinder import *


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

    # Initialize the game with 0 players selected initially.
    # Open the window and display the playing board.
    player_count = 0
    win = Window()
    coords = win.coords
    players = Players(player_count, coords, win)
    current_p = None
    walls = Walls()
    game = Game(players.player_count)

    # While the window is open:
    win_open = True
    while win_open == True:

        # Start the setup game loop first.
        setup = True
        running = False
        end = False
        game.running = running

        while setup == True:
            # Set the game clock to tick/refresh at the frames per second set
            # in the constants file.
            clock.tick(FPS)

            # Get the position of the mouse in order to shade the spaces that is is over.
            pos = pygame.mouse.get_pos()
            
            # Handle events as the user interacts with the window.
            for event in pygame.event.get():

                # Check to see if the user closed the window.
                if event.type == pygame.QUIT:
                    # If so, stop the program running and close the window.
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
                        # If so, stop the program running and close the window.
                        setup = False
                        running = False
                        end = False
                        win_open = False

                    # Check to see if the user clicked the button determining the
                    # number of players that will play and perform associated tasks.
                    elif win.button_2_players.show == True and \
                        win.button_2_players.click(pos) == True:                        
                        # Identify the 2-player button as clicked and 
                        # return the corresponding players.
                        players = click_button_2_players(win, coords)

                    elif win.button_3_players.show == True and \
                        win.button_3_players.click(pos) == True:
                        # Identify the 3-player button as clicked and 
                        # return the corresponding players.
                        players = click_button_3_players(win, coords)

                    elif win.button_4_players.show == True and \
                        win.button_4_players.click(pos) == True:
                        # Identify the 4-player button as clicked and 
                        # return the corresponding players.
                        players = click_button_4_players(win, coords)

                    # Check to see if the user clicked the button determining whether
                    # a players will be a human or bot.
                    elif win.button_hb_player_1.show == True and \
                        win.button_hb_player_1.click(pos) == True:
                        # Alternate from human to bot and back as the button is clicked.
                        click_button_hb_player_1(win)

                    elif win.button_hb_player_2.show == True and \
                        win.button_hb_player_2.click(pos) == True:
                        # Alternate from human to bot and back as the button is clicked.
                        click_button_hb_player_2(win)

                    elif win.button_hb_player_3.show == True and \
                        win.button_hb_player_3.click(pos) == True:
                        # Alternate from human to bot and back as the button is clicked.
                        click_button_hb_player_3(win)

                    elif win.button_hb_player_4.show == True and \
                        win.button_hb_player_4.click(pos) == True:
                        # Alternate from human to bot and back as the button is clicked.
                        click_button_hb_player_4(win)

                    # Check to see if they clicked the "Start" button and perform associated tasks.
                    elif win.button_start.show == True and \
                        players.player_count > 0 and \
                        win.button_start.click(pos) == True:
                        # Record the number of players and types (human or bot) when the game is started.
                        player_types = click_button_start(win)
                        game.set_player_count(players.player_count)
                        # Start the game.
                        game.start()
                        # Set active players' names.
                        players.set_default_names()
                        # Move from the setup loop to the game-running loop.
                        running = game.running
                        setup = False

            # Update the display with any new actions or events.
            win.redraw_window(game, current_p, players, walls, pos)


        # Main game loop
        while running == True:
            # Set the game clock to tick/refresh at the frames per second set
            # in the constants file.
            clock.tick(FPS)

            # Set the current player to handle their different inputs.
            current_p = players.players[game.current_player]

            # Get the position of the mouse in order to shade the spaces that is is over.
            pos = pygame.mouse.get_pos()
            
            # Handle events as the user interacts with the window.
            for event in pygame.event.get():

                # Check to see if the user closed the window.
                if event.type == pygame.QUIT:
                    # Stop the program running and close the window.
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
                        # Stop the program running and close the window.
                        setup = False
                        running = False
                        end = False
                        win_open = False

                    # Check to see if they clicked the "Restart" button.
                    elif win.button_restart.show == True and \
                        win.button_restart.click(pos) == True:
                        
                        # Perform the restart button actions and 
                        # record the updated status of the setup window (active),
                        # running game window (inactive), and end window (inactive), 
                        # and reset the players.
                        setup, running, end, players = \
                            click_restart(win, coords, players, walls)

                    # Check to see if they selected to play wall using the wall button.
                    elif win.button_wall.show == True and \
                        current_p.can_play_wall(game) == True and \
                        win.button_wall.click(pos) == True:
                        
                        # Select the wall button to prepare to play a wall.
                        click_button_wall(win)
                        # Deselect the current player's pawn if it was previously selected.
                        current_p.set_selected(False, win, walls, players)

                    # Check to see if they selected to play a wall but are out of walls.
                    elif win.button_wall.show == True and \
                        current_p.can_play_wall(game) != True and \
                        win.button_wall.click(pos) == True:
                        
                        # Update the info tab to state that that player is out of walls.
                        # Do not select the walls button.
                        win.update_info(f"Player {current_p.get_num_player() + 1}'s out of walls!", \
                                        current_p.color)
                        
                    # Check to see if they selected their piece and show possible moves.
                    elif players.player_count > 0 and \
                        current_p.can_play(game) == True and \
                        current_p.click(pos) == True:
                        
                        # Set their piece to be selected and perform associated actions.
                        current_p.set_selected(True, win, walls, players)
                        
                        # Deselect the wall button if it was selected.
                        if win.button_wall.selected == True:
                            click_button_wall(win)
                        
                    # Check to see if the active player attempted to play a wall.
                    elif win.button_wall.selected == True:
                        
                        # If possible, play a wall.
                        # wall_select = player.play_put_wall(pos, coords, walls, n, pf, players)
                        wall_select = current_p.play_put_wall(pos, coords, walls, players)
                        
                        # If the player successfully selected a wall space:
                        if wall_select != None:
                            # Display either that the player played a wall or 
                            # that they made an invalid play.
                            win.update_info(wall_select, current_p.color)
                            # If the player successfully played a wall.
                            if wall_select != "You can't block players!":
                                # Deselect the wall button.
                                click_button_wall(win)
                                # Make the play and advance to the next player.
                                running, end = game.play(players)
                    
                    # If the player's pawn was previously selected and is selected again:
                    elif players.player_count > 0 and \
                        current_p.selected == True and \
                        current_p.click(pos):
                        # Deselect the player's piece.
                        current_p.set_selected(False, win, walls, players)

                    # If the player's paw is selected.
                    elif players.player_count > 0 and \
                        current_p.selected == True:
                        # Check whether a possible move was selected by the mouse
                        # for all possible moves.
                        for pos_coord in current_p.pos_moves(current_p.coord, walls, players):
                            if pos_coord.click(pos):
                                # Play the move that was selected.
                                current_p.play_move(pos_coord)
                                # Deselect that player's pawn.
                                current_p.set_selected(False, win, walls, players)
                                # Complete the play and advance to the next player.
                                running, end = game.play(players)
                                # Check whether the move was a winning move.
                                if end == True:
                                    # Display the name of the winner on the window.
                                    win.update_info(f"{current_p.name} wins!!! :)", current_p.color)
                                    # Stop displaying the wall button.
                                    win.button_wall.set_show(False)
                                
            # Update the display with any new actions or events.
            win.redraw_window(game, current_p, players, walls, pos)

        # End game loop
        while end == True:
            # Set the game clock to tick/refresh at the frames per second set
            # in the constants file.
            clock.tick(FPS)
            
            # Get the position of the mouse in order to shade the spaces that is is over.
            pos = pygame.mouse.get_pos()
            
            # Handle events as the user interacts with the window.
            for event in pygame.event.get():

                # Check to see if the user closed the window.
                if event.type == pygame.QUIT:
                    # Stop the program running and close the window.
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
                        # Stop the program running and close the window.
                        setup = False
                        running = False
                        end = False
                        win_open = False

                    # Check to see if they clicked the "Restart" button.
                    elif win.button_restart.show == True and \
                        win.button_restart.click(pos) == True:
                        
                        # Perform the restart button actions and 
                        # record the updated status of the setup window (active),
                        # running game window (inactive), and end window (inactive), 
                        # and reset the players.
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