# Import necessary libraries.
import pygame


class Wall:
    '''
    Create a wall object that blocks player movement.
    
    Add more info about the class here.
    '''

    def __init__(self, coord1, coord2, win):
        '''
        Initialize the Wall class.
        
        Add more info about initialization parameters here.
        '''

        # Set the token spaces immediately adjacent to the wall space
        # that was selected to the first two coordinates.
        self.coord1 = coord1
        self.coord2 = coord2

        # If the token spaces are in the same row of token spaces on the grid,
        if coord1.same_row(coord2):
            # Set the other affected coordinates to be the spaces to the south
            # of the affected spaces.
            self.coord3 = coord1.south
            self.coord4 = coord2.south
            # Set the orientation of the wall with reference to the original space.
            self.orient = "e"
        
        # If the token spaces are in the same column of token spaces on the grid,
        if coord1.same_column(coord2):
            # Set the other affected coordinates to be the spaces to the east
            # of the affected spaces.
            self.coord3 = coord1.east
            self.coord4 = coord2.east
            # Set the orientation of the wall with reference to the original space.
            self.orient = "s"

        self.cross_wall = None

        # Window attributes.
        self.win = win
        # Make the wall a rectangle shape.
        self.rect = self.make_rect()
        # Make the wall rectangle a small rectangle (as compared to a token space).
        self.rect_small = self.make_rect_small()
        # Leave the color of the Wall rectangle clear.
        '''Check to see why this couldn't be gray for when the user hovers over.'''
        self.color = None

        # Set info for the position and orientation of the wall.
        self.info = (coord1.x, coord1.y, self.orient)

    def __str__(self):
        '''
        Defines what is returned when "str()" of the Wall class is called.
        
        Add more info about the class here.
        '''
        # Determine whether this function is still needed.
        return ", ".join([str(self.coord1), str(self.coord2),
                         str(self.coord3), str(self.coord4), self.orient])

    def set_color(self, new_color):
        '''
        Set the wall's color.
        
        Add more info about this function's parameters here.
        '''
        self.color = new_color

    def make_cross_wall(self):
        '''
        Return the cross wall that cannot be played if this wall is played
        because the walls would be crossing over one another and interfering.
        
        Add more info about this function's parameters here.
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
        Return the rectangle corresponding to the full-length wall on the window.

        Add more info about this function's parameters here.
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
        Return the small rectangle corresponding to the portion of the wall 
        adjacent to the original coordinate space on the window.
        
        Add more info about this function's parameters here.
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
        Draw the wall on the window with the color of the player placing it.
        
        Add more info about this function's parameters here.
        '''
        pygame.draw.rect(self.win.win, color, self.rect)

    def __eq__(self, other):
        '''
        Operator == for two walls.
        
        Add more info about this function's parameters here.
        '''
        # If the wall is positioned in the same place as another wall, return True.
        if (self.coord1 == other.coord1
            and self.coord2 == other.coord2
            and self.coord3 == other.coord3
            and self.coord4 == other.coord4):
            return True


class Walls:
    '''
    Manage all the walls played.
    
    Add more info about the Wall class here.
    '''

    def __init__(self):
        '''
        Initiate the Walls class.
        
        Add more info about initialization parameters here.
        '''

        # Set a list of walls.
        self.walls = []

        # Set a dictionary of blocked coordinates.
        self.blocked_coords = {}

    def add_wall(self, wall):
        '''
        Add a wall to the grid.
        
        Add more info about this function's parameters here.
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
        Draw the walls on the game board grid.
        
        Add more info about this function's parameters here.
        '''

        # Iterate through all played walls.
        for w in self.walls:
            # Draw them on the game board in their player color.
            w.draw(w.color)

    def contains(self, wall):
        '''
        Return True if wall can't be added.

        Add more info about this function's parameters here.
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
            
        return False

    def wall_in_walls(self, wall):
        '''
        Return True if the wall is in walls.
        Used to compare whether a prospective wall's cross-wall already has been played.
        
        Add more info about this function's parameters here.
        '''

        # Index through all played walls
        for w in self.walls:
            # Check if the wall in question is already in the list of played walls.
            if wall == w:
                # If so, return True.
                return True
        return False

    def can_add(self, wall):
        '''
        Return True if the wall can be added.
        
        Add more info about this function's parameters here.
        '''
        
        # Check whether the wall to-be-added already exists or
        # is a cross-wall to a wall that already exists.
        if not self.contains(wall) and not self.wall_in_walls(wall.cross_wall):
            return True

    def no_wall(self, coord1, coord2):
        '''
        Return True is there is no wall between two positions.
        
        Add more info about this function's parameters here.
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
        Reset the walls.
        
        Add more info about this function's parameters here.
        '''
        
        # Index through all walls.
        for w in self.walls:
            
            # Reset their colors to empty/clear.
            w.color = None
        
        # Reset the list of walls.
        self.walls.clear()

        # Reset the list of blocked coordinates.
        self.blocked_coords.clear()
