# Import necessary libraries.
import pygame
from src.const import *
from src.disp_obj import Text, Button
from src.board import Coords


def pos_in_rect(rect, pos):
    '''
    This function returns True if the position is in the rectangle.
    
    **Parameters**

        rect: *tuple* (int, int, int, int)
            (x, y, x_width, y_height):
            The top left points of a rectangle and its width and height.
        pos: *tuple* (int, int)
            (x, y):
            A position to be assessed if it is in the rectangle provided.

    **Returns**

        position_in_rectange: *bool*
            Returns whether the position is in the rectangle (True) or not (False).
    '''

    # Separates the position tuple into x and y values.
    pos_x, pos_y = pos

    # Separates the rectangle being assessed into top-left x-coord,
    # top-left y-coord, height, and width.
    x, y, width, height = rect
    
    # Assesses if the position in question is contained within
    # the coordinates of the rectangle
    if (x <= pos_x and pos_x <= x + width \
        and y <= pos_y and pos_y <= y + height) == True:
        
        # Return True if so
        return True
    
    else:
        # Otherwise, return False.
        return False


class Window:
    '''
    This class creates and controls the pygame GUI window object and 
    all buttons and manipulations of its display.
    
    Values:
        * width (int)
        * height (int)
        * window_size (tuple, int)
        * square_size (int)
        * wall_width (int)
        * title (str)
        * background_color (tuple, int)
        * win (Pygame Screen: obj)
        * top_left (tuple, int)
        * side_board (int)
        * game_board (tuple, int)

    Functions:
        * __init__(self, width, height, square_size, wall_width, title, background_color)
        * update_info(self, text, color)
        * draw_game_board(self, pos)
        * draw_finish_lines(self, players)
        * draw_right_panel_info(self, game, players)
        * draw_buttons(self)
        * draw_text(self)
        * redraw_window(self, game, player, players, walls, pos)
    '''

    def __init__(self, width = Screen_Dim.WIDTH, height = Screen_Dim.HEIGHT, square_size = Board_Dim.SQUARE_SIZE, wall_width = Board_Dim.WALL_WIDTH,
                 title = "Quoridor", background_color = Colors.SILVER):
        '''
        This function initializes the Window class.

        **Parameters**
            width: *int*
                The width of the display window.
            height: *int*
                The height of the display window.
            square_size: *int*
                The size of one space on the game board.
            wall_width: *int*
                The width of one wall on the game board.
            title: *str*
                The title of the game.
            background_color: *tuple*
                The color of the background of the window.

        **Returns**
            N/A
        '''
        
        # Assign all variables to the class.
        self.width = width
        self.height = height
        # Assign a window size tuple based on give width and height.
        self.window_size = (self.width, self.height)
        self.square_size = square_size
        self.wall_width = wall_width
        self.title = title
        self.background_color = background_color

        # Display the pop-up game window.
        self.win = pygame.display.set_mode(self.window_size)

        # Set the window title.
        pygame.display.set_caption(title)

        # Add an icon consisting of a board with a pawn in front.
        pygame.display.set_icon(Icons.BOARD_WITH_PAWN)
    
        # Fill the starting background with a silver color.
        self.win.fill(self.background_color)
        
        # Set the top-left position for the game board within the window.
        self.top_left = (70, 70)
        
        # Calculate the right side of the game board to use for positioning.
        # right panel information.
        self.side_board = self.top_left[0] * 2 + 9 * self.square_size + 10 * self.wall_width

        # Display game info.
        self.welcome = Text("Welcome to Quoridor!", (self.top_left[0] + 50, self.height - 70),\
                         Colors.BLACK, size=45)

        # Display the title of the game.
        self.title = Text("Quoridor", 
                          (self.side_board + 115, 50), 
                          Colors.BLACK, size=50)
        
        # Display the info text.
        self.info = Text("", (self.side_board + 50, 150), \
                         Colors.BLACK, size = 40)
        
        # Set game board coordinates.
        self.coords = Coords(self)

        # Require the user to select how many players will play.
        self.how_many_players = Text("Select the number of players for this game.", 
                                     (self.side_board + 25, 150), 
                                     Colors.BLACK, size = 20)

        # Add player count buttons for the user to make that selection.
        self.button_2_players = Button("2", 
                                       self.side_board + 100, 200, 
                                       Colors.RED, 40)
        self.button_3_players = Button("3", 
                                       self.side_board + 200, 200, 
                                       Colors.RED, 40)
        self.button_4_players = Button("4", 
                                       self.side_board + 300, 200, 
                                       Colors.RED, 40)
        
        # Add text asking the user how many players will play. 
        # Default is human.
        self.human_or_bot = Text("Will each player be a human or a bot?", 
                                 (self.side_board + 40, 300), 
                                 Colors.BLACK, size = 20, show = False)
        
        # Add text for each human or bot so the user knows 
        # which player they are selecting.
        self.player_1_t = Text("Player 1", 
                               (self.side_board + 40, 340), 
                               Colors.BLUE, size = 18, show = False)
        self.player_2_t = Text("Player 2", 
                               (self.side_board + 140, 340), 
                               Colors.RED, size = 18, show = False)
        self.player_3_t = Text("Player 3", 
                               (self.side_board + 240, 340), 
                               Colors.GREEN, size = 18, show = False)
        self.player_4_t = Text("Player 4", 
                               (self.side_board + 340, 340), 
                               Colors.YELLOW, size = 18, show = False)
        
        # Add text stating that bots aren't ready yet.
        # Comment out once bots implemented.
        self.bot_not_ready = Text("Bot functionality has not been implemented yet.", 
                                 (self.side_board, 430), 
                                 Colors.BLACK, size = 20, show = False)
        
        # Add buttons for the user to click selecting each player as either
        # human player or a bot.
        self.button_hb_player_1 = Button("H", 
                                         self.side_board + 50, 370, 
                                         Colors.RED, 40, show = False)
        self.button_hb_player_2 = Button("H", 
                                         self.side_board + 150, 370, 
                                         Colors.RED, 40, show = False)
        self.button_hb_player_3 = Button("H", 
                                         self.side_board + 250, 370, 
                                         Colors.RED, 40, show = False)
        self.button_hb_player_4 = Button("H", 
                                         self.side_board + 350, 370, 
                                         Colors.RED, 40, show = False)

        # Add start button to start the game and lock in settings.
        self.button_start = Button("Start", 
                                   self.side_board + 70, 570, 
                                   Colors.GREEN, show = False)
        
        # Add wall button for the user to click and 
        # state their intentions to play a wall.
        self.button_wall = Button("Wall", 
                                  self.side_board + 160, 500, 
                                  Colors.RED, show = False)
        
        # Add restart button for the user to restart the game if desired.
        self.button_restart = Button("Restart", 
                                     self.side_board + 70, 570, 
                                     Colors.RED, show = False)
        
        # Add quit button for the user to quit the game if desired.
        self.button_quit = Button("Quit", 
                                  self.side_board + 250, 570, 
                                  Colors.RED)


    def update_info(self, text, color = None):
        '''
        This function updates the text object for the info bar at the top of the right panel.
        This is used once setup is complete and the game is running or
        a player has won and the game has ended.

        **Parameters**
            text: *str*
                Text to be displayed on the info panel.
            color: *tuple: int* (int, int, int)
                (R, G, B):
                Color of the text to be displayed.

        **Returns**
            N/A
        '''

        # Set the text of the Text object to be the input into the function.
        self.info.text = text
        # If a color is assigned, set the color of the Text object to the input into the function.
        if color is not None:
            self.info.color = color


    def draw_game_board(self, pos):
        '''
        This function draws the game board.
        It changes the shading of the spaces depending on if the mouse is hovering over them.
        
        **Parameters**
            pos: *tuple* (int, int)
                (x, y): 
                The current position of the mouse.

        **Returns**
            N/A
        '''

        # Set the game board rectangle based on its top left coordinates and size.
        game_board = (self.top_left[0], self.top_left[1], \
                      9 * self.square_size + 10 * self.wall_width, \
                      9 * self.square_size + 10 * self.wall_width)
        # Color the background of the game board white.
        color = Colors.WHITE
        # Color the background of the game board on the window.
        pygame.draw.rect(self.win, color, game_board)

        # For a coordinate in the grid of coordinates for the game board.
        # The coordinate is already associated with a unique position and 
        # its square size and includes all player spaces.
        for coord in self.coords.coords:

            # Set a rectangle: (x, y, win.square_size, win.square_size).
            rect = coord.rect

            # Returns True if the mouse pos in question is in the rectangle.
            if pos_in_rect(rect, pos):
                # For the position in the rectangle of a space on the board, 
                # draw the board gray (for the player spaces).
                color = Colors.GRAY

            else:
                # Otherwise, draw the board light gray for that position.
                color = Colors.LIGHT_GRAY
                
                # Add wall rectangular space to the east of the game square.
                wall_east = coord.wall_east

                # Add wall rectangular space to the south of the game square.
                wall_south = coord.wall_south

                # Checks to ensure the wall space is in the game board and makes it gray
                # if the player mouse is on that location (otherwise remains white).
                if wall_east and pos_in_rect(wall_east.rect_small, pos):
                    wall_east.draw(Colors.GRAY)
                elif wall_south and pos_in_rect(wall_south.rect_small, pos):
                    wall_south.draw(Colors.GRAY)
            
            # Draws the pixel on the board with the proper color. 
            coord.draw(color)


    def draw_finish_lines(self, players):
        '''
        This function draws the finish lines for each player in-play in their respective colors.
        
        **Parameters**
            players: *obj*
                Class object that includes all active players.

        **Returns**
            N/A
        '''

        # Index through all players if the number of players has been determined.
        if players.player_count > 0:
            for player in players.players:

                # Check the player orientation for the side of the board that
                # their piece is starting on.
                if player.orient == "north":
                    # If the player is starting north, draw a finish line on the
                    # south edge of the board for that player in the player's color.
                    pygame.draw.line(
                        self.win, player.color,
                        (self.top_left[0] - self.wall_width, self.side_board - self.top_left[1]),
                        (self.side_board - self.top_left[0] + self.wall_width, self.side_board - self.top_left[1]),
                        self.wall_width * 2 + 1)
                    
                    # Type in the player name at their starting line.
                    # Set font and size based on input parameters.
                    font = pygame.font.SysFont("Arial", 30)
                    # Render the text in the font and color selected.
                    text = font.render(f"Player {player.get_num_player() + 1}", 1, player.color, None)
                    # Rotate the text 180 degrees.
                    rotated_text = pygame.transform.rotate(text, 180)
                    # Draw the text object onto the window at the proper position.
                    self.win.blit(rotated_text, (self.side_board // 2 - 50, 20))
                
                elif player.orient == "east":
                    # If the player is starting east, draw a finish line on the
                    # west edge of the board for that player in the player's color.
                    pygame.draw.line(
                        self.win, player.color,
                        (self.top_left[0], self.top_left[1] - self.wall_width),
                        (self.top_left[0], self.side_board - self.top_left[1] + self.wall_width),
                        self.wall_width * 2 + 1)
                    
                    # Type in the player name at their starting line.
                    # Set font and size based on input parameters.
                    font = pygame.font.SysFont("Arial", 30)
                    # Render the text in the font and color selected.
                    text = font.render(f"Player {player.get_num_player() + 1}", 1, player.color, None)
                    # Rotate the text 90 degrees.
                    rotated_text = pygame.transform.rotate(text, 90)
                    # Draw the text object onto the window at the proper position.
                    self.win.blit(rotated_text, (self.side_board - 50, self.side_board // 2 - 50))
                
                elif player.orient == "south":
                    # If the player is starting south, draw a finish line on the
                    # north edge of the board for that player in the player's color.
                    pygame.draw.line(
                        self.win, player.color,
                        (self.top_left[0] - self.wall_width, self.top_left[1]),
                        (self.side_board - self.top_left[0] + self.wall_width, self.top_left[1]),
                        self.wall_width * 2 + 1)
                    
                    # Type in the player name at their starting line.
                    # Set font and size based on input parameters.
                    font = pygame.font.SysFont("Arial", 30)
                    # Render the text in the font and color selected.
                    text = font.render(f"Player {player.get_num_player() + 1}", 1, player.color, None)
                    # Draw the text object onto the window at the proper position.
                    self.win.blit(text, (self.side_board // 2 - 50, self.side_board - 50))
                                  
                
                elif player.orient == "west":
                    # If the player is starting west, draw a finish line on the
                    # east edge of the board for that player in the player's color.
                    pygame.draw.line(
                        self.win, player.color,
                        (self.side_board - self.top_left[0], self.top_left[1] - self.wall_width),
                        (self.side_board - self.top_left[0], self.side_board - self.top_left[1] + self.wall_width),
                        self.wall_width * 2 + 1)
                    
                    # Type in the player name at their starting line.
                    # Set font and size based on input parameters.
                    font = pygame.font.SysFont("Arial", 30)
                    # Render the text in the font and color selected.
                    text = font.render(f"Player {player.num_player + 1}", 1, player.color, None)
                    # Rotate the text 270 degrees.
                    rotated_text = pygame.transform.rotate(text, 270)
                    # Draw the text object onto the window at the proper position.
                    self.win.blit(rotated_text, (20, self.side_board // 2 - 50))


    def draw_right_panel_info(self, game, players):
        '''
        This function draws the right panel with the players' info including
        the current player's turn notification and each player's wall count.
        
        **Parameters**
            game: *obj*
                Class object that includes information as to whether the game is running and
                which player is currently active.
            players: *obj*
                Class object that includes all active players.

        **Returns**
            N/A
        '''

        # Start the right info panel 100 pixels away from the edge of the board
        # and spaced vertically in roughly the center of the right panel.
        x, y = self.side_board + 100, 260
        
        # If the number of players has been determined.
        if players.player_count > 0:
            # If the game is passed the setup screen and is running.
            if game.running == True:
                # Update the info panel letting the current player know that it's their turn.
                current_player = players.players[game.current_player_number]
                self.update_info(f"It's {current_player.name}'s turn!",
                                current_player.color)
                self.info.set_show(True)

                # Index through each player.
                for player in players.players:
                    # Record the player name and how many walls they have remaining.
                    text_player = Text(f"{player.name}: {player.walls_remain} walls left     ", \
                                (x - 25, y + 50 * player.get_num_player()), player.color)
                    # Draw the value on the right window.
                    text_player.draw(self.win)

        # If the number of players has not been determined
        # and the game has not been initiated:
        else:
            # Don't show the info panel on the right.
            self.info.set_show(False)


    def draw_buttons(self):
        '''
        This function draws the any active buttons onto the window.
        
        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # Index through all added buttons.
        for button in Button.instances:
            # If the button is showing:
            if button.show == True:
                # If the button is selected:
                if button.selected == True:
                    # Set the button color to blue.
                    button.set_color(Colors.BLUE)
                # Otherwise draw the buttons in red.
                button.draw(self.win)


    def draw_text(self):
        '''
        This function draws the any active text onto the window.
        
        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # Index through all created text objects.
        for text in Text.instances:
            # If the text objects are showing,
            if text.show == True:
                # Draw the text on the window and display it.
                text.draw(self.win)


    def redraw_window(self, game, players, walls, pos):
        '''
        This function redraws the window and updates it with
        any updated information from the game, players, walls, or mouse.
        
        **Parameters**
            game: *obj*
                Class object that includes information as to whether the game is running and
                which player is currently active.
            players: *obj*
                Class object that includes all active players and their positions.
            walls: *obj*
                Class object that includes all played walls and their positions.
            pos: *tuple* (int, int)
                (x, y): 
                The position of the mouse.

        **Returns**
            N/A
        '''
        # Fill the full window with the set background color.
        self.win.fill(self.background_color)

        # Then, draw the text on the window.
        self.draw_text()

        # Then, draw the buttons on the window.
        self.draw_buttons()

        # Then, draw the game board
        self.draw_game_board(pos)

        # Then, draw the player finish lines.
        self.draw_finish_lines(players)

        # Then, draw the right panel with the player information.
        self.draw_right_panel_info(game, players)
        
        # Then, draw the player tokens on the board.
        players.draw(self)

        # Then draw any walls that have been used on the board.
        walls.draw()

        # Draw a player's possible moves if they are selected.
        if players.player_count > 0:
            for player in players.players:
                if player.selected == True:
                    player.draw_pos_moves(self, walls, players)

        # Update the pygame window display.
        pygame.display.update()