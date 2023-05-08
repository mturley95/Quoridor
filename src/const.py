import pygame

# Frames per second to be used for the game and window refresh rate.
FPS = 60


class Screen_Dim:
    '''
    This class holds all of the screen dimension constants.
    
    Values:
        * WIDTH (int)
        * HEIGHT (int)

    Functions:
        N/A
    '''
    # Width of the window including both the game board and the info panel.
    WIDTH = 1150
    # Height of the window including both the game board and the info panel.
    HEIGHT = 690


class Board_Dim:
    '''
    This class holds all of the screen dimension constants.
    
    Values:
        * COLS (int)
        * ROWS (int)
        * SQUARE_SIZE (int)
        * WALL_WIDTH (int)

    Functions:
        N/A
    '''
        
    # Total number of columns.
    COLS = 9
    # Total number of rows.
    ROWS = 9
    # Square size in pixels.
    SQUARE_SIZE = 50
    # Wall width in pixels.
    WALL_WIDTH = 10


class Colors:
    '''
    This class holds all of the colors that will be displayed on the game window.
    
    Values:
        * red (tuple)
        * blue (tuple)
        * green (tuple)
        * yellow (tuple)
        * purple (tuple)
        * white (tuple)
        * black (tuple)
        * silver (tuple)
        * light_gray (tuple)
        * gray (tuple)

    Functions:
        N/A
    '''

    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (50, 180, 110)
    yellow = (255, 255, 50)
    purple = (255, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    silver = (225, 225, 225)
    light_gray = (200, 200, 200)
    gray = (128, 128, 128)


class Icons:
    '''
    This class holds all of the icons used for the game display.
    
    Values:
        * BOARD_WITH_PAWN (Pygame obj .png)
        * BLUE_PAWN (Pygame obj .png)
        * GREEN_PAWN (Pygame obj.png)
        * RED_PAWN (Pygame obj.png)
        * YELLOW_PAWN (Pygame obj.png)

    Functions:
        N/A
    '''
        
    BOARD_WITH_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/quoridor_board_with_pawn.png'), (32,32))
    BLUE_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/pawn_blue.png'), (40,40))
    GREEN_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/pawn_green.png'), (40,40))
    RED_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/pawn_red.png'), (40,40))
    YELLOW_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/pawn_yellow.png'), (40,40))