import pygame
from window import *
from const import Colors
from wall import Walls


class Player():
    '''
    Create and control a player.
    
    Add more info about the Player class here.
    '''

    def __init__(self, num_player, walls_remain, orient, color, coord, win, \
                 radius = 20, selected = False):
        '''
        Initialize the player class.
        
        Add more info about this function's parameters here.
        '''

        self.num_player = num_player
        self.orient = orient
        self.color = color
        self.coord = coord
        self.win = win
        self.radius = radius
        self.name = ''
        self.walls_remain = walls_remain
        self.selected = selected

    def set_name(self, num_player):
        '''
        Set the name of the player.

        Add more info about this function's parameters here.
        '''

        # Set the name of the player to be their number plus 1
        # Ex: player_0 = "Player 1"
        self.name = (f"Player {num_player+1}")


    def get_num_player(self):
        '''
        Get the number of the player.
        
        Add more info about this function's parameters here.
        '''

        # Return the number of the player.
        return self.num_player

    def has_walls(self):
        '''
        Return True if the player has walls left to play.
        
        Add more info about this function's parameters here.
        '''
        
        # If the player still has walls left to play, return True
        if self.walls_remain > 0:
            return True

    def can_play(self, game):
        '''
        Return True if the player can play.

        Add more info about this function's parameters here.
        '''

        # If the game is running and the player is the current player,
        if game.running and game.current_player == self.num_player:
            # then they can play.
            return True
    
    def pos_moves(self, coord):
        
        # List the possible move directions. 
        move_dirs = [coord.north, coord.south, coord.east, coord.west]

        # Make an empty list of the possible moves.
        pos_moves = []
        
        # Index through the different move directions.
        for pos_move in move_dirs:
            
            # If the possible move is on the board
            # and there is no wall present in that direction: 
            if pos_move is not None and walls.no_wall(coord, pos_move):

                # If the position is occupied in the movement direction:
                if pos_move.occupied:
                    
                    # If the direction in question is north:
                    if pos_move == coord.north:
                        # If the position 2 spaces away in the north direction is 
                        # on the board and there is no wall present in that direction
                        # and that space is not occupied:
                        if pos_move.north is not None and \
                            walls.no_wall(pos_move, pos_move.north) and \
                            pos_move.north.occupied != True:
                            
                            # Add the space two spaces to the north as a possible move.
                            pos_moves.append(pos_move.north)
                    
                    # If the direction in question is south:
                    if pos_move == coord.south:
                        # If the position 2 spaces away in the east direction is 
                        # on the board and there is no wall present in that direction
                        # and that space is not occupied:
                        if pos_move.south is not None and \
                            walls.no_wall(pos_move, pos_move.south) and \
                            pos_move.south.occupied != True:
                            
                            # Add the space two spaces to the south as a possible move.
                            pos_moves.append(pos_move.south)

                    # If the direction in question is east:
                    if pos_move == coord.east:
                        # If the position 2 spaces away in the east direction is 
                        # on the board and there is no wall present in that direction
                        # and that space is not occupied:
                        if pos_move.east is not None and \
                            walls.no_wall(pos_move, pos_move.east) and \
                            pos_move.east.occupied != True:
                            
                            # Add the space two spaces to the east as a possible move.
                            pos_moves.append(pos_move.east)

                    # If the direction in question is west:
                    if pos_move == coord.west:
                        # If the position 2 spaces away in the west direction is 
                        # on the board and there is no wall present in that direction
                        # and that space is not occupied:
                        if pos_move.west is not None and \
                            walls.no_wall(pos_move, pos_move.west) and \
                            pos_move.west.occupied != True:
                            
                            # Add the space two spaces to the west as a possible move.
                            pos_moves.append(pos_move.west)

                # If the movement direction is not occupied,
                else:
                    # Add the adjacent space as a possible move.
                    pos_moves.append(pos_move)

        # Returns a list of possible move coordinates.
        return pos_moves
    
    def draw_pos_moves(self, coord):
        '''
        This function draws purple dots on the player's possible moves.
        
        Add more info about this function's parameters here.
        '''

        # Find the possible moves for a piece.
        pos_moves = pos_moves(coord)

        # Index through all possible moves.
        for move in pos_moves:
            # Draw a purple circle wherever the player can move their piece.
            pygame.draw.circle(self.win, Colors.purple, move.middle, 15)


    def piece_selected(self, new_selected_value):
        self.selected = new_selected_value
        self.draw_pos_moves(self.coord)

    def can_play_wall(self, game):
        '''
        Return True if the player can play a wall.
        
        Add more info about this function's parameters here.
        '''

        # Check if the player is the current player and if they have walls.
        if self.can_play(game) and self.has_walls():
            return True


    def play_move(self, coord):
        '''
        Play a move if it is possible.
        
        Add more info about this function's parameters here.
        '''

        for move in pos_moves.list:
            if move.click(pos):
                self.coord = move


    # def play_put_wall(self, pos, coords, walls,
    #                   path_finder, players):
    def play_put_wall(self, pos, coords, walls,
                      players):
        """Put a wall if it is possible"""
        for c in coords.coords:
            wall_east = c.wall_east
            wall_south = c.wall_south
            for w in [wall_east, wall_south]:
                if (w is not None and pos_in_rect(w.rect_small, pos)
                        and walls.can_add(w)):
                    self.send_wall(c, w.orient)
                    # if path_finder.play_wall(w, players):
                    #     self.send_wall(c, w.orient)
                    #     return ''
                    # else:
                    #     return "You can't block players!"
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
    def __init__(self, player_count, coords, win):
        self.player_count = player_count
        self.win = win

        if self.player_count == 2:
            self.players = [
                Player(0, 10, "north", Colors.blue, coords.find_coord(4, 0), win = self.win),
                Player(1, 10, "south", Colors.red, coords.find_coord(4, 8), win = self.win)]
        
        elif self.player_count == 3:
            self.players = [
                Player(0, 7, "north", Colors.blue, coords.find_coord(4, 0), win = self.win),
                Player(1, 7, "east", Colors.red, coords.find_coord(8, 4), win = self.win),
                Player(2, 7, "south", Colors.green, coords.find_coord(4, 8), win = self.win)]
        
        elif player_count == 4:
            self.players = [
                Player(0, 5, "north", Colors.blue, coords.find_coord(4, 0), win = self.win),
                Player(1, 5, "east", Colors.red, coords.find_coord(8, 4), win = self.win),
                Player(2, 5, "south", Colors.green, coords.find_coord(4, 8), win = self.win),
                Player(3, 5, "west", Colors.yellow, coords.find_coord(0, 4), win = self.win)]

    def draw(self, win):
        '''
        Draw all players on the game board.
        
        Add more about function parameters here.
        '''
        
        if self.player_count > 0:
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
            player.coord.occupied = False
            player.coord = coords.find_coord(x, y)
            player.coord.occupied = True
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
