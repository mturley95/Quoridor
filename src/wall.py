# Import necessary libraries.
import pygame


class Wall:
    '''
    This class creates and controls a wall object that blocks player movement.
    
    Values:
        * coord1 (Coord: obj)
        * coord2 (Coord: obj)
        * coord3 (Coord: obj)
        * coord4 (Coord: obj)
        * orient (str)
        * cross_wall (Wall: obj)
        * win (Window: obj)
        * rect (tuple, int)
        * rect_small (tuple, int)
        * color (tuple, int)
        * info (tuple, obj)

    Functions:
        * __init__(self, width, height, square_size, wall_width, title, background_color)
        * set_color(self, new_color)
        * make_cross_wall(self)
        * make_rect(self)
        * make_rect_small(self)
        * draw(self, color)
        * __eq__(self, other)
    '''

    def __init__(self, coord1, coord2, win):
        '''
        This function initializes the Wall class.

        **Parameters**
            coord1: *Coord obj*
                The coordinate of the space adjacent to the wall space.
            coord2: *Coord obj*
                The coordinate of the space adjacent to the wall space on the other side.
            win: *Window obj*
                The window display object.

        **Returns**
            N/A
        '''

        # Set the piece spaces immediately adjacent to the wall space
        # that was selected to the first two coordinates.
        self.coord1 = coord1
        self.coord2 = coord2

        # If the piece spaces are in the same row of piece spaces on the grid,
        if coord1.same_row(coord2):
            # Set the other affected coordinates to be the spaces to the south
            # of the affected spaces.
            self.coord3 = coord1.south
            self.coord4 = coord2.south
            # Set the orientation of the wall with reference to the original space.
            self.orient = "e"
        
        # If the piece spaces are in the same column of piece spaces on the grid,
        if coord1.same_column(coord2):
            # Set the other affected coordinates to be the spaces to the east
            # of the affected spaces.
            self.coord3 = coord1.east
            self.coord4 = coord2.east
            # Set the orientation of the wall with reference to the original space.
            self.orient = "s"

        # Set a variable holder for the cross wall that will conflict with this wall if it is played.
        self.cross_wall = None
        # Set the window variable for the game window.
        self.win = win
        # Make the wall a rectangle shape.
        self.rect = self.make_rect()
        # Make the wall rectangle a small rectangle (as compared to the full wall length)
        # for mouse selection purposes.
        self.rect_small = self.make_rect_small()
        # Leave the color of the Wall rectangle clear upon initiation.
        self.color = None

        # Set info for the position and orientation of the wall.
        self.info = (coord1.x, coord1.y, self.orient)


    def set_color(self, new_color):
        '''
        This function updates the wall's color to a new color that is provided.

        **Parameters**
            new_color: *tuple: int* (int, int, int)
                (R, G, B):
                New color of the wall to be displayed.

        **Returns**
            N/A
        '''

        # Change the wall's color to a new color that is provided.
        self.color = new_color


    def make_cross_wall(self):
        '''
        This function sets the position of the cross wall that cannot be played with 
        the current wall because the walls would be crossing over one another and interfering.
        
        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # If the orientation of the wall was on the east of the original space,
        if self.orient == "e":
            # Set the cross_wall to be to the south of that space.
            self.cross_wall = self.coord1.wall_south

        # If the orientation of the wall was on the south of the original space,
        if self.orient == "s":
            # Set the cross wall to be to the east of that space.
            self.cross_wall = self.coord1.wall_east


    def make_rect(self):
        '''
        This function returns the rectangle corresponding to 
        the full-length wall on the window.

        **Parameters**
            N/A

        **Returns**
            wall_rectangle: *tuple: int* (int, int, int, int)
                (x_pos, y_pos, wall_width, wall_height):
                Returns the position and size of the wall rectangle space.
        '''

        # Bring in the current game window.
        win = self.win

        # Set the starting coordinate to be the top left of the space in question.
        (x, y) = self.coord1.top_left

        # If the wall is on the east of that coordinate space,
        if self.orient == "e":
            # Set the top left corner of the wall coordinate to be the 
            # top right corner of the original space.
            # Set the width to be the wall width and the height 
            # to stretch down to the blocks below the original space.
            return (x + win.square_size, y,
                    win.wall_width, 2*win.square_size + win.wall_width)
        
        # If the wall is on the south of that coordinate space,
        elif self.orient == "s":
            # Set the top left corner of the wall coordinate to be the 
            # bottom left corner of the original space.
            # Set the width to stretch over to the blocks on the right of the 
            # original space and the height to be the wall width.
            return (x, y + win.square_size,
                    2*win.square_size + win.wall_width, win.wall_width)
        return None


    def make_rect_small(self):
        '''
        This function returns the small rectangle corresponding to the portion of the wall 
        adjacent to the original coordinate space on the window.
        
        **Parameters**
            N/A

        **Returns**
            wall_rectangle_small: *tuple: int* (int, int, int, int)
                (x_pos, y_pos, wall_width, wall_height):
                Returns the position and size of the wall rectangle space
                that the player would select.
        '''

        # Bring in the current game window.
        win = self.win

        # Set the starting coordinate to be the top left of the space in question.
        (x, y) = self.coord1.top_left

        # If the wall is on the east of that coordinate space,
        if self.orient == "e":
            # Set the top left corner of the wall coordinate to be the 
            # top right corner of the original space.
            # Set the width to be the wall width and 
            # the height to stretch down the height of the original space.
            return (x + win.square_size, y, win.wall_width, win.square_size)
        
        # If the wall is on the south of that coordinate space,
        elif self.orient == "s":
            # Set the top left corner of the wall coordinate to be the 
            # bottom left corner of the original space.
            # Set the width to stretch over to the width of the original space 
            # and the height to be the wall width.
            return (x, y + win.square_size, win.square_size, win.wall_width)
        return None


    def draw(self, color):
        '''
        This function draws the wall on the window with the color of the player placing it.
        
        **Parameters**
            color: *tuple: int* (int, int, int)
                (R, G, B):
                Color of the wall to be displayed.

        **Returns**
            N/A
        '''

        # Draw the wall rectangle on the game window in the color of the player placing it.
        pygame.draw.rect(self.win.win, color, self.rect)


    def __eq__(self, other):
        '''
        Operator == for two walls.
        
        **Parameters**
            other: *Wall obj*
                Another wall object to be compared in positioning to the current wall object.

        **Returns**
            N/A
        '''
        # If the wall is positioned in the same place as another wall, return True.
        if (self.coord1 == other.coord1
            and self.coord2 == other.coord2
            and self.coord3 == other.coord3
            and self.coord4 == other.coord4):
            return True


class Walls:
    '''
    This class manages all the walls played.
    
    Values:
        * walls (list)
        * blocked_coords (dict)

    Functions:
        * __init__(self)
        * add_wall(self, wall)
        * draw(self)
        * contains(self, wall)
        * wall_in_walls(self, wall)
        * can_add(self, wall)
        * no_wall(self, coord1, coord2)
        * reset(self)
    '''

    def __init__(self):
        '''
        This function initializes the Walls class.

        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # Set a list of walls.
        self.walls = []

        # Set a dictionary of blocked coordinates.
        self.blocked_coords = {}


    def add_wall(self, wall):
        '''
        This function adds a wall to the game board grid and
        sets the blocked coordinates for the pieces.
        
        **Parameters**
            wall: *Wall obj*
                The wall that will be added to the grid.

        **Returns**
            N/A
        '''

        # Append the wall to the list of walls.
        self.walls.append(wall)

        # Assign d to the dictionary of blocked coordinates and 
        # add blocked moves for pieces related to their coordinate spaces.
        d = self.blocked_coords

        # If the wall starting coordinate space is not a key in the dictionary,
        if wall.coord1.pos not in d:
            # Add the coordinate space as a key and the second coordinate space as a value.
            d[wall.coord1.pos] = [wall.coord2.pos]
        # If the wall starting coordinate space is already a key in the dictionary,
        else:
            # Append the second coordinate space as a value to the key.
            d[wall.coord1.pos].append(wall.coord2.pos)

        # If the wall adjacent coordinate space is not a key in the dictionary,
        if wall.coord2.pos not in d:
            # Add the coordinate space as a key and the original coordinate space as a value.
            d[wall.coord2.pos] = [wall.coord1.pos]
        # If the wall adjacent coordinate space is already a key in the dictionary,
        else:
            # Append the original space as a value to the key.
            d[wall.coord2.pos].append(wall.coord1.pos)

        # If the wall adjacent coordinate space is not a key in the dictionary,
        if wall.coord3.pos not in d:
            # Add the coordinate space as a key and the its adjacent coordinate space as a value.
            d[wall.coord3.pos] = [wall.coord4.pos]
        # If the wall adjacent coordinate space is already a key in the dictionary,
        else:
            # Append the adjacent coordinate space as a value to the key.
            d[wall.coord3.pos].append(wall.coord4.pos)

        # If the wall adjacent coordinate space is not a key in the dictionary,
        if wall.coord4.pos not in d:
            # Add the coordinate space as a key and the its adjacent coordinate space as a value.
            d[wall.coord4.pos] = [wall.coord3.pos]
        # If the wall adjacent coordinate space is already a key in the dictionary,
        else:
            # Append the adjacent coordinate space as a value to the key.
            d[wall.coord4.pos].append(wall.coord3.pos)


    def draw(self):
        '''
        This function draws the played walls on the game board grid.
        
        **Parameters**
            N/A

        **Returns**
            N/A
        '''

        # Iterate through all played walls.
        for wall in self.walls:
            # Draw them on the game board in their player color.
            wall.draw(wall.color)


    def contains(self, wall):
        '''
        This function checks blocked coordinates dictionary to determine if
        the wall's location already exists on the game board.
        The function returns True if the wall location exists in the dictionary
        and False if it does not.

        **Parameters**
            wall: *Wall obj*
                The wall that will be added to the grid.

        **Returns**
            wall_location_in_dict: *bool*
                True if the wall location exists in the dictionary of blocked coordinates.
        '''

        # Assign d to the dictionary of blocked coordinates and 
        # check whether the new wall overlaps with any existing ones.
        d = self.blocked_coords

        # If the wall coordinate space is already in the dictionary,
        if wall.coord1.pos in d:
            # and if the value already exists for that coordinate space,
            if wall.coord2.pos in d[wall.coord1.pos]:
                # then the wall can't be played.
                return True
            
        # If the second wall coordinate space is already in the dictionary,
        if wall.coord3.pos in d:
            # and if the value already exists for that coordinate space,
            if wall.coord4.pos in d[wall.coord3.pos]:
                # then the wall can't be played.
                return True

        # If the wall coordinates are not in the dictionary, return False. 
        return False
    

    def wall_in_walls(self, wall):
        '''
        This function checks whether the wall to be played already exists on the game board.
        The function returns True if the wall exists in the list of played walls
        and False if it does not.
        Function used to compare a wall in question to cross-walls.

        **Parameters**
            wall: *Wall obj*
                The wall that will be added to the grid.

        **Returns**
            wall_in_list_of_walls: *bool*
                Returns True if the wall in question is in the list of walls.
        '''

        # Index through the list of walls.
        for w in self.walls:
            # Check if the wall in question is already in the list of walls.
            if wall == w:
                # If so, return True.
                return True
        # If the wall in question is not in the wall list, return False.
        return False

    def can_add(self, wall):
        '''
        This function checks whether a wall can be added to the game board and
        returns True if it can.

        **Parameters**
            wall: *Wall obj*
                The wall that will be added to the grid.

        **Returns**
            can_add: *bool*
                Returns True if the wall can be added.
        '''
        
        # Check whether the wall to-be-added already exists or
        # is a cross-wall to a wall that already exists.
        if not self.contains(wall) and not self.wall_in_walls(wall.cross_wall):
            return True
        

    def no_wall(self, coord1, coord2):
        '''
        This function checks whether there is a wall between two coordinates and 
        returns True is there is no wall between the two space.
        
        **Parameters**
            coord1: *Coord obj*
                The first coordinate to be used to check for a wall.
            coord2: *Coord obj*
                The second coordinate to be used to check for a wall.

        **Returns**
            no_wall: *bool*
                Returns True if there is no wall between two coordinates.
        '''

        # Assign d to the dictionary of blocked coordinates and 
        # check whether there is a wall between two coordinate spaces.
        d = self.blocked_coords

        # If the coordinate space is a key to the dictionary,
        if coord1.pos in d:
            # And the space to be moved to is not a value for that key,
            if coord2.pos not in d[coord1.pos]:
                # There is no wall in the way and the player can move.
                return True
            
            # If the space to be moved to is a value for that key,
            else:
                # There is a wall in the way and the player cannot move in that direction.
                return False
            
        # If the coordinate space is not a key to the dictionary,
        return True
    

    def reset(self):
        '''
        The function resets the walls on the game board 
        and the list and dictionary of walls.
        
        **Parameters**
            N/A

        **Returns**
            N/A
        '''
        
        # Index through all walls.
        for wall in self.walls:
            
            # Reset their colors to empty/clear.
            wall.color = None
        
        # Reset the list of walls.
        self.walls.clear()

        # Reset the list of blocked coordinates.
        self.blocked_coords.clear()
