# Import necessary libraries.
import pygame
from const import Colors


class Text:
    '''
    Creates a text box object that can be displayed.
    
    Add more details about class parameters here.
    '''
    
    # Create a list of all instances of text objects being made.
    instances = []

    def __init__(self, text, pos, color, size=30, font="Arial", show = True):
        '''
        Initializes the Text class.
        
        Add more info about initialization parameters here.
        '''
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

    def draw(self, win, pos):
        '''
        Draw the text on the window.
        
        Add more info about draw function parameters here.
        '''

        # Set font and size based on input parameters.
        font = pygame.font.SysFont(self.font, self.size)
        # Render the text in the font and color selected.
        text = font.render(self.text, 1, self.color, None)

        # Draw the text object onto the window at the proper position.
        win.blit(text, pos)

    def set_show(self, new_show_value):
        '''
        Function that changes whether the text will display on the window or not.
        
        Add more info about function parameters here.
        '''
        self.show = new_show_value


class Button:
    '''
    Creates a button object that can be displayed and clicked on.
    
    Add more details about class parameters here.
    '''

    # Create a list of all instances of text objects being made.
    instances = []

    def __init__(self, text, x, y, color, width=100, height=40, \
                 selected = False, show = True):
        '''
        Initializes the Button class.
        
        Add more info about initialization parameters here.
        '''
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
        Draw the button on the window.
        
        Add more info about initialization parameters here.
        '''

        # Sets the button to be rectangle of the size and color input.
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))
        
        # Set the button font and size.
        font = pygame.font.SysFont("comicsans", 40)
        # Render the text in the font and color selected.
        text = font.render(self.text, 1, Colors.black)

        # Draw the text object onto the window at the proper position.
        win.blit(text,
                 (self.x + round(self.width/2) - round(text.get_width()/2),
                  self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        '''
        Return True if pos is in the button rectangle.
        
        Add more info about initialization parameters here.
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
        Function that changes whether the button will display on the window or not.
        
        Add more info about function parameters here.
        '''
        self.show = new_show_value
    
    def set_color(self, new_color):
        '''
        Function that changes the button color when it displays on the window.
        
        Add more info about function parameters here.
        '''
        self.color = new_color

    def set_text(self, new_text_value):
        '''
        Function that changes the button text when it displays on the window.
        
        Add more info about function parameters here.
        '''
        self.text = new_text_value

    def set_selected(self, new_selected_value):
        '''
        Function that changes whether the button functions as a selected button.
        It also updates the text and color of the button as-needed.
        
        Add more info about function parameters here.
        '''
        self.selected = new_selected_value

        # If the button is selected,
        if self.selected == True:
            # Set the button color to blue.
            self.set_color(Colors.blue)

            # If the button is for human/bot:
            if self.text == "H":
                # Change the text value.
                self.set_text("B")
        else:
            # If the button is not selected.
            # Set the colot to red.
            self.set_color(Colors.red)

            # If the button is for human/bot:
            if self.text == "B":
                # Change the text value.
                self.set_text("H")
