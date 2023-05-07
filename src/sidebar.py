import pygame
from window import *
from player import Players
from game import Game
from wall import Walls

def click_restart(win):
    '''
    When the restart button is clicked,
    perform the following actions:
    
    Add more info about this function's parameters here.
    '''

    # Show the user the buttons asking them to select the number of players.
    win.how_many_players.set_show(True)
    win.button_2_players.set_show(True)
    win.button_3_players.set_show(True)
    win.button_4_players.set_show(True)

    # Do not show the remainder of the buttons until the user picks the number of players.
    win.button_2_players.set_selected(False)
    win.button_3_players.set_selected(False)
    win.button_4_players.set_selected(False)
    win.human_or_bot.set_show(False)
    win.player_1_t.set_show(False)
    win.player_2_t.set_show(False)
    win.player_3_t.set_show(False)
    win.player_4_t.set_show(False)
    win.button_hb_player_1.set_show(False)
    win.button_hb_player_2.set_show(False)
    win.button_hb_player_3.set_show(False)
    win.button_hb_player_4.set_show(False)
    win.button_hb_player_1.set_selected(False)
    win.button_hb_player_2.set_selected(False)
    win.button_hb_player_3.set_selected(False)
    win.button_hb_player_4.set_selected(False)
    win.button_wall.set_show(False)
    win.button_start.set_show(False)
    win.button_restart.set_show(False)

    # Reset the board spaces.
    coords.reset()
    # Reset the players.
    players.reset(coords)
    # Reset the walls.
    walls.reset()
    # Reset the paths to finish.
    # pf.reset()

def click_button_2_players(win, coords):
    '''
    When the 2_players button is clicked,
    perform the following actions:
    
    Add more info about this function's parameters here.
    '''
    
    # Show the selected button for the number of players.
    win.button_2_players.set_selected(True)
    win.button_3_players.set_selected(False)
    win.button_4_players.set_selected(False)

    # Show the human or bot question and the options for the those players.
    win.human_or_bot.set_show(True)
    win.player_1_t.set_show(True)
    win.player_2_t.set_show(True)
    win.player_3_t.set_show(False)
    win.player_4_t.set_show(False)
    win.button_hb_player_1.set_show(True)
    win.button_hb_player_2.set_show(True)
    win.button_hb_player_3.set_show(False)
    win.button_hb_player_4.set_show(False)

    # Show the start button if ready to begin.
    win.button_start.set_show(True)

    # Set the player_count = 2
    player_count = 2
    players = Players(player_count, coords, win)

    return players


def click_button_3_players(win, coords):
    '''
    When the 3_players button is clicked,
    perform the following actions:
    
    Add more info about this function's parameters here.
    '''
        
    # Show the selected button for the number of players.
    win.button_2_players.set_selected(False)
    win.button_3_players.set_selected(True)
    win.button_4_players.set_selected(False)

    # Show the human or bot question and the options for the those players.
    win.human_or_bot.set_show(True)
    win.player_1_t.set_show(True)
    win.player_2_t.set_show(True)
    win.player_3_t.set_show(True)
    win.player_4_t.set_show(False)
    win.button_hb_player_1.set_show(True)
    win.button_hb_player_2.set_show(True)
    win.button_hb_player_3.set_show(True)
    win.button_hb_player_4.set_show(False)

    # Show the start button if ready to begin.
    win.button_start.set_show(True)

    # Set the player_count = 3
    player_count = 3
    players = Players(player_count, coords, win)

    return players


def click_button_4_players(win, coords):
    '''
    When the 4_players button is clicked,
    perform the following actions:
    
    Add more info about this function's parameters here.
    '''

    # Show the selected button for the number of players.
    win.button_2_players.set_selected(False)
    win.button_3_players.set_selected(False)
    win.button_4_players.set_selected(True)

    # Show the human or bot question and the options for the those players.
    win.human_or_bot.set_show(True)
    win.player_1_t.set_show(True)
    win.player_2_t.set_show(True)
    win.player_3_t.set_show(True)
    win.player_4_t.set_show(True)
    win.button_hb_player_1.set_show(True)
    win.button_hb_player_2.set_show(True)
    win.button_hb_player_3.set_show(True)
    win.button_hb_player_4.set_show(True)

    # Show the start button if ready to begin.
    win.button_start.set_show(True)

    # Set the player_count = 4
    player_count = 4
    players = Players(player_count, coords, win)

    return players


