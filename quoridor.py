'''
Quoridor
Mitch Turley

This project will allow the user to virtually play the Quoridor game published by Gigamic games.
The user may play against another user one-on-one or against a simple bot.
'''

# Import libraries.
import os
import pygame
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class Colors:
    # Colors to be used in the game
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    purple = (255, 0, 255)
    teal = (0, 255, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    light_gray = (200, 200, 200)
    gray = (128, 128, 128)
    dark_gray = (50, 50, 50)


class Text:
    '''Create a text box'''
    def __init__(self, text, color = Colors.black, size = 30, font = "ubuntu"):
        self.text = text
        self.color = color
        self.size = size
        self.font = font

    def draw(self, win, pos):
        '''Draw the text on the window'''
        font = pygame.font.SysFont(self.font, self.size)
        text = font.render(self.text, 1, self.color, True)
        win.blit(text, pos)


class Button:
    '''Create a button'''
    def __init__(self, text, x, y, color, width = 100, height = 30, show=True):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.button_size = (self.width, self.height)
        self.show = show

    def draw(self, win):
        '''Draw the button on the window'''
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont('ubuntu', 30)
        text = font.render(self.text, 1, Colors.black)
        win.blit(text,
                 (self.x + round(self.width/2) - round(text.get_width()/2),
                  self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        '''Return True if pos is in the button rectangle'''
        pos_x, pos_y = pos
        if (self.x <= pos_x and pos_x <= self.x + self.width
                and self.y <= pos_y and pos_y <= self.y + self.height):
            return True
        else:
            return False


# class Wall:


# class Walls:


# class Coord:


# class Coords:


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
        image_path = os.path.join(os.path.dirname(__file__), '32x32 Icons')
        icon = pygame.image.load(os.path.join(image_path, 'quoridor_board_with_pawn.png'))
        pygame.display.set_icon(icon)
    
        # Fill the starting background with a silver color.
        self.win.fill(self.background_color)

            
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


class Game_Window(Window):
        
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


class Player():
    """Create a player"""
    def __init__(self, num_player, walls_remain, orient, color, coord,
                 radius=20):
        self.num_player = num_player
        self.orient = orient
        self.color = color
        self.coord = coord
        self.radius = radius
        self.name = ''
        self.walls_remain = walls_remain

    def set_name(self, name):
        """Set the name of the player"""
        if name != '':
            self.name = name

    def get_num_player(self):
        """Get the num of the player"""
        return self.num_player

    def has_walls(self):
        """Return True if the player has walls"""
        return self.walls_remain > 0

    def can_play(self, game):
        """Return True if the player can play"""
        return game.run and game.current_player == self.num_player

    def can_play_wall(self, game):
        """Return True if the player can play a wall"""
        return self.can_play(game) and self.has_walls()

    def send_move(self, network, coord):
        """Send a move to the server"""
        if self.has_win(coord):
            win = "w"
        else:
            win = "c"
        data = ";".join(['P', str(self.num_player), str(0),
                        str(coord.x), str(coord.y), win])
        network.send(data)

    def play_move(self, walls, network):
        """Play a move if it is possible"""
        keys = pygame.key.get_pressed()
        coord = self.coord

        # Left
        if keys[pygame.K_LEFT]:
            c = coord.west
            if c is not None and walls.no_wall(coord, c):
                if c.is_occuped:
                    c2 = c.west
                    if (c2 is not None and not c2.is_occuped
                            and walls.no_wall(c, c2)):
                        self.send_move(network, c2)
                else:
                    self.send_move(network, c)

        # Right
        elif keys[pygame.K_RIGHT]:
            c = coord.east
            if c is not None and walls.no_wall(coord, c):
                if c.is_occuped:
                    c2 = c.east
                    if (c2 is not None and not c2.is_occuped
                            and walls.no_wall(c, c2)):
                        self.send_move(network, c2)
                else:
                    self.send_move(network, c)

        # Up
        elif keys[pygame.K_UP]:
            c = coord.north
            if c is not None and walls.no_wall(coord, c):
                if c.is_occuped:
                    c2 = c.north
                    if (c2 is not None and not c2.is_occuped
                            and walls.no_wall(c, c2)):
                        self.send_move(network, c2)
                else:
                    self.send_move(network, c)

        # Down
        elif keys[pygame.K_DOWN]:
            c = coord.south
            if c is not None and walls.no_wall(coord, c):
                if c.is_occuped:
                    c2 = c.south
                    if (c2 is not None and not c2.is_occuped
                            and walls.no_wall(c, c2)):
                        self.send_move(network, c2)
                else:
                    self.send_move(network, c)

    def send_wall(self, network, coord, orient):
        """Send a wall to the server"""
        data = ";".join(['P', str(self.num_player), str(1),
                        str(coord.x), str(coord.y), orient])
        network.send(data)

    def play_put_wall(self, pos, coords, walls, network,
                      path_finder, players):
        """Put a wall if it is possible"""
        for c in coords.coords:
            wall_east = c.wall_east
            wall_south = c.wall_south
            for w in [wall_east, wall_south]:
                if (w is not None and pos_in_rect(w.rect_small, pos)
                        and walls.can_add(w)):
                    if path_finder.play_wall(w, players):
                        self.send_wall(network, c, w.orient)
                        return ''
                    else:
                        return "You can't block players!"
        return ''

    def draw(self, win):
        """Draw player on the game board"""
        (x, y) = self.coord.middle
        pygame.draw.circle(win.win, self.color,
                           (x, y), self.radius)
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.name[0], 1, Colors.white)
        win.win.blit(text, (x - self.radius // 2, y - self.radius // 2))

    def has_win(self, coord):
        """Return True if the player wins in the coord"""
        if self.orient == "north" and coord.y == 8:
            return True
        if self.orient == "east" and coord.x == 0:
            return True
        if self.orient == "south" and coord.y == 0:
            return True
        if self.orient == "west" and coord.x == 8:
            return True
        return False


class Players:
    """Manage the players"""
    def __init__(self, player_count, coords):
        self.player_count = player_count
        if player_count == 4:
            self.players = [
                Player(0, 5, "north", Colors.red, coords.find_coord(4, 0)),
                Player(1, 5, "east", Colors.blue, coords.find_coord(8, 4)),
                Player(2, 5, "south", Colors.green, coords.find_coord(4, 8)),
                Player(3, 5, "west", Colors.yellow, coords.find_coord(0, 4))]
        elif self.player_count == 2:
            self.players = [
                Player(0, 10, "north", Colors.red, coords.find_coord(4, 0)),
                Player(1, 10, "south", Colors.green, coords.find_coord(4, 8))]
        elif self.player_count == 3:
            self.players = [
                Player(0, 7, "north", Colors.red, coords.find_coord(4, 0)),
                Player(1, 7, "east", Colors.blue, coords.find_coord(8, 4)),
                Player(2, 7, "south", Colors.green, coords.find_coord(4, 8))]

    def draw(self, win):
        """Draw all players on the game board"""
        for p in self.players:
            if p.name != '':
                p.draw(win)

    def get_player(self, num_player):
        """Get a player"""
        return self.players[num_player]

    def play(self, last_play, coords, walls, path_finder):
        """Make a player play"""
        data = last_play.split(";")
        player = self.get_player(int(data[1]))
        type_play = int(data[2])
        x, y = int(data[3]), int(data[4])
        if type_play == 0:   # Move
            player.coord.is_occuped = False
            player.coord = coords.find_coord(x, y)
            player.coord.is_occuped = True
            win = data[5]
            if win == "w":
                return False
            return True
        elif type_play == 1:    # Wall
            orient = data[5]
            coord_wall = coords.find_coord(x, y)
            if orient == "e":
                wall = coord_wall.wall_east
            elif orient == "s":
                wall = coord_wall.wall_south
            wall.set_color(player.color)
            walls.add_wall(wall)
            player.walls_remain -= 1
            path_finder.add_wall(wall)
        return True

    def set_names(self, names):
        """Set the names of players"""
        for player, name in zip(self.players, names):
            player.set_name(name)

    def reset(self, coords):
        """Reset the players"""
        if self.player_count == 2:
            walls_remain = 10
        elif self.player_count == 3:
            walls_remain = 7
        elif self.player_count == 4:
            walls_remain = 5
        for p in self.players:
            if p.orient == "north":
                p.coord = coords.find_coord(4, 0)
            elif p.orient == "east":
                p.coord = coords.find_coord(8, 4)
            elif p.orient == "south":
                p.coord = coords.find_coord(4, 8)
            elif p.orient == "west":
                p.coord = coords.find_coord(0, 4)
            p.walls_remain = walls_remain


class PathFinder:
    """Create the path finder to avoid blocked players"""
    def __init__(self):
        self.finder = AStarFinder()
        self.side = 17
        self.matrix = [[1]*self.side for _ in range(self.side)]
        self.make_walls()

    def make_walls(self):
        """Init the walls"""
        for i in range(self.side):
            if i % 2 == 1:
                for j in range(self.side):
                    if j % 2 == 1:
                        self.matrix[i][j] = 0

    def pos_player_in_grid(self, player):
        """Return the position of a player in the grid"""
        return (2*player.coord.y, 2*player.coord.x)

    def print_grid(self, grid=True, players=None):
        """Print the grid"""
        matrix = self.matrix.copy()
        if players is not None:
            for p in players.players:
                i, j = self.pos_player_in_grid(p)
                matrix[i][j] = -1
        grid = Grid(matrix=matrix)
        print(grid.grid_str())

    def add_wall(self, wall):
        """Add a wall"""
        if wall.orient == "e":
            y, x = 2*wall.coord1.x + 1, 2*wall.coord1.y
            for i in range(3):
                self.matrix[x + i][y] = 0
        elif wall.orient == "s":
            y, x = 2*wall.coord1.x, 2*wall.coord1.y + 1
            for i in range(3):
                self.matrix[x][y + i] = 0

    def remove_wall(self, wall):
        """Remove a wall"""
        if wall.orient == "e":
            y, x = 2*wall.coord1.x + 1, 2*wall.coord1.y
            for i in range(3):
                self.matrix[x + i][y] = 1
        elif wall.orient == "s":
            y, x = 2*wall.coord1.x, 2*wall.coord1.y + 1
            for i in range(3):
                self.matrix[x][y + i] = 1

    def find_path(self, player, show=False):
        """Return True if the player can finish"""
        x, y = self.pos_player_in_grid(player)
        grid = Grid(matrix=self.matrix)
        if player.orient == "north":
            x_end = self.side - 1
            for y_end in range(0, self.side, 2):
                start = grid.node(y, x)
                end = grid.node(y_end, x_end)
                path, runs = self.finder.find_path(start, end, grid)
                if path != []:
                    if show:
                        print(grid.grid_str(path=path, start=start, end=end))
                    return True
                grid.cleanup()

        elif player.orient == "east":
            y_end = 0
            for x_end in range(0, self.side, 2):
                start = grid.node(y, x)
                end = grid.node(y_end, x_end)
                path, runs = self.finder.find_path(start, end, grid)
                if path != []:
                    if show:
                        print(grid.grid_str(path=path, start=start, end=end))
                    return True
                grid.cleanup()

        elif player.orient == "south":
            x_end = 0
            for y_end in range(0, self.side, 2):
                start = grid.node(y, x)
                end = grid.node(y_end, x_end)
                path, runs = self.finder.find_path(start, end, grid)
                if path != []:
                    if show:
                        print(grid.grid_str(path=path, start=start, end=end))
                    return True
                grid.cleanup()

        elif player.orient == "west":
            y_end = self.side - 1
            for x_end in range(0, self.side, 2):
                start = grid.node(y, x)
                end = grid.node(y_end, x_end)
                path, runs = self.finder.find_path(start, end, grid)
                if path != []:
                    if show:
                        print(grid.grid_str(path=path, start=start, end=end))
                    return True
                grid.cleanup()

        return False

    def play_wall(self, wall, players):
        """Return True if the wall doesn't block players"""
        self.add_wall(wall)
        for p in players.players:
            if not self.find_path(p):
                self.remove_wall(wall)
                return False
        return True

    def reset(self):
        """Reset the matrix"""
        self.matrix.clear()
        self.matrix = [[1]*self.side for _ in range(self.side)]
        self.make_walls()


class Game:
    """Create a game"""
    def __init__(self, game_id, player_count):
        self.game_id = game_id
        self.player_count = player_count
        self.connected = [False] * player_count
        self.names = [''] * player_count
        self.run = False
        self.current_player = -1
        self.last_play = ''
        self.winner = ''
        self.wanted_restart = []

    def add_player(self, num_player):
        """Add a player"""
        self.connected[num_player] = True
        print(f"[Game {self.game_id}]: player {num_player} added")

    def add_name(self, data):
        """Add a player's name"""
        num_player = int(data.split(';')[1])
        name = data.split(';')[2]
        self.names[num_player] = name
        print(f"[Game {self.game_id}]: {name} added as player {num_player}")

    def remove_player(self, num_player):
        """Remove a player"""
        self.connected[num_player] = False
        self.names[num_player] = ''
        if self.player_count_connected() == 1:
            self.run = False
            self.current_player == -1
        else:
            if num_player == self.current_player:
                self.current_player = self.next_player(self.current_player)
                self.last_play = ';'.join(['D', str(num_player)])
        print(f"[Game {self.game_id}]: player {num_player} removed")

    def player_count_connected(self):
        """Return the number of players connected"""
        return self.connected.count(True)

    def players_missing(self):
        """Return the number of players missing to start"""
        return self.player_count - self.player_count_connected()

    def ready(self):
        """Return True if the game can start"""
        return self.player_count_connected() == self.player_count

    def next_player(self, current):
        """Return the new current player"""
        current = (current + 1) % self.player_count
        while not self.connected[current]:
            current = (current + 1) % self.player_count
        return current

    def get_name_current(self):
        """Return the name of the current player"""
        return self.names[self.current_player]

    def start(self):
        """Start the game"""
        self.winner = ''
        self.current_player = self.next_player(-1)
        self.run = True
        print(f"[Game {self.game_id}]: started")

    def play(self, data):
        """Get a move"""
        print(f"[Game {self.game_id}]: move {data}")
        self.last_play = data
        if data.split(';')[-1] == 'w':
            print(f"[Game {self.game_id}]: {self.get_name_current()} wins!")
            self.winner = self.get_name_current()
            self.current_player = -1
            self.run = False
            self.wanted_restart = []
        else:
            self.current_player = self.next_player(self.current_player)

    def restart(self, data):
        """Restart the game if there are enough players"""
        num_player = int(data.split(';')[1])
        self.wanted_restart.append(num_player)
        print(f"[Game {self.game_id}]: {self.names[num_player]} asked restart",
              end=' ')
        print(f"{len(self.wanted_restart)}/{self.player_count}")
        if len(self.wanted_restart) == self.player_count:
            self.start()


class Games:
    """Manage games"""
    def __init__(self, player_count):
        self.games = {}
        self.player_count = player_count
        self.num_player = 0
        self.game_id = 0

    def find_game(self, game_id):
        """Find a game"""
        if game_id in self.games:
            return self.games[game_id]
        return None

    def add_game(self):
        """Create a new game"""
        if self.game_id not in self.games:
            self.num_player = 0
            self.games[self.game_id] = Game(self.game_id, self.player_count)
            print(f"[Game {self.game_id}]: created")

    def del_game(self, game_id):
        """Delete a game"""
        if game_id in self.games:
            del self.games[game_id]
            print(f"[Game {game_id}]: closed")
            if game_id == self.game_id:
                self.num_player = 0

    def accept_player(self):
        """Accept a player"""
        if self.game_id not in self.games:
            self.add_game()
        self.games[self.game_id].add_player(self.num_player)
        return self.game_id, self.num_player

    def launch_game(self):
        """Lauch a game"""
        if self.games[self.game_id].ready():
            self.games[self.game_id].start()
            self.game_id += 1
        else:
            self.num_player += 1

    def remove_player(self, game_id, num_player):
        """Remove a player"""
        game = self.find_game(game_id)
        if game is not None:
            game.remove_player(num_player)
            if not game.run:
                self.del_game(game_id)


def start_game():
    '''Start the quoridor game.'''
    print("Welcome to Quoridor!")

    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()
    win = Window()

    # Create the font for the text
    font = pygame.font.SysFont(None, 40)

    # Set up the text input boxes
    user_input_box = pygame.Rect(100, 100, 100, 50)
    bot_input_box = pygame.Rect(300, 100, 100, 50)
    user_text = ''
    bot_text = ''

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Handle user input
                if event.key == pygame.K_RETURN:
                    # Get the number of users and bots
                    num_users = int(user_text)
                    num_bots = int(bot_text)
                    print("Starting game with", num_users, "users and", num_bots, "bots.")
                elif event.key == pygame.K_BACKSPACE:
                    if user_input_box.collidepoint(event.pos):
                        user_text = user_text[:-1]
                    elif bot_input_box.collidepoint(event.pos):
                        bot_text = bot_text[:-1]
                else:
                    if user_input_box.collidepoint(event.pos):
                        user_text += event.unicode
                    elif bot_input_box.collidepoint(event.pos):
                        bot_text += event.unicode

        # Draw the background and input boxes
        pygame.draw.rect(win.win, Colors.black, user_input_box, 2)
        pygame.draw.rect(win.win, Colors.black, bot_input_box, 2)

        # Draw the user input text
        user_surface = font.render(user_text, True, Colors.black)
        user_rect = user_surface.get_rect()
        user_rect.center = user_input_box.center
        win.win.blit(user_surface, user_rect)

        # Draw the bot input text
        bot_surface = font.render(bot_text, True, Colors.black)
        bot_rect = bot_surface.get_rect()
        bot_rect.center = bot_input_box.center
        win.win.blit(bot_surface, bot_rect)

        # Draw the labels for the input boxes
        user_label_surface = font.render("Number of users:", True, Colors.black)
        user_label_rect = user_label_surface.get_rect()
        user_label_rect.x = user_input_box.x - 200
        user_label_rect.centery = user_input_box.centery
        win.win.blit(user_label_surface, user_label_rect)

        bot_label_surface = font.render("Number of bots:", True, Colors.black)
        bot_label_rect = bot_label_surface.get_rect()
        bot_label_rect.x = bot_input_box.x - 200
        bot_label_rect.centery = bot_input_box.centery
        win.win.blit(bot_label_surface, bot_label_rect)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()


    # Select number of players
    proper_input = False
    while proper_input == False:
        number_of_players = input("Enter the number of players (up to 4): ")
        if number_of_players.isdigit():
            player_count = int(number_of_players)
            if 1<= player_count <= 4:
                proper_input = True
            else:
                print("The input is not a valid player count. Please enter a number between 1 and 4.")

    # Name input
    name = ''
    while name == '' or len(name) > 10:
        name = input("Enter your name: ").capitalize()
        if len(name) > 10:
            print("Too long")

    player_count, num_player = int(data[0]), int(data[1])

    # Send name
    try:
        n.send(';'.join(['N', str(num_player), name]))
    except Exception:
        print("Impossible to send data to the server")
        exit()

    print("Connexion established!")
    print(f"Hello {name}! You are player {num_player}!")

    # Init pygame
    pygame.init()
    clock = pygame.time.Clock()
    path = os.path.dirname(os.path.abspath(__file__))
    # sounds = Sounds(path)

    # Init game
    win = Window()
    coords = win.coords
    players = Players(player_count, coords)
    player = players.players[num_player]
    walls = Walls()
    pf = PathFinder()

    last_play = ''
    run = True
    ready = False
    start = False

    while run:
        clock.tick(40)
        n.send('get')
        try:
            game = n.get_game()
        except Exception:
            run = False
            print("Couldn't get game")
            break

        # Start a game
        if not start:
            if not ready:
                players.set_names(game.names)
                win.update_info(
                    f"Waiting for {game.players_missing()} players...")
                ready = game.ready()
            if game.run:
                current_p = players.players[game.current_player]
                win.update_info(f"Let's go! {current_p.name} plays!",
                                current_p.color)
                try:
                    sounds.start_sound.play()
                except Exception:
                    pass
                start = True
            elif game.wanted_restart != []:
                nb = len(game.wanted_restart)
                p = players.players[game.wanted_restart[-1]]
                win.update_info(
                    f"{p.name} wants to restart! ({nb}/{player_count})",
                    p.color)

        # Continue a game
        else:
            get_play = game.last_play
            if get_play != '' and get_play != last_play:
                if get_play[0] == 'D':
                    current_p = players.players[game.current_player]
                    win.update_info(f"{current_p.name} plays!",
                                    current_p.color)
                elif get_play[0] == 'P':
                    if players.play(get_play, coords, walls, pf):
                        current_p = players.players[game.current_player]
                        win.update_info(f"{current_p.name} plays!",
                                        current_p.color)
                    else:
                        win.update_info(f"{game.winner} wins!")
                        try:
                            sounds.winning_sound.play()
                        except Exception:
                            pass
                        win.button_restart.show = True
                        start = False
                last_play = get_play

        pos = pygame.mouse.get_pos()
        win.redraw_window(game, players, walls, pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if win.button_quit.click(pos):
                    run = False
                    pygame.quit()
                elif (not game.run and win.button_restart.click(pos)
                        and win.button_restart.show):   # Restart
                    coords.reset()
                    players.reset(coords)
                    walls.reset()
                    pf.reset()
                    win.button_restart.show = False
                    n.send(';'.join(['R', str(num_player)]))
                elif player.can_play_wall(game):    # Put a wall
                    mes = player.play_put_wall(
                        pos, coords, walls, n, pf, players)
                    if mes != '':
                        win.update_info(mes)

            elif event.type == pygame.KEYDOWN:  # Move pawn
                if player.can_play(game):
                    player.play_move(walls, n)

    print("Good bye!")



'''
# Create a class to control the functionality of the window and set up the board.
class Window:
    # Create the pop-up game window.
    def __init__(self, width = 800, height = 600, square_size = 40, wall_width = 10, title = 'Quoridor', background_color = Colors.light_gray):
        self.width = width
        self.height = height
        self.window_size = (height, width)
        self.square_size = square_size
        self.wall_width = wall_width
        self.title = title
        self.background_color = background_color

        # Display the pop-up game window.
        self.win = pygame.display.set_mode(self.window_size)
    
        # Fill the starting background with a silver color.
        self.win.fill(self.background_color)

    # Name the window title to "Quoridor"
    pygame.display.set_caption('Quoridor')
    
    # Add an icon consisting of a board with a pawn in front.
    image_path = os.path.join(os.path.dirname(__file__), '32x32 Icons')
    icon = pygame.image.load(os.path.join(image_path, 'quoridor_board_with_pawn.png'))
    pygame.display.set_icon(icon)

    # Game Loop
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
'''

# class Player:


if __name__ == "__main__":
    start_game()

    '''
    # Initialize the pygame library.
    pygame.init()
    clock = pygame.time.Clock()

    win = Window()
    # players = Players(player_count, player_coords)


    # screen = pygame.display.set_mode((800,600))
    '''