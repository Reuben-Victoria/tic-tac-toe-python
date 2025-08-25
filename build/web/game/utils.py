import random

def check_winner(board):
    win_patterns = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for pattern in win_patterns:
        marks = [board[r][c] for r, c in pattern]
        if marks[0] != "" and marks.count(marks[0]) == 3:
            return marks[0], pattern
    return None, None

def is_draw(board):
    return all(board[r][c] != "" for r in range(3) for c in range(3))

def reset_board():
    return [["" for _ in range(3)] for _ in range(3)]

import random

def ai_move(board, ai="O", player="X"):
    def can_win(b, mark):
        for r in range(3):
            for c in range(3):
                if b[r][c] == "":
                    b[r][c] = mark
         
                    win = (
                        all(b[r][i] == mark for i in range(3)) or
                        all(b[i][c] == mark for i in range(3)) or
                        (r == c and all(b[i][i] == mark for i in range(3))) or
                        (r + c == 2 and all(b[i][2-i] == mark for i in range(3)))
                    )
                    b[r][c] = ""
                    if win:
                        return (r, c)
        return None


    win_move = can_win(board, ai)
    if win_move:
        return win_move

    block_move = can_win(board, player)
    if block_move:
        return block_move


    if board[1][1] == "":
        return (1, 1)


    corners = [(0,0), (0,2), (2,0), (2,2)]
    available_corners = [c for c in corners if board[c[0]][c[1]] == ""]
    if available_corners:
        return random.choice(available_corners)

    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    return random.choice(empty) if empty else None

