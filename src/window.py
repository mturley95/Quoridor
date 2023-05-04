import pygame
import os
from const import *
from widgets import Text, Button
from coord import Coords


def pos_in_rect(rect, pos):
    '''Return True if pos is in the rectangle'''
    pos_x, pos_y = pos
    x, y, width, height = rect
    
    if (x <= pos_x and pos_x <= x + width
            and y <= pos_y and pos_y <= y + height):
        return True
    else:
        return False


class Window:
    # Create the pop-up game window.
    def __init__(self, width = Screen_Dim.WIDTH, height = Screen_Dim.HEIGHT, square_size = Board_Dim.SQ_SIZE, wall_width = Board_Dim.WALL_WIDTH,
                 title = "Quoridor", background_color = Colors.light_gray):
        self.width = width
        self.height = height
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
        image_path = os.path.join(os.path.dirname(__file__), '32x32_Icons')
        icon = pygame.image.load(os.path.join(image_path, 'quoridor_board_with_pawn.png'))
        pygame.display.set_icon(icon)
    
        # Fill the starting background with a silver color.
        self.win.fill(self.background_color)
            
        self.top_left = (70, 70)
        self.side_board = self.top_left[0] * 2 + 9 * self.square_size + 10 * self.wall_width

        # Display the title of the game
        self.title = Text("Quoridor", 
                          (self.side_board + 110, 50), Colors.black, size=50)

        # Add text asking the user how many players will play
        self.how_many_players = Text("How many players will play this game?", 
                                     (self.side_board + 40, 150), Colors.black, size = 20)

        # Add player count button
        self.button_2_players = Button("2", self.side_board + 100, 200, 
                                       Colors.blue, 40)
        self.button_3_players = Button("3", self.side_board + 200, 200, 
                                       Colors.red, 40)
        self.button_4_players = Button("4", self.side_board + 300, 200, 
                                       Colors.red, 40)
        
        # Add text asking the user how many players will play
        self.human_or_bot = Text("Will each player be a human or a bot?", 
                                 (self.side_board + 40, 300), Colors.black, size = 20)
        
        # Add player count button
        self.player_1 = Button("H", self.side_board + 50, 350, 
                               Colors.red, 40)
        self.player_2 = Button("H", self.side_board + 150, 350, 
                               Colors.red, 40)
        self.player_3 = Button("H", self.side_board + 250, 350, 
                               Colors.red, 40, show = False)
        self.player_4 = Button("H", self.side_board + 350, 350, 
                               Colors.red, 40, show = False)
        
        # Add text for the human vs bot key.
        self.human = Text("Red = Human", 
                          (self.side_board + 100, 410), Colors.black, size = 18)
        self.bot = Text("Blue = Bot", 
                       (self.side_board + 250, 410), Colors.black, size = 18)

        # Add start button
        self.button_start = Button("Start", self.side_board + 70, 500, 
                                   Colors.red)
        
        # Add wall button
        self.button_wall = Button("Wall", self.side_board + 100, 350, 
                                  Colors.red, show = False)
        
        # Add restart button
        self.button_restart = Button("Restart", self.side_board + 70, self.side_board - 100, 
                                   Colors.red, show = False)
        
        # Add quit button
        self.button_quit = Button("Quit", self.side_board + 250, 500, 
                                  Colors.red)
        
        # Draw text and buttons that are supposed to be showing.
        self.draw_text()
        self.draw_buttons()


    def draw_game_board(self, pos):
        '''Draw the game board'''
        for c in self.coords.coords:
            rect = c.rect
            if pos_in_rect(rect, pos):
                color = Colors.grey
            else:
                color = Colors.white
                wall_east = c.wall_east
                wall_south = c.wall_south
                if wall_east and pos_in_rect(wall_east.rect_small, pos):
                    wall_east.draw(Colors.grey_dark)
                elif wall_south and pos_in_rect(wall_south.rect_small, pos):
                    wall_south.draw(Colors.grey_dark)
            c.draw(color)

    def draw_finish_lines(self, players):
        """Draw the finish lines with the player's color"""
        for p in players.players:
            if p.name != '':
                if p.orient == "north":
                    pygame.draw.line(
                        self.win, p.color,
                        (self.top_left[0], self.top_left[1] + self.side_board),
                        (self.top_left[0] + self.side_board,
                         self.top_left[1] + self.side_board),
                        self.wall_width)
                elif p.orient == "east":
                    pygame.draw.line(
                        self.win, p.color,
                        (self.top_left[0], self.top_left[1]),
                        (self.top_left[0], self.top_left[1] + self.side_board),
                        self.wall_width)
                elif p.orient == "south":
                    pygame.draw.line(
                        self.win, p.color,
                        (self.top_left[0], self.top_left[1]),
                        (self.top_left[0] + self.side_board, self.top_left[1]),
                        self.wall_width)
                elif p.orient == "west":
                    pygame.draw.line(
                        self.win, p.color,
                        (self.top_left[0] + self.side_board, self.top_left[1]),
                        (self.top_left[0] + self.side_board,
                         self.top_left[1] + self.side_board),
                        self.wall_width)

    def draw_right_panel(self, game, players):
        """Draw the right panel with player's informations"""
        x, y = self.side_board + 50, 20
        self.title.draw(self.win, (x + 10, y))
        for p in players.players:
            if p.name != '':
                text_p = Text(f"{p.name}: {p.walls_remain} walls", p.color)
                text_p.draw(self.win, (x, y + 100*p.num_player + 100))

    def draw_buttons(self):
        '''Draw buttons'''
        for b in Button.instances:
            if b.show == True:
                b.draw(self.win)

    def draw_text(self):
        '''Draw buttons'''
        for t in Text.instances:
            if t.show == True:
                t.draw(self.win, t.pos)

    def redraw_window(self, game, players, walls, pos):
        """Redraw the full window"""
        self.win.fill(self.background_color)
        self.draw_game_board(pos)

        '''
        self.draw_finish_lines(players)
        self.draw_right_panel(game, players)
        '''
        self.draw_buttons()
        '''
        players.draw(self)
        walls.draw()
        '''
        self.info.draw(self.win, (self.top_left[0], self.height - 50))
        pygame.display.update()