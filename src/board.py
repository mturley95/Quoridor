import pygame
from src.wall import Wall
from src.const import Board_Dim

class Coord:
    '''
    This class creates and controls a player space coordinate on the game board.
    
    Values:
        * x (int)
        * y (int)
        * pos (tuple: int)
        * occupied (bool)
        * top_left (tuple: int)
        * middle (tuple: int)
        * rect (tuple: int)
        * north (Coord obj)
        * east (Coord obj)
        * south (Coord obj)
        * west (Coord obj)
        * wall_east (Wall obj)
        * wall_south (Wall obj)

    Functions:
        * __init__(self, x, y, win, coords)
        * coord_north(self)
        * coord_east(self)
        * coord_south(self)
        * coord_west(self)
        * make_top_left(self)
        * make_middle(self)
        * make_rect(self)
        * make_wall_east(self)
        * make_wall_south(self)
        * link_coord(self)
        * make_walls(self)
        * make_cross_walls(self)
        * same_row(self, other)
        * same_column(self, other)
        * __eq__(self, other)
        * draw(self, color)
        * click_on_coord(self, pos)
        * is_occupied(self, players)
    '''

    def __init__(self, x, y, win, coords):
        '''
        This function initializes the Coord class.

        **Parameters**
            x: *int*
                The x-position of the coordinate.
            y: *int*
                The y-position of the coordinate.
            win: *Window obj*
                The game display window object.
            coords: *Coords obj*
                The game board coordinates object.

        **Returns**
            N/A
        '''

        # Assign all variables to the class.
        self.win = win
        self.coords = coords

        self.x = x
        self.y = y
        # Set the coordinate position using its x and y values.
        self.pos = (x, y)
        # Set the initial coordinate occupied value to False (not occupied).
        self.occupied = False

        # Assign the position value of the top left of the coordinate.
        self.top_left = self.make_top_left()
        # Assign the position value of the middle of the coordinate.
        self.middle = self.make_middle()
        # Assign the rectangular position and size of the coordinate. 
        # (x, y, width, height)
        self.rect = self.make_rect()

        # Assign the value for links between this coordinate and others on the game board.
        self.north = None
        self.east = None
        self.south = None
        self.west = None

        # Assign the values for whether there are neighboring walls to the coordinate space.
        self.wall_east = None
        self.wall_south = None


    def coord_north(self):
        '''
        This function returns the coordinate space to the north
        of the current coordinate space.

        **Parameters**
            N/A

        **Returns**
            coord_north: *Coord obj*
                Returns the coordinate space to the north of the current coordinate space. 
        '''

        # If the coordinate to the north of the current coordinate is still on the game board:
        if self.y - 1 >= 0:
            # Return that coordinate.
            return self.coords.find_coord(self.x, self.y - 1)
        # If it is off the game board, return None.
        return None
    

    def coord_east(self):
        '''
        This function returns the coordinate space to the east
        of the current coordinate space.

        **Parameters**
            N/A

        **Returns**
            coord_east: *Coord obj*
                Returns the coordinate space to the east of the current coordinate space. 
        '''

        # If the coordinate to the east of the current coordinate is still on the game board:
        if self.x + 1 <= Board_Dim.ROWS-1:
            # Return that coordinate.
            return self.coords.find_coord(self.x + 1, self.y)
        # If it is off the game board, return None.
        return None
    

    def coord_south(self):
        '''
        This function returns the coordinate space to the south
        of the current coordinate space.

        **Parameters**
            N/A

        **Returns**
            coord_south: *Coord obj*
                Returns the coordinate space to the south of the current coordinate space. 
        '''

        # If the coordinate to the south of the current coordinate is still on the game board:
        if self.y + 1 <= Board_Dim.COLS-1:
            # Return that coordinate.
            return self.coords.find_coord(self.x, self.y + 1)
        # If it is off the game board, return None.
        return None
    

    def coord_west(self):
        '''
        This function returns the coordinate space to the west
        of the current coordinate space.

        **Parameters**
            N/A

        **Returns**
            coord_north: *Coord obj*
                Returns the coordinate space to the west of the current coordinate space. 
        '''

        # If the coordinate to the west of the current coordinate is still on the game board:
        if self.x - 1 >= 0:
            # Return that coordinate.
            return self.coords.find_coord(self.x - 1, self.y)
        # If it is off the game board, return None.
        return None
    

    def make_top_left(self):
        '''
        This function returns the top left point of the coordinate space
        on a window.

        **Parameters**
            N/A

        **Returns**
            pos: *tuple: int* (int, int)
                (x, y):
                Returns the position of the top left point of the coordinate space.
        '''

        # Identify the game board window.
        win = self.win

        # Assign the x-position of the top-left of the coordinate space.
        x = ((win.wall_width + win.square_size)*self.x
             + win.wall_width + win.top_left[0])
        # Assign the y-position of the top-left of the coordinate space.
        y = ((win.wall_width + win.square_size)*self.y
             + win.wall_width + win.top_left[1])
        # Assign the position variable to be the x- and y- values of the top-left corner.
        pos = (x, y)

        # Return the position of the top left point of the coordinate space.
        return pos
    

    def make_middle(self):
        '''
        This function returns the middle point of the coordinate space on a window.

        **Parameters**
            N/A

        **Returns**
            pos: *tuple: int* (int, int)
                (x, y):
                Returns the position of the top left point of the coordinate space.
        '''

        # Identify the game board window.
        win = self.win

        # Assign the x-position of the middle of the coordinate space.        
        x = ((win.wall_width + win.square_size)*self.x
             + (win.wall_width + win.square_size // 2)
             + win.top_left[0])
        # Assign the y-position of the middle of the coordinate space.
        y = ((win.wall_width + win.square_size)*self.y
             + (win.wall_width + win.square_size // 2)
             + win.top_left[1])
        # Assign the position variable to be the x- and y- values of the middle point.
        pos = (x, y)

        # Return the position of the middle point of the coordinate space.
        return pos
    

    def make_rect(self):
        '''
        This function returns the rectangle position and size of the coordinate space.

        **Parameters**
            N/A

        **Returns**
            rect: *tuple: int* (int, int, int, int)
                (x, y, width, height):
                Returns the rectangle position and size of the coordinate space.
        '''

        # Identify the game board window.
        win = self.win

        # Assigns the x- and y- coordinate to the top-left corner of the coordinate space.
        x, y = self.top_left

        # Return the rectangle position and size of the coordinate space.
        return (x, y, win.square_size, win.square_size)
    

    def make_wall_east(self):
        '''
        This function returns the east wall of the coordinate space.

        **Parameters**
            N/A

        **Returns**
            wall_east: *Wall obj*
                Returns the wall to the east of the coordinate space.
        '''

        # If the space to the east of the current coordinate is still on the game board and
        # the space to the south of the current coordinate is still on the game board.
        if self.east is not None and self.y != Board_Dim.ROWS-1:
            # Return the eastern wall of the coordinate space.
            return Wall(self, self.east, self.win)
        # If one of the coordinates are off the game board, return None.
        return None
    

    def make_wall_south(self):
        '''
        This function returns the south wall of the coordinate space.

        **Parameters**
            N/A

        **Returns**
            wall_south: *Wall obj*
                Returns the wall to the south of the coordinate space.
        '''

        # If the space to the south of the current coordinate is still on the game board and
        # the space to the east of the current coordinate is still on the game board.
        if self.south is not None and self.x != Board_Dim.COLS-1:
            # Return the southern wall of the coordinate space.
            return Wall(self, self.south, self.win)
        # If one of the coordinates are off the game board, return None.
        return None
    

    def link_coord(self):
        '''
        This function links the coordinate space with the coordinate spaces
        to the north, east, south, and west of it.

        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # Link the coordinate space with the coordinate spaces next to it
        # using directional assignments.
        self.north = self.coord_north()
        self.east = self.coord_east()
        self.south = self.coord_south()
        self.west = self.coord_west()


    def make_walls(self):
        '''
        This function makes the walls around the coordinate that
        are directly linked to it (east and south walls).

        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # Link the coordinate space with the walls next to it
        # using directional assignments.
        self.wall_east = self.make_wall_east()
        self.wall_south = self.make_wall_south()


    def make_cross_walls(self):
        '''
        This function makes the cross-walls of the coordinate to ensure
        no walls interfere with walls that have already been played.

        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # If the eastern wall is on the game board:
        if self.wall_east is not None:
            # Make the eastern wall a cross-wall to prevent interfering walls from being played.
            self.wall_east.make_cross_wall()
        # If the southern wall is on the game board:
        if self.wall_south is not None:
            # Make the southern wall a cross-wall to prevent interfering walls from being played.
            self.wall_south.make_cross_wall()


    def same_row(self, other):
        '''
        This function checks whether two coordinate spaces are in the same row and 
        returns True if they are.

        **Parameters**
            other: *Coord obj*
                A different coordinate space to be compared to this coordinate space.

        **Returns**
            same_row: *bool*
                Returns true if two coordinate spaces are in the same row.
        '''

        # If the coordinates have the same y-position:
        if self.y == other.y:
            # Return true that the two coordinates are in the same row.
            return True
    

    def same_column(self, other):
        '''
        This function checks whether two coordinate spaces are in the same column and 
        returns True if they are.

        **Parameters**
            other: *Coord obj*
                A different coordinate space to be compared to this coordinate space.

        **Returns**
            same_column: *bool*
                Returns true if two coordinate spaces are in the same column.
        '''

        # If the coordinates have the same x-position:
        if self.x == other.x:
            # Return true that the two coordinates are in the same row.
            return True
    

    def __eq__(self, other):
        '''
        This function checks whether two coordinate spaces are the same space
        using the == operator between two coordinates.

        **Parameters**
            other: *Coord obj*
                A different coordinate space to be compared to this coordinate space.

        **Returns**
            __eq__: *bool*
                Returns true if the two coordinate spaces are the same space.
        '''

        # If the coordinates have the same x- and y- positions:
        if self.x == other.x and self.y == other.y:
            # Return True that the two coordinates are the same coordinate space.
            return True
    

    def draw(self, color):
        '''
        This function draws the rectangle of the coordinate on the game board.
        
        **Parameters**
            color: *tuple: int* (int, int, int)
                (R, G, B):
                The color value to draw the coordinate as.

        **Returns**
            N/A
        '''

        # Draw the coordinate rectangle at the proper position, size, and color on the game board.
        pygame.draw.rect(self.win.win, color, self.rect)


    def click_on_coord(self, pos):
        '''
        The function returns True if position that the mouse clicked on
        is in the coordinate rectangle.
        
        *Parameters**
            pos: *tuple: int* (int, int)
                The position that the mouse clicked on.

        **Returns**
            click_on_coord: *bool*
                Returns True if the mouse click was on the coordinate rectangle.
        '''

        # Separate out x and y coordinates based on input position.
        pos_x, pos_y = pos
        
        # Checks to see if input position was within the coordinate's area.
        if (self.rect[0] <= pos_x and pos_x <= self.rect[0] + self.rect[2] 
        and self.rect[1] <= pos_y and pos_y <= self.rect[1] + self.rect[3]) == True:
            # If so, return True
            return True
    

    def is_occupied(self, players):
        '''
        The function returns True if the coordinate space is occupied by a player.
        
        *Parameters**
            players: *Players obj*
                This object controls all of the players' information including
                their coordinate positions.

        **Returns**
            is_occupied: *bool*
                Returns True if the coordinate space is occupied by a player pawn.
        '''

        # Iterate through all players.
        for player in players.players:
            # and check if they are in the same location as this coordinate.
            if player.coord.x == self.x and player.coord.y == self.y:
                # If so, return True that the coordinate space is occupied by a player.
                return True


class Coords:
    '''
    This class creates the game board and manages the game board coordinates.
    
    Values:
        * win (Window obj)
        * coords (Coords obj)

    Functions:
        * __init__(self, win)
        * make_coords_grid(self)
        * link_coords(self)
        * make_walls(self)
        * find_coord(self, x, y)
        * reset(self)
    '''

    def __init__(self, win):
        '''
        This function initializes the Coords class and makes the game board.

        **Parameters**
            win: *Window obj*
                The game display window object.

        **Returns**
            N/A
        '''

        # Set the classes window to be the game window.
        self.win = win
        # Make the coordinate grid to make the game board.
        self.coords = self.make_coords_grid()
        # Link each coordinate to the coordinates around it.
        self.link_coords()
        # Link each coordinate to the walls around it and make those spaces on the board.
        self.make_walls()


    def make_coords_grid(self):
        '''
        The function makes the grid of Coord objects for the game board.
        
        *Parameters**
            N/a

        **Returns**
            coords: *list*
                Returns the grid of coordinates for the game board
                as a list of Coord objects.
        '''

        # Make an empty list of game coordinates.
        coords = []

        # For each column in the game board,
        for x in range(Board_Dim.COLS):
            # And for each row in the game board,
            for y in range(Board_Dim.ROWS):
                # Append a new coordinate space to the coordinate list.
                coords.append(Coord(x, y, self.win, self))
        # Once the game board is made, return the list of Coordinate objects.
        return coords
    

    def link_coords(self):
        '''
        This function links the coordinate space with the coordinate spaces
        to the north, east, south, and west of it for all coordinates on the game board.

        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # For every coordinate space on the game board,
        for coord in self.coords:
            # Link it to the coordinates around it.
            coord.link_coord()


    def make_walls(self):
        '''
        This function makes all of the walls and cross walls objects around
        every coordinate on the game board.

        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # For every coordinate space on the game board,
        for coord in self.coords:
            # Make the wall objects around it.
            coord.make_walls()
            # And make the cross walls around it.
            coord.make_cross_walls()


    def find_coord(self, x, y):
        '''
        This function finds the coordinate space corresponding to a
        given x, y position for the coordinate grid.
        
        **Parameters**
            N/A

        **Returns**
            N/A
        '''
        
        # Return the coordinate in the coordinate list corresponding to the
        # x, y position given.
        return self.coords[x * Board_Dim.COLS + y]
    

    def reset(self):
        '''
        This function rests all of the coordinates on the game board
        and clears their occupied values.
        
        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # For every coordinate space on the game board,
        for coord in self.coords:
            # Reset whether it is occupied to False to make it unoccupied.
            coord.occupied = False
