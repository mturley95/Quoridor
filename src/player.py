import pygame
from src.window import *
from src.const import Colors


class Player():
    '''
    This class creates a Player object and allows control over player moves and info.
    
    Values:
        * num_player (int)
        * orient (str)
        * color (tuple: int)
        * coord (Coord obj)
        * win (Window obj)
        * name (str)
        * walls_remain (int)
        * selected (bool)
        * pos_moves_list (list)

    Functions:
        * __init__(self, num_player, walls_remain, orient, color, coord, win, selected)
        * set_default_name(self, num_player)
        * get_num_player(self)
        * has_walls(self)
        * can_play(self, game)
        * pos_moves(self, coord, walls, players)
        * draw_pos_moves(self, win, coord, walls, players)
        * click(self, pos)
        * set_selected(self, new_selected_value, win, walls, players)
        * can_play_wall(self, game)
        * play_move(self, pos_coord)
        * play_put_wall(self, pos, coords, walls, players)
        * draw(self, win)
        * has_win(self, coord)
    '''

    def __init__(self, num_player, walls_remain, orient, color, coord, win, \
                 selected = False):
        '''
        This function initializes the Player class.

        **Parameters**
            num_player: *int*
                The player identification number.
            walls_remain: *int*
                The number of walls that the player has remaining to play.
            orient: *str*
                The orientation of the side of the board that the player is starting on.
            color: *tuple: int* (int, int, int)
                (R, G, B):
                The color of the player.
            coord: *Coord obj*
                The space on the board that the player is on.
            win: *Window obj*
                The game window display object.
            selected: *bool*
                Controls whether the player's pawn is selected for a move.

        **Returns**
            N/A
        '''

        # Assign all variables to the class.
        self.num_player = num_player
        self.orient = orient
        self.color = color
        self.coord = coord
        self.win = win
        self.name = ''
        self.walls_remain = walls_remain
        self.selected = selected


    def set_default_name(self, num_player):
        '''
        This function sets the default name of the player.

        **Parameters**
            num_player: *int*
                The player identification number.

        **Returns**
            N/A
        '''

        # Set the name of the player to be their number plus 1
        # Ex: player_0 = "Player 1"
        self.name = (f"Player {num_player+1}")


    def get_num_player(self):
        '''
        This function returns the number of the player.

        **Parameters**
            N/A

        **Returns**
            num_player: *int*
                The player identification number.
        '''

        # Return the number of the player.
        return self.num_player
    

    def has_walls(self):
        '''
        This function returns whether the player has walls left to play.

        **Parameters**
            N/A

        **Returns**
            has_walls: *bool*
                Returns True if the player has walls left to play.
        '''
        
        # If the player still has walls left to play, return True
        if self.walls_remain > 0:
            return True


    def can_play(self, game):
        '''
        This function returns whether the player is the current player whose turn it is to play.

        **Parameters**
            game: *Game obj*
                Controls the game including determining whose turn it is to play.

        **Returns**
            can_play: *bool*
                Returns True if it is the player's turn to play.
        '''

        # If the game is running and the player is the current player,
        if game.running and game.current_player_number == self.get_num_player():
            # then they can play.
            return True
    
    def pos_moves(self, coord, walls, players):
        '''
        This function returns a list of the player's possible move coordinates
        based on their position and the status of the game board.

        **Parameters**
            coord: *Coord obj*
                Contains information about the player's current game board coordinate.
            walls: *Walls obj*
                Contains information about all of the walls played on the game board.
            players: *Players obj*
                Contains information about all of the players in the game.

        **Returns**
            pos_moves_list: *list*
                Returns a list of the player's possible move coordinates.
        '''

        # List the possible move directions. 
        move_dirs = [coord.north, coord.south, coord.east, coord.west]

        # Make an empty list of the possible moves.
        pos_moves_list = []
        
        # Index through the different move directions.
        for pos_move in move_dirs:
            
            # If the possible move is on the board
            # and there is no wall present in that direction: 
            if pos_move is not None and walls.no_wall(coord, pos_move):

                # If the position is occupied in the movement direction:
                if pos_move.is_occupied(players):
                    
                    # If the direction in question is north:
                    if coord.north is not None and pos_move == coord.north:
                        # If the position 2 spaces away in the north direction is 
                        # on the board and there is no wall present in that direction
                        # and that space is not occupied:
                        if pos_move.north is not None and \
                            walls.no_wall(pos_move, pos_move.north) == True and \
                            pos_move.north.is_occupied(players) != True:
                            
                            # Add the space two spaces to the north as a possible move.
                            pos_moves_list.append(pos_move.north)

                        # If the position 2 spaces away in the north direction is 
                        # on the board and there is a wall present in that direction
                        # and the space to the east of the occupied space does not have a wall
                        # and that space is not occupied:
                        if pos_move.north is not None and \
                            walls.no_wall(pos_move, pos_move.north) != True and \
                            pos_move.east is not None and \
                            walls.no_wall(pos_move, pos_move.east) == True and \
                            pos_move.east.is_occupied(players) != True:
                            
                            # Add the space diagonally to the northeast as a possible move.
                            pos_moves_list.append(pos_move.east)

                        # If the position 2 spaces away in the north direction is 
                        # on the board and there is a wall present in that direction
                        # and the space to the west of the occupied space does not have a wall
                        # and that space is not occupied:
                        if pos_move.north is not None and \
                            walls.no_wall(pos_move, pos_move.north) != True and \
                            pos_move.west is not None and \
                            walls.no_wall(pos_move, pos_move.west) == True and \
                            pos_move.west.is_occupied(players) != True:
                            
                            # Add the space diagonally to the northwest as a possible move.
                            pos_moves_list.append(pos_move.west)

                    
                    # If the direction in question is south:
                    if coord.south is not None and pos_move == coord.south:
                        # If the position 2 spaces away in the east direction is 
                        # on the board and there is no wall present in that direction
                        # and that space is not occupied:
                        if pos_move.south is not None and \
                            walls.no_wall(pos_move, pos_move.south) == True and \
                            pos_move.south.is_occupied(players) != True:
                            
                            # Add the space two spaces to the south as a possible move.
                            pos_moves_list.append(pos_move.south)

                        # If the position 2 spaces away in the south direction is 
                        # on the board and there is a wall present in that direction
                        # and the space to the east of the occupied space does not have a wall
                        # and that space is not occupied:
                        if pos_move.south is not None and \
                            walls.no_wall(pos_move, pos_move.south) != True and \
                            pos_move.east is not None and \
                            walls.no_wall(pos_move, pos_move.east) == True and \
                            pos_move.east.is_occupied(players) != True:
                            
                            # Add the space diagonally to the southeast as a possible move.
                            pos_moves_list.append(pos_move.east)

                        # If the position 2 spaces away in the south direction is 
                        # on the board and there is a wall present in that direction
                        # and the space to the west of the occupied space does not have a wall
                        # and that space is not occupied:
                        if pos_move.south is not None and \
                            walls.no_wall(pos_move, pos_move.south) != True and \
                            pos_move.west is not None and \
                            walls.no_wall(pos_move, pos_move.west) == True and \
                            pos_move.west.is_occupied(players) != True:
                            
                            # Add the space diagonally to the southwest as a possible move.
                            pos_moves_list.append(pos_move.west)


                    # If the direction in question is east:
                    if coord.east is not None and pos_move == coord.east:
                        # If the position 2 spaces away in the east direction is 
                        # on the board and there is no wall present in that direction
                        # and that space is not occupied:
                        if pos_move.east is not None and \
                            walls.no_wall(pos_move, pos_move.east) == True and \
                            pos_move.east.is_occupied(players) != True:
                            
                            # Add the space two spaces to the east as a possible move.
                            pos_moves_list.append(pos_move.east)

                        # If the position 2 spaces away in the east direction is 
                        # on the board and there is a wall present in that direction
                        # and the space to the north of the occupied space does not have a wall
                        # and that space is not occupied:
                        if pos_move.east is not None and \
                            walls.no_wall(pos_move, pos_move.east) != True and \
                            pos_move.north is not None and \
                            walls.no_wall(pos_move, pos_move.north) == True and \
                            pos_move.north.is_occupied(players) != True:
                            
                            # Add the space diagonally to the northeast as a possible move.
                            pos_moves_list.append(pos_move.north)

                        # If the position 2 spaces away in the east direction is 
                        # on the board and there is a wall present in that direction
                        # and the space to the south of the occupied space does not have a wall
                        # and that space is not occupied:
                        if pos_move.east is not None and \
                            walls.no_wall(pos_move, pos_move.east) != True and \
                            pos_move.south is not None and \
                            walls.no_wall(pos_move, pos_move.south) == True and \
                            pos_move.south.is_occupied(players) != True:
                            
                            # Add the space diagonally spaces to the southeast as a possible move.
                            pos_moves_list.append(pos_move.south)


                    # If the direction in question is west:
                    if coord.west is not None and pos_move == coord.west:
                        # If the position 2 spaces away in the west direction is 
                        # on the board and there is no wall present in that direction
                        # and that space is not occupied:
                        if pos_move.west is not None and \
                            walls.no_wall(pos_move, pos_move.west) == True and \
                            pos_move.west.is_occupied(players) != True:
                            
                            # Add the space two spaces to the west as a possible move.
                            pos_moves_list.append(pos_move.west)

                        # If the position 2 spaces away in the west direction is 
                        # on the board and there is a wall present in that direction
                        # and the space to the north of the occupied space does not have a wall
                        # and that space is not occupied:
                        if pos_move.west is not None and \
                            walls.no_wall(pos_move, pos_move.west) != True and \
                            pos_move.north is not None and \
                            walls.no_wall(pos_move, pos_move.north) == True and \
                            pos_move.north.is_occupied(players) != True:
                            
                            # Add the space diagonally spaces to the northwest as a possible move.
                            pos_moves_list.append(pos_move.north)

                        # If the position 2 spaces away in the west direction is 
                        # on the board and there is a wall present in that direction
                        # and the space to the south of the occupied space does not have a wall
                        # and that space is not occupied:
                        if pos_move.west is not None and \
                            walls.no_wall(pos_move, pos_move.west) != True and \
                            pos_move.south is not None and \
                            walls.no_wall(pos_move, pos_move.south) == True and \
                            pos_move.south.is_occupied(players) != True:
                            
                            # Add the space diagonally to the southwest as a possible move.
                            pos_moves_list.append(pos_move.south)

                # If the movement direction is not occupied,
                else:
                    # Add the adjacent space as a possible move.
                    pos_moves_list.append(pos_move)

        # Returns a list of possible move coordinates.
        return pos_moves_list

    
    def draw_pos_moves(self, win, walls, players):
        '''
        This function draws the possible moves for the active player when their piece is selected.
        
        **Parameters**
            win: *Window obj*
                The game display window object.
            walls: *Walls obj*
                Contains information about all of the walls played on the game board.
            players: *Players obj*
                Contains information about all of the players in the game.

        **Returns**
            N/A
        '''

        # Find the possible moves for a piece.
        pos_moves_list = self.pos_moves(self.coord, walls, players)

        # Index through all possible moves.
        for move in pos_moves_list:
            # Draw a purple circle wherever the player can move their piece.
            pygame.draw.circle(win.win, Colors.PURPLE, move.middle, 15)
        

    def click_on_player(self, pos):
        '''
        The function returns True if position that the mouse clicked on
        is in the active player's coordinate's rectangle.
        
        *Parameters**
            pos: *tuple: int* (int, int)
                The position that the mouse clicked on.

        **Returns**
            click_on_player: *bool*
                Returns True if the mouse click was on the player's coordinate.
        '''

        # Separate out x and y coordinates based on input position.
        pos_x, pos_y = pos
        
        # Checks to see if input position was coordinate space of the player's current position.
        if (self.coord.rect[0] <= pos_x and pos_x <= self.coord.rect[0] + self.coord.rect[2] 
        and self.coord.rect[1] <= pos_y and pos_y <= self.coord.rect[1] + self.coord.rect[3]) == True:
            # If so, return True
            return True


    def set_selected(self, new_selected_value, win, walls, players):
        '''
        This function sets the selected value of the player.
        If the player is selected, it draws their possible moves on the game board.

        **Parameters**
            new_selected_value: *bool*
                True if the player is selected and False if they are not.
            win: *Window obj*
                The game display window object.
            walls: *Walls obj*
                Contains information about all of the walls played on the game board.
            players: *Players obj*
                Contains information about all of the players in the game.

        **Returns**
            N/A
        '''

        # Set the player's selected value to the new value 
        # (switch between True and False).
        self.selected = new_selected_value
        # If the new value is true,
        if self.selected == True:
            # Draw the player's possible moves on the game board.
            self.draw_pos_moves(win, walls, players)


    def can_play_wall(self, game):
        '''
        This function checks whether a player is able to play a wall and
        returns True if they can.

        **Parameters**
            game: *Game obj*
                Controls the game including determining whose turn it is to play.

        **Returns**
            can_play_wall: *bool*
                Returns True if the player can play a wall.
        '''

        # Check if the player is the current player and if they have walls.
        if self.can_play(game) and self.has_walls():
            return True


    def play_move(self, pos_coord):
        '''
        This function moves the players pawn to the selected coordinate.
        
        **Parameters**
            pos_coord: *Coord obj*
                A possible coordinate space that the player can move to.

        **Returns**
            N/A
        '''

        # The the player coordinate to the possible coordinate that was selected.
        self.coord = pos_coord


    # # Add path_finder to this function once it is finished.
    # def play_put_wall(self, pos, coords, walls, path_finder, players):
    def play_put_wall(self, pos, coords, walls):
        '''
        This function places a wall on the game board if it is possible.
        It places the wall in the player's color, 
        subtracts 1 from the player's remaining walls,
        and updates the game info box stating that the player played a wall.

        **Parameters**
            pos: *tuple: int*
                The position of the mouse selecting where to place a wall.
            coords: *Coords obj*
                Controls the game board spaces and coordinates.
            walls: *Walls obj*
                Controls the game board walls including which have been played.

        **Returns**
            update_game_info: *str*
                Updates the game info text box with if a wall was played.
        '''

        # For all spaces on the game board:
        for coord in coords.coords:
            # Set eastern and southern walls for the coordinate space.
            wall_east = coord.wall_east
            wall_south = coord.wall_south

            # For both walls for a given coordinate:
            for wall in [wall_east, wall_south]:
                # If the wall is on the game board and 
                # the mouse click was on that wall's rectangular space and
                # A wall can be added into that space:
                if (wall is not None and pos_in_rect(wall.rect_small, pos)
                        and walls.can_add(wall)) == True:
                    
                    # # Code to run pathfinder once it's working:
                    # if path_finder.play_wall(w, players):
                    #     Do the stuff below:
                    # else:
                    #     return "You can't block players!"
                    
                    # Set the wall color to the player's color.
                    wall.set_color(self.color)
                    # Add the wall to the game board.
                    walls.add_wall(wall)
                    # Subtract one from the remaining walls.
                    self.walls_remain -= 1
                    
                    # # Code to add wall to pathfinder calculations once it is ready.
                    # Add a wall to the pathfinder code
                    # path_finder.add_wall(wall)
                    
                    # Return text to update the info box if the player played a wall.
                    return f"Player {self.get_num_player() + 1} played a wall."
                
        # Don't return anything if no wall is played.
        return None


    def draw(self, win):
        '''
        This function draws the player on the game board in the position they occupy.

        **Parameters**
            win: *Window obj*
                Controls the game board window object to update the screen.

        **Returns**
            N/A
        '''

        # Set the position of the icon to be in the middle of the space it occupies.
        (x, y) = self.coord.middle
        
        # If the player color is blue,
        if self.color == Colors.BLUE:
            # Draw the blue pawn onto its coordinate space.
            win.win.blit(Icons.BLUE_PAWN, (x - Icons.BLUE_PAWN.get_width()//2, \
                                           y - Icons.BLUE_PAWN.get_height()//2))
        # If the player color is red,
        if self.color == Colors.RED:
            # Draw the red pawn onto its coordinate space.
            win.win.blit(Icons.RED_PAWN, (x - Icons.RED_PAWN.get_width()//2, \
                                          y - Icons.RED_PAWN.get_height()//2))
        # If the player color is green,
        if self.color == Colors.GREEN:
            # Draw the green pawn onto its coordinate space.
            win.win.blit(Icons.GREEN_PAWN, (x - Icons.GREEN_PAWN.get_width()//2, \
                                            y - Icons.GREEN_PAWN.get_height()//2))
        # If the player color is yellow,
        if self.color == Colors.YELLOW:
            # Draw the yellow pawn onto its coordinate space.
            win.win.blit(Icons.YELLOW_PAWN, (x - Icons.YELLOW_PAWN.get_width()//2, \
                                             y - Icons.YELLOW_PAWN.get_height()//2))
        

    def has_win(self):
        '''
        This function checks whether a player won with their most recent move and 
        returns True if they did.

        **Parameters**
            N/A

        **Returns**
            has_win: *bool*
                Returns True if the player won.
        '''
        # If the player started on the north side of the board and 
        # they have made it to the south edge of the board.
        if self.orient == "north" and self.coord.y == 8:
            # Return True that they have won.
            return True
        # If the player started on the east side of the board and 
        # they have made it to the west edge of the board.
        if self.orient == "east" and self.coord.x == 0:
            # Return True that they have won.
            return True
        # If the player started on the south side of the board and 
        # they have made it to the north edge of the board.
        if self.orient == "south" and self.coord.y == 0:
            # Return True that they have won.
            return True
        # If the player started on the west side of the board and 
        # they have made it to the east edge of the board.
        if self.orient == "west" and self.coord.x == 8:
            # Return True that they have won.
            return True
        # If the player has not won, return False.
        return False


class Players:
    '''
    This class creates a Players object and manages the players on the game.
    
    Values:
        * player_count (int)
        * win (Window obj)

    Functions:
        * __init__(self, player_count, coords, win)
        * draw(self, win)
        * set_default_names(self)
        * reset(self, coords)
    '''

    def __init__(self, player_count, coords, win):
        '''
        This function initializes the Players class.

        **Parameters**
            player_count: *int*
                The number of players playing in the current game.
            coords: *Coords obj*
                The game board coordinates including piece and wall spaces.
            win: *Window obj*
                The game board display window object.

        **Returns**
            N/A
        '''

        # Assign all variables to the class.
        self.player_count = player_count
        self.win = win

        # If the player count is two,
        if self.player_count == 2:
            # Create two Player objects.
            self.players = [
                Player(0, 10, "north", Colors.BLUE, coords.find_coord(4, 0), win = self.win),
                Player(1, 10, "south", Colors.RED, coords.find_coord(4, 8), win = self.win)]
        
        # If the player count is three,
        elif self.player_count == 3:
            # Create three player objects.
            self.players = [
                Player(0, 7, "north", Colors.BLUE, coords.find_coord(4, 0), win = self.win),
                Player(1, 7, "south", Colors.RED, coords.find_coord(4, 8), win = self.win),
                Player(2, 7, "east", Colors.GREEN, coords.find_coord(8, 4), win = self.win)]
        
        # If the player count is four,
        elif player_count == 4:
            # Create four player objects.
            self.players = [
                Player(0, 5, "north", Colors.BLUE, coords.find_coord(4, 0), win = self.win),
                Player(1, 5, "south", Colors.RED, coords.find_coord(4, 8), win = self.win),
                Player(2, 5, "east", Colors.GREEN, coords.find_coord(8, 4), win = self.win),
                Player(3, 5, "west", Colors.YELLOW, coords.find_coord(0, 4), win = self.win)]


    def draw(self, win):
        '''
        This function draws all active players on the game board.
        
        **Parameters**
            win: *Window object*
                The game board display window object.

        **Returns**
            N/A
        '''
        
        # If there are active players:
        if self.player_count > 0:
            # For each player,
            for player in self.players:
                # Draw their piece on the board.
                player.draw(win)
    

    def set_default_names(self):
        '''
        This function sets the default names for all players selected to play the game.
        
        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # For each player,
        for player in self.players:
            # Set their default name based on their player number.
            player.set_default_name(player.get_num_player())


    def reset(self, coords):
        '''
        This function resets the player positions and walls.
        
        **Parameters**
            coords: *Coords obj*
                Controls all game spaces including wall and player spaces.

        **Returns**
            N/A
        '''

        # If the player count is 2,
        if self.player_count == 2:
            # Set the remaining wall count back to 10.
            walls_remain = 10
        # If the player count is 3,
        elif self.player_count == 3:
            # Set the remaining wall count back to 10.
            walls_remain = 7
        # If the player count is 4,
        elif self.player_count == 4:
            # Set the remaining wall count back to 10.
            walls_remain = 5
        
        # For each active player,
        for player in self.players:
            
            # Reset their position to their starting position based on their orientation.
            if player.orient == "north":
                player.coord = coords.find_coord(4, 0)
            elif player.orient == "east":
                player.coord = coords.find_coord(8, 4)
            elif player.orient == "south":
                player.coord = coords.find_coord(4, 8)
            elif player.orient == "west":
                player.coord = coords.find_coord(0, 4)
            
            # Reset the player walls remaining back to their original values. 
            player.walls_remain = walls_remain
