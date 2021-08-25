import pygame
import time
import random
import math
import numpy

pygame.init()
pygame.font.init()

rows = 7
cols = 7

blue = (0, 0, 255)
white = (255, 255, 255)
red = (200, 0, 2)
black = (0, 0, 0)
green = (0, 205, 0)
light_red = (100, 0, 0)
gray = (52, 52, 52)
yellow = (255, 255, 0)
bright_green = (0, 255, 0)

Width = 700
Height = 800
window = pygame.display.set_mode((Width, Height))


def init_board():
    board = numpy.zeros((rows, cols))
    return board


def play_piece(board, row, col, piece):
    board[row][col] = piece


def check(board, col):
    return board[rows-1][col] == 0


def get_row(board, col):
    for r in range(rows):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(numpy.flip(board, 0))


def winning(board, piece):
    for c in range(cols-3):
        for r in range(rows):
            if board[r][c] == piece and board[r][c+1] == piece \
                    and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    for c in range(cols):
        for r in range(rows-3):
            if board[r][c] == piece and board[r+1][c] == piece \
                    and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    for c in range(cols-3):
        for r in range(rows-3):
            if board[r][c] == piece and board[r+1][c+1] == piece \
                    and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    for c in range(cols-3):
        for r in range(3, rows):
            if board[r][c] == piece and board[r-1][c+1] == piece \
                    and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def draw_board(board):
    for c in range(cols):
        for r in range(rows):
            pygame.draw.rect(window, red, (c*100, r*100+100, 100, 100))
            pygame.draw.circle(window, black, (c*100+50, r*100+150), 45)
            pygame.draw.circle(window, light_red, (c*100+50, r*100+150), 47, 5)

    for c in range(cols):
        for r in range(rows):
            if board[r][c] == 1:
                pygame.draw.circle(window, white, (c*100+50, Height-r*100-50), 46, 5)
                pygame.draw.circle(window, green, (c*100+50, Height-r*100-50), 43)

            elif board[r][c] == 2:
                pygame.draw.circle(window, white, (c*100+50, Height-r*100-50), 46, 5)
                pygame.draw.circle(window, blue, (c*100+50, Height-r*100-50), 43)
    pygame.display.update()


def main_menu():
    running = True
    title_font = pygame.font.SysFont("javanesetext", 55)
    title_text = title_font.render("Justin's Connect 4", 1, (255, 0, 0))

    button_font = pygame.font.SysFont("comicsans", 50)
    button_text = button_font.render("PLAY", 1, white)

    rect_w = 200
    rect_x = Width / 2 - rect_w / 2
    rect_y = 600
    rect_h = 75

    pieces = []

    for p in range(70):
        star_loc_x = random.randrange(50, Width+100, int(Width/7))
        star_loc_y = random.randrange(0, Height, int(Height/7))
        star_color = random.choice([yellow, blue, red, green, bright_green])

        pieces.append([star_loc_x, star_loc_y, star_color])  # i love your balls

    while running:
        window.fill(black)

        for piece in pieces:
            piece[1] += 1*.2

            if piece[1] > Height+50:
                piece[0] = random.randrange(50, Width+100, int(Width/7))
                piece[1] = random.randrange(-Height+50, -100, int(Height/7))

            color = piece[2]
            pygame.draw.circle(window, white, (piece[0], piece[1]), 47, 5)
            pygame.draw.circle(window, color, (piece[0], piece[1]), 44)

        r_x = Width/2-title_text.get_width()/2-25
        r_y = 170
        r_w = title_text.get_width()+50
        r_h = title_text.get_height()+50

        pygame.draw.rect(window, black, (r_x, r_y, r_w, r_h))
        pygame.draw.rect(window, white, (r_x, r_y, r_w, r_h), width=2)

        window.blit(title_text, (Width/2 - title_text.get_width()/2, 200))

        mouse = pygame.mouse.get_pos()

        if rect_x + rect_w > mouse[0] > rect_x and rect_y + rect_h > mouse[1] > rect_y:
            pygame.draw.rect(window, gray, (rect_x, rect_y, rect_w, rect_h))
            pygame.draw.rect(window, white, (rect_x, rect_y, rect_w, rect_h), 3)

            window.blit(button_text, (rect_x + 55, rect_y + 20))

        else:
            pygame.draw.rect(window, black, (rect_x, rect_y, rect_w, rect_h))
            pygame.draw.rect(window, white, (rect_x, rect_y, rect_w, rect_h), 3)

            window.blit(button_text, (rect_x + 55, rect_y + 20))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN and \
                    (rect_x + rect_w > mouse[0] > rect_x and rect_y + rect_h > mouse[1] > rect_y):
                main()

    pygame.quit()


def main():
    window.fill(black)
    board = init_board()
    print_board(board)

    my_font = pygame.font.SysFont("javanesetext", 75)

    draw_board(board)

    run = True
    turn = 0

    turn_text = my_font.render(f"Player {turn+1}'s turn", 1, red)
    turn2_text = my_font.render("Player 2's turn", 1, red)

    window.blit(turn_text, (Width / 2 - turn_text.get_width() / 2, 0))

    pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos[0]
                col = int(math.floor(pos / 100))

                if check(board, col):
                    pygame.draw.rect(window, black, (0, 0, Width, 100))

                    if not winning(board, 2):
                        window.blit(turn2_text, (Width / 2 - turn2_text.get_width() / 2, 0))

                    if turn == 0:
                        row = get_row(board, col)
                        play_piece(board, row, col, 1)

                        if winning(board, 1):
                            print(f"Player {turn-1} won")

                            win_text = my_font.render("Player 1 wins!!", 1, red)
                            pygame.draw.rect(window, black, (0, 0, Width, 100))
                            window.blit(win_text, (Width/2-win_text.get_width()/2, 0))
                            run = False

                    elif turn == 1:
                        pygame.draw.rect(window, black, (0, 0, Width, 100))

                        if not winning(board, 1):
                            window.blit(turn_text, (Width / 2 - turn_text.get_width() / 2, 0))
                        if check(board, col):
                            row = get_row(board, col)
                            play_piece(board, row, col, 2)

                            if winning(board, 2):
                                print(f"Player {turn - 1} won")
                                win_text = my_font.render("Player 2 wins!!", 1, red)
                                pygame.draw.rect(window, black, (0, 0, Width, 100))
                                window.blit(win_text, (Width/2-win_text.get_width()/2, 0))
                                run = False

                    print_board(board)
                    draw_board(board)

                    turn += 1
                    turn = turn % 2

                if not run:
                    time.sleep(3)


main_menu()
