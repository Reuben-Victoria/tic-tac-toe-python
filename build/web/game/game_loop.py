import pygame, sys
from .board import draw_board
from .utils import check_winner, reset_board, ai_move, is_draw
from .settings import WIDTH, HEIGHT, CELL_SIZE
import asyncio

async def run_game(screen, font, small_font, click_sound=None, win_sound=None):
    board = reset_board()
    current_player = "X"
    game_over = False
    winning_line = None

    while True:
        button_rect = draw_board(screen, board, font, small_font, winning_line, game_over)
        pygame.display.flip()
        await asyncio.sleep(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle click
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                if y < WIDTH:
                    row, col = y // CELL_SIZE, x // CELL_SIZE
                    if board[row][col] == "":
                        board[row][col] = current_player
                        if click_sound: click_sound.play()
                        winner, line = check_winner(board)
                        if winner:
                            winning_line, game_over = line, True
                            if win_sound: win_sound.play()
                        elif is_draw(board):
                            game_over = True
                        else:
                            current_player = "O"
                            move = ai_move(board)
                            if move:
                                r, c = move
                                board[r][c] = "O"
                                if click_sound: click_sound.play()
                            winner, line = check_winner(board)
                            if winner:
                                winning_line, game_over = line, True
                                if win_sound: win_sound.play()
                            elif is_draw(board):
                                game_over = True
                            else:
                                current_player = "X"

            # Restart button
            if event.type == pygame.MOUSEBUTTONDOWN and game_over and button_rect:
                if button_rect.collidepoint(event.pos):
                    board = reset_board()
                    current_player = "X"
                    game_over = False
                    winning_line = None
