import pygame

# Frames per second to be used for the game and window refresh rate.
FPS = 60

# Screen dimension constants.
class Screen_Dim:
    # Width of the window including both the game board and the info panel.
    WIDTH = 1150
    # Height of the window including both the game board and the info panel.
    HEIGHT = 690
    # Window size in tuple form.
    SCREEN_SIZE = (WIDTH, HEIGHT)

# Board dimension constants.
class Board_Dim:
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
    Colors to be used in the game in RGB values.
    
    Add more info about the Colors class here.
    '''
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (50, 180, 110)
    yellow = (255, 255, 50)
    purple = (255, 0, 255)
    teal = (0, 255, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    silver = (225, 225, 225)
    light_gray = (200, 200, 200)
    gray = (128, 128, 128)

class Icons:
    BOARD_WITH_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/quoridor_board_with_pawn.png'), (32,32))
    BLACK_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/pawn_black.png'), (40,40))
    BLUE_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/pawn_blue.png'), (40,40))
    GREEN_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/pawn_green.png'), (40,40))
    PURPLE_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/pawn_purple.png'), (40,40))
    RED_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/pawn_red.png'), (40,40))
    YELLOW_PAWN = pygame.transform.scale(pygame.image.load('src/32x32_Icons/pawn_yellow.png'), (40,40))