def click_button_hb_player_1(win):
    '''
    When the human or bot button 1 is clicked,
    perform the following actions:
    
    Add more info about this function's parameters here.
    '''

    # If the button was not selected, now select it.
    if win.button_hb_player_1.selected == False:
        win.button_hb_player_1.set_selected(True)    
    # If the button was selected, deselect it.
    else:
        win.button_hb_player_1.set_selected(False)


def click_button_hb_player_2(win):
    '''
    When the human or bot button 2 is clicked,
    perform the following actions:
    
    Add more info about this function's parameters here.
    '''

    # If the button was not selected, now select it.
    if win.button_hb_player_2.selected == False:
        win.button_hb_player_2.set_selected(True)
    # If the button was selected, deselect it.
    else:
        win.button_hb_player_2.set_selected(False)


def click_button_hb_player_3(win):
    '''
    When the human or bot button 3 is clicked,
    perform the following actions:
    
    Add more info about this function's parameters here.
    '''

    # If the button was not selected, now select it.
    if win.button_hb_player_3.selected == False:
        win.button_hb_player_3.set_selected(True)
    # If the button was selected, deselect it.
    else:
        win.button_hb_player_3.set_selected(False)

def click_button_hb_player_4(win):
    '''
    When the human or bot button 4 is clicked,
    perform the following actions:
    
    Add more info about this function's parameters here.
    '''

    # If the button was not selected, now select it.
    if win.button_hb_player_4.selected == False:
        win.button_hb_player_4.set_selected(True)
    # If the button was selected, deselect it.
    else:
        win.button_hb_player_4.set_selected(False)


def click_button_start(win):
    '''
    When the start button is clicked,
    perform the following actions:
    
    Add more info about this function's parameters here.
    '''

    # Stop showing buttons and requests for how many players
    # and whether they are humans or bots.
    win.how_many_players.set_show(False)
    win.button_2_players.set_show(False)
    win.button_3_players.set_show(False)
    win.button_4_players.set_show(False)
    win.human_or_bot.set_show(False)
    win.player_1_t.set_show(False)
    win.player_2_t.set_show(False)
    win.player_3_t.set_show(False)
    win.player_4_t.set_show(False)
    win.button_hb_player_1.set_show(False)
    win.button_hb_player_2.set_show(False)
    win.button_hb_player_3.set_show(False)
    win.button_hb_player_4.set_show(False)

    # Show the wall button for playing walls in the game.
    win.button_wall.set_show(True)

    # Replace the start button with the restart button.
    win.button_start.set_show(False)
    win.button_restart.set_show(True)

    # Determine the number of players from the user input.
    if win.button_2_players.selected == True:
        player_count = 2
    
    elif win.button_3_players.selected == True:
        player_count = 3
    
    elif win.button_4_players.selected == True:
        player_count = 4

    # Determine whether each player is human or a bot and add their value to a dictionary.
    # Start an empty player types dictionary.
    player_types = {}

    if win.button_hb_player_1.selected == True:
        player_types[1] = ['bot']
    else:
        player_types[1] = ['human']

    if win.button_hb_player_2.selected == True:
        player_types[2] = ['bot']
    else:
        player_types[2] = ['human']
    
    if win.button_hb_player_3.selected == True:
        player_types[3] = ['bot']
    else:
        player_types[3] = ['human']
    
    if win.button_hb_player_4.selected == True:
        player_types[4] = ['bot']
    else:
        player_types[4] = ['human']

    '''
    Show player wall info on the right panel.
    '''

    # Start the game.
    coords = win.coords
    players = Players(player_count, coords, win)
    walls = Walls()
    # pf = PathFinder()

    last_play = ''
    running = True
    ready = False
    start = False

    while running == True:
        clock.tick(FPS)
        game = n.get_game()

        # Start a game
        '''Review this code and fix it to get the game running immediately.'''
        if not start:
            if not ready:
                players.set_names(game.names)
                ready = game.ready()
            if game.running:
                current_p = players.players[game.current_player]
                win.update_info(f"Let's go! {current_p.name} plays!",
                                current_p.color)
                start = True

    # Do something with player_count, player_types

def click_button_wall(win):
    win.button_wall.set_selected(True)
    # wall.select()
    '''
    Add check to ensure this button is selected when playing a wall.
    '''
    pass

