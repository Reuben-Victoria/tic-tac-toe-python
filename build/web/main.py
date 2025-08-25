import pygame
from game.settings import WIDTH, HEIGHT, load_fonts
from game.game_loop import run_game
import asyncio

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Load fonts
font, small_font = load_fonts()

# Load sounds
try:
    click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
    win_sound = pygame.mixer.Sound("assets/sounds/win.wav")
except:
    click_sound = win_sound = None

# Run game
asyncio.run(run_game(screen, font, small_font, click_sound, win_sound))
