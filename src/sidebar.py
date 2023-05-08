from src.const import *
from src.window import *
from src.player import Players

def click_restart(win, coords, players, walls):
    '''
    This function resets the game board to setup mode and 
    clears the game board contents when the reset button is clicked.
    
    **Parameters**
        win: *Window obj*
            The current game board window that is being displayed.
        coords: *Coords obj*
            Contains information for the game board coordinates.
        players: *Players obj*
            Contains information about all of the players in the game.
        walls: *Walls obj*
            Contains information about all of the walls played on the game board.

    **Returns**
        setup: *bool*
            Returns setup to True to return the game to setup mode.
        running: *bool*
            Returns running to False to exit the game from running.
        end: *bool*
            Returns end to False to exit the end-game screen.
        players: *Players obj*
            Resets the number of players in the game to zero for initial setup.
    '''

    # Stop the game running and return to the setup window.
    setup = True
    running = False
    end = False

    # Clear all buttons from the screen.
    for button in Button.instances:
        button.set_show(False)
        button.set_selected(False)

    # Clear all text from the screen.
    for text in Text.instances:
        text.set_show(False)

    # Show the title, welcome text, and info text.
    win.welcome.set_show(True)
    win.title.set_show(True)
    win.info.set_show(True)
    
    # Show the user the buttons asking them to select the number of players.
    win.how_many_players.set_show(True)
    win.button_2_players.set_show(True)
    win.button_3_players.set_show(True)
    win.button_4_players.set_show(True)

    # Show the quit button.
    win.button_quit.set_show(True)

    # Reset the board spaces.
    coords.reset()

    # Reset the players.
    players.reset(coords)

    # Reset the walls.
    walls.reset()

    # Reset the paths to finish.
    # pf.reset()

    # Set the player_count = 0
    player_count = 0
    players = Players(player_count, coords, win)

    return setup, running, end, players


def click_button_2_players(win, coords):
    '''
    This function selects the number of players to be two and 
    continues setup to ask about the number of bots in the game.
    
    **Parameters**
        win: *Window obj*
            The current game board window that is being displayed.
        coords: *Coords obj*
            Contains information for the game board coordinates.

    **Returns**
        players: *Players obj*
            Sets the number of players in the game to two.
    '''
    
    # Show the selected button for the number of players.
    win.button_2_players.set_selected(True)
    win.button_3_players.set_selected(False)
    win.button_4_players.set_selected(False)

    # Show the human or bot question and the options for the number of players.
    win.human_or_bot.set_show(True)
    win.player_1_t.set_show(True)
    win.player_2_t.set_show(True)
    win.player_3_t.set_show(False)
    win.player_4_t.set_show(False)
    win.button_hb_player_1.set_show(True)
    win.button_hb_player_2.set_show(True)
    win.button_hb_player_3.set_show(False)
    win.button_hb_player_4.set_show(False)
    win.bot_not_ready.set_show(True)

    # Stop showing the welcome text.
    win.welcome.set_show(False)

    # Show the start button that the player may select if they are ready to begin.
    win.button_start.set_show(True)

    # Set the player_count = 2
    player_count = 2
    players = Players(player_count, coords, win)

    return players


def click_button_3_players(win, coords):
    '''
    This function selects the number of players to be three and 
    continues setup to ask about the number of bots in the game.
    
    **Parameters**
        win: *Window obj*
            The current game board window that is being displayed.
        coords: *Coords obj*
            Contains information for the game board coordinates.

    **Returns**
        players: *Players obj*
            Sets the number of players in the game to three.
    '''
        
    # Show the selected button for the number of players.
    win.button_2_players.set_selected(False)
    win.button_3_players.set_selected(True)
    win.button_4_players.set_selected(False)

    # Show the human or bot question and the options for the number of players.
    win.human_or_bot.set_show(True)
    win.player_1_t.set_show(True)
    win.player_2_t.set_show(True)
    win.player_3_t.set_show(True)
    win.player_4_t.set_show(False)
    win.button_hb_player_1.set_show(True)
    win.button_hb_player_2.set_show(True)
    win.button_hb_player_3.set_show(True)
    win.button_hb_player_4.set_show(False)
    win.bot_not_ready.set_show(True)

    # Stop showing the welcome text.
    win.welcome.set_show(False)

    # Show the start button that the player may select if they are ready to begin.
    win.button_start.set_show(True)

    # Set the player_count = 3
    player_count = 3
    players = Players(player_count, coords, win)

    return players


