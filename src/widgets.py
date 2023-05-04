import pygame
from const import Colors


class Text:
    """Create a text box"""
    
    instances = []

    def __init__(self, text, pos, color, size=30, font="Arial", show = True):
        self.text = text
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.size = size
        self.font = font
        self.show = show
        Text.instances.append(self)

    def draw(self, win, pos):
        """Draw the text on the window"""
        font = pygame.font.SysFont(self.font, self.size)
        text = font.render(self.text, 1, self.color, None)
        win.blit(text, pos)

    def set_show(self, new_show_value):
        self.show = new_show_value


class Button:
    """Create a button"""

    instances = []

    def __init__(self, text, x, y, color, width=100, height=40, show = True):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.show = show
        Button.instances.append(self)

    def draw(self, win):
        """Draw the button on the window"""
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, Colors.black)
        win.blit(text,
                 (self.x + round(self.width/2) - round(text.get_width()/2),
                  self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        """Return True if pos is in the button rectangle"""
        pos_x, pos_y = pos
        return (self.x <= pos_x <= self.x + self.width
                and self.y <= pos_y <= self.y + self.height)
    
    def set_show(self, new_show_value):
        self.show = new_show_value
    
    def set_color(self, new_color):
        self.color = new_color

