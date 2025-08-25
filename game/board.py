import pygame
from .settings import WIDTH, HEIGHT, CELL_SIZE, WHITE, BLACK, RED, BLUE, GREEN

def draw_board(screen, board, font, small_font, winning_line, game_over):
    screen.fill(WHITE)
    # Grid
    pygame.draw.line(screen, BLACK, (CELL_SIZE, 0), (CELL_SIZE, WIDTH), 5)
    pygame.draw.line(screen, BLACK, (CELL_SIZE*2, 0), (CELL_SIZE*2, WIDTH), 5)
    pygame.draw.line(screen, BLACK, (0, CELL_SIZE), (WIDTH, CELL_SIZE), 5)
    pygame.draw.line(screen, BLACK, (0, CELL_SIZE*2), (WIDTH, CELL_SIZE*2), 5)

    # Marks
    for r in range(3):
        for c in range(3):
            mark = board[r][c]
            if mark:
                color = RED if mark == "X" else BLUE
                text = font.render(mark, True, color)
                rect = text.get_rect(center=(c*CELL_SIZE + CELL_SIZE//2,
                                             r*CELL_SIZE + CELL_SIZE//2))
                screen.blit(text, rect)

    # Winning line
    if winning_line:
        first, last = winning_line[0], winning_line[-1]
        start_pos = (first[1]*CELL_SIZE + CELL_SIZE//2, first[0]*CELL_SIZE + CELL_SIZE//2)
        end_pos = (last[1]*CELL_SIZE + CELL_SIZE//2, last[0]*CELL_SIZE + CELL_SIZE//2)
        pygame.draw.line(screen, GREEN, start_pos, end_pos, 6)

    # Restart button
    if game_over:
        button_rect = pygame.Rect(WIDTH//2 - 60, WIDTH + 10, 120, 30)
        pygame.draw.rect(screen, (180, 180, 180), button_rect)
        text = small_font.render("Restart", True, BLACK)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)
        return button_rect
    return None
