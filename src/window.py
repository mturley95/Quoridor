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
    def __init__(self, width = 800, height = 600, square_size=50, wall_width=10,
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
            
        self.top_left = (20, 20)
        self.side_board = 9 * self.square_size + 10 * self.wall_width
        
        # Add quit button
        self.button_quit = Button("Quit", self.side_board + 60,
                                  self.side_board - 50, Colors.red)
        self.buttons = [self.button_quit]

        self.title = Text("Quoridor", Colors.black, size=50)
        self.info = Text("Welcome to Quoridor!", Colors.black, size=45)

    def draw_buttons(self):
        """Draw buttons"""
        for b in self.buttons:
            if b.show == True:
                b.draw(self.win)

    def redraw_window(self, game, players, walls, pos):
        """Redraw the full window"""
        self.win.fill(self.background_color)
        self.draw_game_board(pos)
        self.draw_finish_lines(players)
        self.draw_right_panel(game, players)
        self.draw_buttons()
        players.draw(self)
        walls.draw()
        self.info.draw(self.win, (self.top_left[0], self.height - 50))
        pygame.display.update()


class Setup_Window(Window):
    # Create the pop-up game window.
    def __init__(self, width = 800, height = 600, square_size=50, wall_width=10,
                 title = "Quoridor", background_color = Colors.light_gray):
        super().__init__(width = 800, height = 600, square_size=50, wall_width=10,
                 title = "Quoridor", background_color = Colors.light_gray)
        
        # Add text asking the user how many players will play
        self.how_many_players = Text("How many players will play this game?", Colors.black, size = 30)
        self.how_many_players.draw(self.win, (self.side_board + 30,
                                  self.side_board - 175))

        # Add player count button
        self.button_player_count_2 = Button("2", self.side_board + 30,
                                  self.side_board - 150, Colors.red, 30)
        self.button_player_count_3 = Button("3", self.side_board + 60,
                                  self.side_board - 150, Colors.red, 30)
        self.button_player_count_4 = Button("4", self.side_board + 90,
                                  self.side_board - 150, Colors.red, 30)
        self.buttons = [self.button_player_count_2, self.button_player_count_3, self.button_player_count_4, self.button_quit]

        # Add Start button
        self.button_restart = Button("Start", self.side_board + 60,
                                     self.side_board - 100, Colors.red,
                                     show=False)

        self.title = Text("Quoridor", Colors.black, size=50)
        self.info = Text("Welcome to Quoridor!", Colors.black, size=45)

         # Game Loop
        running = True
        while running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        pygame.quit()


class Game_Window(Window):
        
    def __init__(self, width = 800, height = 600, square_size=50, wall_width=10,
                 title = "Quoridor", background_color = Colors.light_gray):
        super().__init__(width = 800, height = 600, square_size=50, wall_width=10,
                 title = "Quoridor", background_color = Colors.light_gray)
        self.top_left = (20, 20)
        self.side_board = 9 * self.square_size + 10 * self.wall_width

        # Add restart button
        self.button_restart = Button("Restart", self.side_board + 60,
                                     self.side_board - 100, Colors.red,
                                     show=False)
        
        # Add quit button
        self.button_quit = Button("Quit", self.side_board + 60,
                                  self.side_board - 50, Colors.red)
        self.buttons = [self.button_restart, self.button_quit]

        self.title = Text("Quoridor", Colors.black, size=50)
        self.info = Text("Welcome to Quoridor!", Colors.black, size=45)
        
        # What does this do?
        '''
        self.coords = Coords(self)
        '''

    # From intro video. Is this needed? Delete?
    '''
    # Game Loop
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    '''

    # Is this needed? Delete?
    '''
    def update_info(self, text, color = None):
        """Update info text"""
        self.info.text = text
        if color is not None:
            self.info.color = color
    '''

    def draw_game_board(self, pos):
        '''Draw the game board'''
        for c in self.coords.coords:
            rect = c.rect
            if pos_in_rect(rect, pos):
                color = Colors.grey_dark
            else:
                color = Colors.grey
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
        """Draw buttons"""
        for b in self.buttons:
            if b.show:
                b.draw(self.win)

    def redraw_window(self, game, players, walls, pos):
        """Redraw the full window"""
        self.win.fill(self.background_color)
        self.draw_game_board(pos)
        self.draw_finish_lines(players)
        self.draw_right_panel(game, players)
        self.draw_buttons()
        players.draw(self)
        walls.draw()
        self.info.draw(self.win, (self.top_left[0], self.height - 50))
        pygame.display.update()