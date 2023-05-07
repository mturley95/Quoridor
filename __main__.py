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
# from pathfinder import *

# Change directory location for self-made modules.
sys.path.append('src/')

# Controls window class object.
from window import *

# Various constants such as colors and window sizes.
from const import *

# Control over the buttons on the sidebar on the right of the screen.
from sidebar import *

# Controls walls.
from wall import Walls

# Controls game mechanics.
from game import Game


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
    walls = Walls()
    game = Game(win)

    # Main game loop
    running = True
    while running == True:
        # Set the game clock to tick/refresh at the frames per second set
        # in the constants file.
        clock.tick(FPS)

        # Check to see if either player has won the game before continuing.
        '''Consider if this should be here or if the game should stop
        if the player has won at the end.'''
        if game.winner != None:
            print(game.winner)
            run = False

        pos = pygame.mouse.get_pos()
        
        # Handle events as the user interacts with the window.
        for event in pygame.event.get():

            # Check to see if the user closed the window.
            if event.type == pygame.QUIT:
                # Stop the program running.
                running = False

            # Identify if the user clicks the mouse.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position at the time of the mouse click.
                pos = pygame.mouse.get_pos()

                # Check to see if they clicked on the "Quit" button.
                if win.button_quit.click(pos):
                    # Stop the program running.
                    running = False

                # Check to see if they clicked the "Restart" button.
                elif win.button_restart.show == True and \
                    win.button_restart.click(pos):
                    
                    # Perform the restart button actions.
                    click_restart(win)

                # Check to see if the user clicked the button determining the
                # number of players that will play and perform associated tasks.
                elif win.button_2_players.show == True and \
                    win.button_2_players.click(pos):

                    players = click_button_2_players(win, coords)

                elif win.button_3_players.show == True and \
                    win.button_3_players.click(pos):

                    players = click_button_3_players(win, coords)

                elif win.button_4_players.show == True and \
                    win.button_4_players.click(pos):

                    players = click_button_4_players(win, coords)

                # Check to see if the user clicked the button determining whether
                # a players will be a human or bot.
                elif win.button_hb_player_1.show == True and \
                    win.button_hb_player_1.click(pos):

                    click_button_hb_player_1(win)

                elif win.button_hb_player_2.show == True and \
                    win.button_hb_player_2.click(pos):

                    click_button_hb_player_2(win)

                elif win.button_hb_player_3.show == True and \
                    win.button_hb_player_3.click(pos):

                    click_button_hb_player_3(win)

                elif win.button_hb_player_4.show == True and \
                    win.button_hb_player_4.click(pos):

                    click_button_hb_player_4(win)

                # Check to see if they clicked the "Start" button and perform associated tasks.
                elif win.button_start.show == True and \
                    win.button_start.click(pos):
                    
                    click_button_start(win)

                # Check to see if they selected a wall.
                elif win.button_wall.show == True and \
                    player.can_play_wall(game) and \
                    win.button_wall.click(pos):
                    
                    click_button_wall(win)
                    
                # Check to see if they attempted to play a wall.
                elif win.button_wall.selected == True:
                    
                    # wall_select = player.play_put_wall(pos, coords, walls, n, pf, players)
                    wall_select = player.play_put_wall(pos, coords, walls, n, players)

                    if wall_select != '':
                        win.update_info(wall_select)
                    else:
                        win.button_wall.set_selected(False)

                # Check to see if they selected their piece and show possible moves.
                elif player.can_play == True and \
                    win.player.coord.click(pos):
                    
                    player.piece_selected(True)

                elif player.selected == True:

                    played_move = False
                    for pos_coord in player.pos_coord:
                        if win.pos_coord.click(pos):
                            player.play_move(pos_coord)
                            played_move = True
                    
                    if played_move == False:
                        player.piece.selected(False)

        # Update the display with any new actions or events.
        win.redraw_window(game, players, walls, pos)

    # Quit Pygame if the loop is broken.
    pygame.quit()

    # Print a parting message in the terminal.
    print("Good bye!")


# Run the main code.
if __name__ == "__main__":
    # Run the play_game() function to initiate the game.
    play_game()