def click_button_4_players(win, coords):
    '''
    This function selects the number of players to be four and 
    continues setup to ask about the number of bots in the game.
    
    **Parameters**
        win: *Window obj*
            The current game board window that is being displayed.
        coords: *Coords obj*
            Contains information for the game board coordinates.

    **Returns**
        players: *Players obj*
            Sets the number of players in the game to four.
    '''

    # Show the selected button for the number of players.
    win.button_2_players.set_selected(False)
    win.button_3_players.set_selected(False)
    win.button_4_players.set_selected(True)

    # Show the human or bot question and the options for the the number of players.
    win.human_or_bot.set_show(True)
    win.player_1_t.set_show(True)
    win.player_2_t.set_show(True)
    win.player_3_t.set_show(True)
    win.player_4_t.set_show(True)
    win.button_hb_player_1.set_show(True)
    win.button_hb_player_2.set_show(True)
    win.button_hb_player_3.set_show(True)
    win.button_hb_player_4.set_show(True)
    win.bot_not_ready.set_show(True)

    # Stop showing the welcome text.
    win.welcome.set_show(False)

    # Show the start button that the player may select if they are ready to begin.
    win.button_start.set_show(True)

    # Set the player_count = 4
    player_count = 4
    players = Players(player_count, coords, win)

    return players


def click_button_hb_player_1(win):
    '''
    This function selects whether player 1 will play as a human or bot
    based on the selected value of the button.
    
    **Parameters**
        win: *Window obj*
            The current game board window that is being displayed.

    **Returns**
        N/A
    '''

    # If the button was not selected, now select it.
    if win.button_hb_player_1.selected == False:
        win.button_hb_player_1.set_selected(True)    
    # If the button was selected, deselect it.
    else:
        win.button_hb_player_1.set_selected(False)


def click_button_hb_player_2(win):
    '''
    This function selects whether player 2 will play as a human or bot
    based on the selected value of the button.
    
    **Parameters**
        win: *Window obj*
            The current game board window that is being displayed.

    **Returns**
        N/A
    '''

    # If the button was not selected, now select it.
    if win.button_hb_player_2.selected == False:
        win.button_hb_player_2.set_selected(True)
    # If the button was selected, deselect it.
    else:
        win.button_hb_player_2.set_selected(False)


def click_button_hb_player_3(win):
    '''
    This function selects whether player 3 will play as a human or bot
    based on the selected value of the button.
    
    **Parameters**
        win: *Window obj*
            The current game board window that is being displayed.

    **Returns**
        N/A
    '''

    # If the button was not selected, now select it.
    if win.button_hb_player_3.selected == False:
        win.button_hb_player_3.set_selected(True)
    # If the button was selected, deselect it.
    else:
        win.button_hb_player_3.set_selected(False)


def click_button_hb_player_4(win):
    '''
    This function selects whether player 4 will play as a human or bot
    based on the selected value of the button.
    
    **Parameters**
        win: *Window obj*
            The current game board window that is being displayed.

    **Returns**
        N/A
    '''

    # If the button was not selected, now select it.
    if win.button_hb_player_4.selected == False:
        win.button_hb_player_4.set_selected(True)
    # If the button was selected, deselect it.
    else:
        win.button_hb_player_4.set_selected(False)


def click_button_start(win):
    '''
    This function starts the game in running mode when the start button is clicked.
    
    **Parameters**
        win: *Window obj*
            The current game board window that is being displayed.

    **Returns**
        player_types: *dict*
            A dictionary of player types whether each player is a human or a bot
            for all players in-play at the start of the game.
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
    win.bot_not_ready.set_show(False)

    # Show the wall button for playing walls in the game.
    win.button_wall.set_show(True)

    # Replace the start button with the restart button.
    win.button_start.set_show(False)
    win.button_restart.set_show(True)

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

    return player_types


def click_button_wall(win):
    '''
    This function selects the wall button to allow the active player to play a wall.
    
    **Parameters**
        win: *Window obj*
            The current game board window that is being displayed.

    **Returns**
        N/A
    '''

    # If the button was not selected, now select it.
    if win.button_wall.selected == False:
        win.button_wall.set_selected(True)
    # If the button was selected, deselect it.
    else:
        win.button_wall.set_selected(False)
