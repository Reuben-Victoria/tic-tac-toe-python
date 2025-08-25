import pygame

# Window settings
WIDTH, HEIGHT = 300, 350
LINE_WIDTH = 5
CELL_SIZE = WIDTH // 3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)

def load_fonts():
    font = pygame.font.SysFont(None, 80)
    small_font = pygame.font.SysFont(None, 40)
    return font, small_font
