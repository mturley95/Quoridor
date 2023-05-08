# Import necessary libraries.
import pygame
from src.const import Colors


class Text:
    '''
    This class creates a Text object that can be displayed on the GUI.
    
    Values:
        * instances (list)
        * text (str)
        * pos (tuple: int)
        * x (int)
        * y (int)
        * color (tuple: int)
        * size (int)
        * font (str)
        * show (bool)

    Functions:
        * __init__(self, text, pos, color, size, font, show)
        * draw(self, win)
        * set_show(self, new_show_value)
    '''
    
    # Create a list of all instances of text objects being made.
    instances = []

    def __init__(self, text, pos, color, size = 30, font = "Arial", show = True):
        '''
       This function initializes the Text class.

        **Parameters**
            text: *str*
                The string of text that will be displayed on the window.
            pos: *tuple: int*
                The position on the window to place the text.
            color *tuple: int*
                The color of the text to be displayed on the window.
            size *int*
                The size of the text to be displayed on the window.
            font *str*
                The font of the text to be displayed on the window.
            show *bool*
                Sets whether the text box object is showing on the window or not.

        **Returns**
            N/A
        '''

        # Assign all variables to the class.
        self.text = text
        self.pos = pos
        # Get x and y values from the input position.
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.size = size
        self.font = font
        self.show = show

        # For each text object that is initialized, 
        # add it to the list of text objects.
        Text.instances.append(self)


    def draw(self, win):
        '''
        This function draws the text object onto the game window display.
        
        **Parameters**
            win: *Window obj*
                The game display window object for the text to appear on.

        **Returns**
            N/A
        '''

        # Set font and size based on input parameters.
        font = pygame.font.SysFont(self.font, self.size)
        # Render the text in the font and color selected.
        text = font.render(self.text, 1, self.color, Colors.SILVER)

        # Draw the text object onto the window at the proper position.
        win.blit(text, self.pos)


    def set_show(self, new_show_value):
        '''
        This function changes whether the text will display on the window or not.
        
        **Parameters**
            new_show_value: *bool*
                True if the text should be displayed, False if not.

        **Returns**
            N/A
        '''

        # Set the show boolean to the assigned new value.
        self.show = new_show_value


class Button:
    '''
    This class creates a Button object that can be displayed on the GUI.
    
    Values:
        * instances (list)
        * text (str)
        * x (int)
        * y (int)
        * color (tuple: int)
        * width (int)
        * height (int)
        * selected (bool)
        * show (bool)

    Functions:
        * __init__(self, text, x, y, color, width, height, selected, show)
        * draw(self, win)
        * click(self, pos)
        * set_show(self, new_show_value)
        * set_color(self, new_color)
        * set_text(self, new_text_value)
        * set_selected(self, new_selected_value)
    '''

    # Create a list of all instances of text objects being made.
    instances = []

    def __init__(self, text, x, y, color, width = 100, height = 40, \
                 selected = False, show = True):
        '''
        This function initializes the Button class.

        **Parameters**
            text: *str*
                The string of text that will be displayed in the button on the window.
            x: *int*
                The x-coordinate for the button position.
            y *int*
                The y-coordinate for the button position.
            color *tuple: int*
                The color of the button to be displayed on the window.
            width *int*
                The width of the button.
            height *int*
                The height of the button.
            selected *bool*
                Sets whether the button is selected or not.
            show *bool*
                Sets whether the button is showing on the window or not.

        **Returns**
            N/A
        '''

        # Assign all variables to the class.
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.show = show
        self.selected = selected

        # For each button object that is initialized, 
        # add it to the list of button objects.
        Button.instances.append(self)


    def draw(self, win):
        '''
        This function draws the button object onto the game window display.
        
        **Parameters**
            win: *Window obj*
                The game display window object for the text to appear on.

        **Returns**
            N/A
        '''

        # Sets the button to be rectangle of the size and color input.
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))
        
        # Set the button font and size.
        font = pygame.font.SysFont("comicsans", 40)
        # Render the text in the font and color selected.
        text = font.render(self.text, 1, Colors.BLACK)

        # Draw the text object onto the window at the proper position.
        win.blit(text,
                 (self.x + round(self.width/2) - round(text.get_width()/2),
                  self.y + round(self.height/2) - round(text.get_height()/2)))


    def click_on_button(self, pos):
        '''
        The function returns True if position that the mouse clicked on
        is within the button object.
        
        *Parameters**
            pos: *tuple: int* (int, int)
                The position that the mouse clicked on.

        **Returns**
            click_on_button: *bool*
                Returns True if the mouse click was on the button object.
        '''

        # Separate out x and y coordinates based on input position.
        pos_x, pos_y = pos
        
        # Checks to see if input position was within the button area.
        if (self.x <= pos_x and pos_x <= self.x + self.width 
        and self.y <= pos_y and pos_y <= self.y + self.height) == True:
            # If so, return True
            return True


    def set_show(self, new_show_value):
        '''
        This function changes whether the button will display on the window or not.
        
        **Parameters**
            new_show_value: *bool*
                True if the text should be displayed, False if not.

        **Returns**
            N/A
        '''

        # Set the show boolean to the assigned new value.
        self.show = new_show_value


    def set_color(self, new_color):
        '''
        This function changes the color of the button when it is displayed on the window.
        
        **Parameters**
            new_color: *tuple: int* (int, int, int)
                The new color to display for the button.

        **Returns**
            N/A
        '''
        
        # Set the button color to the assigned new color.
        self.color = new_color


    def set_text(self, new_text_value):
        '''
        This function changes the button text when it displays on the window.
        
        **Parameters**
            new_text_value: *str*
                The new text to display on the button.

        **Returns**
            N/A
        '''

        # Set the button text to the assigned new text.
        self.text = new_text_value


    def set_selected(self, new_selected_value):
        '''
        This function sets the selected value of the Button.
        It also updates the text and color of the button as-needed.

        **Parameters**
            new_selected_value: *bool*
                True if the button is selected and False if it is not.

        **Returns**
            N/A
        '''

        # Set the button selected value to the assigned new value.
        self.selected = new_selected_value

        # If the button is selected,
        if self.selected == True:
            # Set the button color to blue.
            self.set_color(Colors.BLUE)

            # If the button is for human/bot:
            if self.text == "H":
                # Change the text value.
                self.set_text("B")
        else:
            # If the button is not selected.
            # Set the colot to red.
            self.set_color(Colors.RED)

            # If the button is for human/bot:
            if self.text == "B":
                # Change the text value.
                self.set_text("H")
