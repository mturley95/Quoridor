# Import necessary libraries.
import pygame
import os
from src.const import *
from src.disp_obj import Text, Button
from src.board import Coords


def pos_in_rect(rect, pos):
    '''
    Return True if pos is in the rectangle.
    
    Add more info about the function here.
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
    Create the pop-up game window with instructions on how to update it.
    
    Add more info about the Window class here.
    '''

    def __init__(self, width = Screen_Dim.WIDTH, height = Screen_Dim.HEIGHT, square_size = Board_Dim.SQUARE_SIZE, wall_width = Board_Dim.WALL_WIDTH,
                 title = "Quoridor", background_color = Colors.silver):
        '''
        Initialize the Window class.
        
        Add more info about initialization parameters here.
        '''
        
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
                         Colors.black, size=45)

        # Display the title of the game.
        self.title = Text("Quoridor", 
                          (self.side_board + 115, 50), 
                          Colors.black, size=50)
        
        # Display the info text.
        self.info = Text("", (self.side_board + 50, 150), \
                         Colors.black, size = 40)
        
        # Set game board coordinates.
        self.coords = Coords(self)

        # Require the user to select how many players will play.
        self.how_many_players = Text("Select the number of players for this game.", 
                                     (self.side_board + 25, 150), 
                                     Colors.black, size = 20)

        # Add player count buttons for the user to make that selection.
        self.button_2_players = Button("2", 
                                       self.side_board + 100, 200, 
                                       Colors.red, 40)
        self.button_3_players = Button("3", 
                                       self.side_board + 200, 200, 
                                       Colors.red, 40)
        self.button_4_players = Button("4", 
                                       self.side_board + 300, 200, 
                                       Colors.red, 40)
        
        # Add text asking the user how many players will play. 
        # Default is human.
        self.human_or_bot = Text("Will each player be a human or a bot?", 
                                 (self.side_board + 40, 300), 
                                 Colors.black, size = 20)
        
        # Add text for each human or bot so the user knows 
        # which player they are selecting.
        self.player_1_t = Text("Player 1", 
                               (self.side_board + 40, 340), 
                               Colors.blue, size = 18, show = False)
        self.player_2_t = Text("Player 2", 
                               (self.side_board + 140, 340), 
                               Colors.red, size = 18, show = False)
        self.player_3_t = Text("Player 3", 
                               (self.side_board + 240, 340), 
                               Colors.green, size = 18, show = False)
        self.player_4_t = Text("Player 4", 
                               (self.side_board + 340, 340), 
                               Colors.yellow, size = 18, show = False)
        
        # Add buttons for the user to click selecting each player as either
        # human player or a bot.
        self.button_hb_player_1 = Button("H", 
                                         self.side_board + 50, 370, 
                                         Colors.red, 40, show = False)
        self.button_hb_player_2 = Button("H", 
                                         self.side_board + 150, 370, 
                                         Colors.red, 40, show = False)
        self.button_hb_player_3 = Button("H", 
                                         self.side_board + 250, 370, 
                                         Colors.red, 40, show = False)
        self.button_hb_player_4 = Button("H", 
                                         self.side_board + 350, 370, 
                                         Colors.red, 40, show = False)

        # Add start button to start the game and lock in settings.
        self.button_start = Button("Start", 
                                   self.side_board + 70, 570, 
                                   Colors.red)
        
        # Add wall button for the user to click and 
        # state their intentions to play a wall.
        self.button_wall = Button("Wall", 
                                  self.side_board + 160, 500, 
                                  Colors.red, show = False)
        
        # Add restart button for the user to restart the game if desired.
        self.button_restart = Button("Restart", 
                                     self.side_board + 70, 570, 
                                     Colors.red, show = False)
        
        # Add quit button for the user to quit the game if desired.
        self.button_quit = Button("Quit", 
                                  self.side_board + 250, 570, 
                                  Colors.red)
        
        # Draw text and buttons that are supposed to be showing on the game window.
        self.draw_text()
        self.draw_buttons()


    def update_info(self, text, color = None):
        """Update info text"""
        self.info.text = text
        if color is not None:
            self.info.color = color


    def draw_game_board(self, pos):
        '''
        Draw the game board.
        
        Add more info about the function here.
        '''
        game_board = (self.top_left[0], self.top_left[1], \
                      9 * self.square_size + 10 * self.wall_width, \
                      9 * self.square_size + 10 * self.wall_width)
        color = Colors.white
        pygame.draw.rect(self.win, color, game_board)

        # For a coordinate in the grid of coordinates for the game board.
        # The coordinate is already associated with a unique position and 
        # its square size.
        for c in self.coords.coords:

            # Set a rectangle: (x, y, win.square_size, win.square_size).
            rect = c.rect

            # Returns True if the mouse pos in question is in the rectangle.
            if pos_in_rect(rect, pos):
                # For the position in the rectangle of a space on the board, 
                # draw the board gray.
                color = Colors.gray

            else:
                # Otherwise, draw the board light gray for that position.
                color = Colors.light_gray
                
                # Add wall object to the east of the game square
                wall_east = c.wall_east

                # Add wall object to the south of the game square
                wall_south = c.wall_south

                # Checks to ensure the wall is in the game board and makes it gray
                # if it has been played on that location.
                if wall_east and pos_in_rect(wall_east.rect_small, pos):
                    wall_east.draw(Colors.gray)
                elif wall_south and pos_in_rect(wall_south.rect_small, pos):
                    wall_south.draw(Colors.gray)
            
            # Draws the pixel on the board with the proper color. 
            c.draw(color)


    def draw_finish_lines(self, players):
        '''
        Draw the finish lines with the player's color.
        
        Add more info about function parameters.
        '''

        # Index through all players.
        if players.player_count > 0:
            for p in players.players:

                # Check the player orientation for the side of the board that
                # their piece is starting on.
                if p.orient == "north":
                    # If the player is starting north, draw a finish line on the
                    # south edge of the board for that player in the player's color.
                    pygame.draw.line(
                        self.win, p.color,
                        (self.top_left[0] - self.wall_width, self.side_board - self.top_left[1]),
                        (self.side_board - self.top_left[0] + self.wall_width, self.side_board - self.top_left[1]),
                        self.wall_width * 2 + 1)
                    
                    # Type in the player name at their starting line.
                    # Set font and size based on input parameters.
                    font = pygame.font.SysFont("Arial", 30)
                    # Render the text in the font and color selected.
                    text = font.render(f"Player {p.num_player + 1}", 1, p.color, None)
                    # Rotate the text 180 degrees.
                    rotated_text = pygame.transform.rotate(text, 180)
                    # Draw the text object onto the window at the proper position.
                    self.win.blit(rotated_text, (self.side_board // 2 - 50, 20))
                
                elif p.orient == "east":
                    # If the player is starting east, draw a finish line on the
                    # west edge of the board for that player in the player's color.
                    pygame.draw.line(
                        self.win, p.color,
                        (self.top_left[0], self.top_left[1] - self.wall_width),
                        (self.top_left[0], self.side_board - self.top_left[1] + self.wall_width),
                        self.wall_width * 2 + 1)
                    
                    # Type in the player name at their starting line.
                    # Set font and size based on input parameters.
                    font = pygame.font.SysFont("Arial", 30)
                    # Render the text in the font and color selected.
                    text = font.render(f"Player {p.num_player + 1}", 1, p.color, None)
                    # Rotate the text 90 degrees.
                    rotated_text = pygame.transform.rotate(text, 90)
                    # Draw the text object onto the window at the proper position.
                    self.win.blit(rotated_text, (self.side_board - 50, self.side_board // 2 - 50))
                
                elif p.orient == "south":
                    # If the player is starting south, draw a finish line on the
                    # north edge of the board for that player in the player's color.
                    pygame.draw.line(
                        self.win, p.color,
                        (self.top_left[0] - self.wall_width, self.top_left[1]),
                        (self.side_board - self.top_left[0] + self.wall_width, self.top_left[1]),
                        self.wall_width * 2 + 1)
                    
                    # Type in the player name at their starting line.
                    # Set font and size based on input parameters.
                    font = pygame.font.SysFont("Arial", 30)
                    # Render the text in the font and color selected.
                    text = font.render(f"Player {p.num_player + 1}", 1, p.color, None)
                    # Draw the text object onto the window at the proper position.
                    self.win.blit(text, (self.side_board // 2 - 50, self.side_board - 50))
                                  
                
                elif p.orient == "west":
                    # If the player is starting west, draw a finish line on the
                    # east edge of the board for that player in the player's color.
                    pygame.draw.line(
                        self.win, p.color,
                        (self.side_board - self.top_left[0], self.top_left[1] - self.wall_width),
                        (self.side_board - self.top_left[0], self.side_board - self.top_left[1] + self.wall_width),
                        self.wall_width * 2 + 1)
                    
                    # Type in the player name at their starting line.
                    # Set font and size based on input parameters.
                    font = pygame.font.SysFont("Arial", 30)
                    # Render the text in the font and color selected.
                    text = font.render(f"Player {p.num_player + 1}", 1, p.color, None)
                    # Rotate the text 270 degrees.
                    rotated_text = pygame.transform.rotate(text, 270)
                    # Draw the text object onto the window at the proper position.
                    self.win.blit(rotated_text, (20, self.side_board // 2 - 50))


    def draw_right_panel_info(self, game, players):
        '''
        Draw the right panel with player's informations.
        
        Add more details about the function parameters here.
        '''

        # Start the right panel 100 pixels away from the edge of the board
        # and in the middle (vertically) of the right panel.
        x, y = self.side_board + 100, 260

        if players.player_count > 0:
            if game.running == True:
                current_p = players.players[game.current_player]
                self.update_info(f"It's {current_p.name}'s turn!",
                                current_p.color)
                self.info.set_show(True)

                # Index through each player.
                for p in players.players:
                    # Record the player name and how many walls they have remaining.
                    text_p = Text(f"{p.name}: {p.walls_remain} walls     ", \
                                (x, y + 50 * p.num_player), p.color)
                    # Draw the value on the right window.
                    text_p.draw(self.win, text_p.pos)

        else:
            self.info.set_show(False)


    def draw_buttons(self):
        '''
        Draw buttons.
        
        Add more details about the function parameters here.
        '''

        # Index through all added buttons.
        for b in Button.instances:
            # If the button is showing:
            if b.show == True:
                # If the button is selected:
                if b.selected == True:
                    # Set the button color to blue.
                    b.set_color(Colors.blue)
                # Otherwise draw the buttons in red.
                b.draw(self.win)


    def draw_text(self):
        '''
        Draw the text.
        
        Add more details about the function parameters here.
        '''

        # Index through all created text objects.
        for t in Text.instances:
            # If the text objects are showing,
            if t.show == True:
                # Draw the text on the window and display it.
                t.draw(self.win, t.pos)


    def redraw_window(self, game, current_p, players, walls, pos):
        '''
        Redraw the full window.
        
        Add more details about the function parameters here.
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
            for p in players.players:
                if p.selected == True:
                    current_p.draw_pos_moves(self, current_p.coord, walls, players)

        # Update the pygame window display.
        pygame.display.update()