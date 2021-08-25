import pygame
import numpy
import math
import time

blue = (0, 0, 255)
white = (255, 255, 255)
red = (200, 0, 2)
black = (0, 0, 0)
green = (0, 205, 0)
light_red = (100, 0, 0)
gray = (52, 52, 52)
yellow = (255, 255, 0)
bright_green = (0, 255, 0)

pygame.init()
pygame.font.init()

Width = 600
Height = 700
rows = 3
cols = 3
window = pygame.display.set_mode((Width, Height))

n = 200


def init_board():
    board = numpy.zeros((rows, cols))
    return board


def play_piece(board, row, col, piece):
    board[row][col] = piece


def check(board, row, col):
    return board[row][col] == 0


def get_row(board, col):
    for r in range(rows):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(board)


def full_board(board):
    for c in range(3):
        for r in range(3):
            if board[r][c] != 0:
                return True


def winning(board, piece):
    for c in range(cols-2):
        for r in range(rows):
            if board[r][c] == piece and board[r][c+1] == piece \
                    and board[r][c+2] == piece:
                pygame.draw.line(window, black, (50,50), (250,250), 5)

                return True

    for c in range(cols):
        for r in range(rows-2):
            if board[r][c] == piece and board[r+1][c] == piece \
                    and board[r+2][c] == piece:
                pygame.draw.line(window, black, (50,50), (250,250), 5)

                return True

    for c in range(cols-2):
        for r in range(rows-2):
            if board[r][c] == piece and board[r+1][c+1] == piece \
                    and board[r+2][c+2] == piece:
                pygame.draw.line(window, black, (50,50), (250,250), 5)

                return True

    for c in range(cols-2):
        for r in range(2, rows):
            if board[r][c] == piece and board[r-1][c+1] == piece \
                    and board[r-2][c+2] == piece:
                pygame.draw.line(window, black, (50,50), (250,250), 5)
                return True


def draw_board(board):
    for c in range(cols):
        for r in range(rows):
            pygame.draw.rect(window, black, (c*n, r*n, n, n))
            pygame.draw.rect(window, white, (c*n, r*n, n-5, n-5))

    for c in range(cols):
        for r in range(rows):
            if board[r][c] == 1:
                pygame.draw.line(window, red, (c*n+23, r*n+25), (c*n+n-23, r*n+n-25), 10)
                pygame.draw.line(window, red, (c*n+23, r*n+175), (c*n+n-23, r*n+25), 10)

                # pygame.draw.circle(window, red, (c*n+n/2, r*n+n/2), n/4)

            elif board[r][c] == 2:
                pygame.draw.circle(window, blue, (c*n+n/2, r*n+n/2), n/3, width=5)

    # pygame.draw.line(window, black, (int(Width/3), int(Height/3)-n), (int(Width/3), int(Width-Width/3)+n))
    # pygame.draw.line(window, black, (int(Width-Width/3), int(Height/3)-n), (int(Width-Width/3), int(Width-Width/3)+n))
    # pygame.draw.line(window, black, (int(Width/3-n), int(Width/3)), (int(Width-Width/3+n), int(Width/3)))
    # pygame.draw.line(window, black, (int(Width/3-n), int(Height/3)+n), (int(Width-Width/3+n), int(Width-Width/3)))

    pygame.display.update()


def main():
    moves = 0
    turn = 0
    run = True
    window.fill(white)
    board = init_board()
    pygame.display.update()
    draw_board(board)

    my_font = pygame.font.SysFont("javanesetext", 75)

    turn_text = my_font.render(f"Player {turn+1}'s turn", 1, red)
    turn2_text = my_font.render("Player 2's turn", 1, red)
    pygame.draw.rect(window, black, (0, 600, Width, n/2))

    window.blit(turn_text, (Width / 2 - turn_text.get_width() / 2, 580))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x = event.pos[0]
                pos_y = event.pos[1]
                col = int(math.floor(pos_x / n))
                row = int(math.floor(pos_y / n))

                # print(pos_x, pos_y, col, row)

                if check(board, row, col):
                    pygame.draw.rect(window, black, (0, 600, Width, n/2))

                    if not winning(board, 2):
                        window.blit(turn2_text, (Width / 2 - turn2_text.get_width() / 2, 580))

                    if turn == 0:
                        play_piece(board, row, col, 1)

                        if winning(board, 1):
                            win_text = my_font.render("Player 1 wins!!", 1, red)
                            pygame.draw.rect(window, black, (0, 600, Width, n/2))
                            window.blit(win_text, (Width / 2 - win_text.get_width() / 2, 580))
                            pygame.draw.circle(window, bright_green, (200, 200), 50)

                            run = False


                    elif turn == 1:
                        pygame.draw.rect(window, black, (0, 600, Width, n/2))

                        if not winning(board, 1):
                            window.blit(turn_text, (Width / 2 - turn_text.get_width() / 2, 580))

                        if check(board, row, col):
                            play_piece(board, row, col, 2)

                            if winning(board, 2):
                                pygame.draw.circle(window, bright_green, (200, 200), 50)
                                pygame.draw.line(window, black, (row*n, col*n), (row*n, col*n + n), 5)
                                win_text = my_font.render("Player 2 wins!!", 1, red)
                                pygame.draw.rect(window, black, (0, 600, Width, n/2))
                                window.blit(win_text, (Width / 2 - win_text.get_width() / 2, 580))
                                pygame.draw.circle(window, bright_green, (200, 200), 50)

                                run = False

                    print_board(board)
                    print(len(board))
                    draw_board(board)

                    turn += 1
                    turn = turn % 2
                    moves += 1

                    if moves == 9:
                        run = False

                if not run:
                    time.sleep(3)
                    main()


main()
