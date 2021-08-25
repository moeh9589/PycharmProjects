import itertools
from time import sleep
import pygame
import time
import numpy

pygame.init()
pygame.font.init()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = list(itertools.permutations(nums))
a = 0
b = 1
c = 2

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 245, 10)
Width = 700
Height = 800
window = pygame.display.set_mode((Width, Height))
my_font = pygame.font.SysFont("javanesetext", 65)
fps = 60
clock = pygame.time.Clock()


def check(a1, b1, c1):
    if a1 + c1 == b1:
        return True


def find_num_of_checks(n):
    times = len(n) // 2
    return times


def draw_board():
    for i in range(5):
        pygame.draw.circle(window, black, (i * 100+150, 300), 45, 5)
        pygame.display.update()

    for i in range(4):
        pygame.draw.circle(window, black, (i * 100+200, 400), 45, 5)
        pygame.display.update()


def main():
    run = True
    window.fill(red)
    
    def redraw_window():
        successes = 0
        total = 0
        number_font = pygame.font.SysFont("comicsans", 90)
        
        for i in x:
            if check(i[0], i[1], i[2]) and check(i[2], i[3], i[4]) and check(i[4], i[5], i[6]) and check(i[6], i[7],
                                                                                                         i[8]):
                window.fill(green)

                top_text = number_font.render(f"{i[0]}    {i[2]}    {i[4]}    {i[6]}   {i[8]}", 1, black)
                bottom_text = number_font.render(f"{i[1]}    {i[3]}    {i[5]}    {i[7]}", 1, black)
                window.blit(top_text, (135, 265))
                window.blit(bottom_text, (180, 370))

                draw_board()
                
                for j in range(5):
                    pygame.draw.circle(window, green, (j * 100 + 150, 300), 40)
                    
                for k in range(4):
                    pygame.draw.circle(window, green, (k * 100 + 150, 300), 40)
                    
                time.sleep(2)
                successes += 1
                total += 1
                window.fill(red)
                pygame.display.update()

            else:
                if i[0] != 9 and i[2] != 9 and i[4] != 9 and i[6] != 9 and i[8] != 9:
                    top_text = number_font.render(f"{i[0]}    {i[2]}    {i[4]}    {i[6]}   {i[8]}", 1, black)
                    bottom_text = number_font.render(f"{i[1]}    {i[3]}    {i[5]}    {i[7]}", 1, black)

                    window.blit(top_text, (135, 265))
                    window.blit(bottom_text, (180, 370))

                    draw_board()

                    for j in range(5):
                        pygame.draw.circle(window, white, (j * 100 + 150, 300), 40)
                    for k in range(4):
                        pygame.draw.circle(window, white, (k * 100 + 200, 400), 40)

                    total += 1
                    pygame.display.update()

    while run:
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            pygame.display.update()


def main_menu():
    running = True
    title_font = pygame.font.SysFont("javanesetext", 55)
    title_text = title_font.render("Math Problem Solver", 1, red)

    button_font = pygame.font.SysFont("comicsans", 50)
    button_text = button_font.render("SOLVE", 1, (255, 255, 255))

    bright_red = (240, 25, 0)

    rect_w = 200
    rect_x = Width / 2 - rect_w / 2
    rect_y = 600
    rect_h = 75

    window.fill(white)

    while running:

        window.blit(title_text, (Width / 2 - title_text.get_width() / 2, 200))

        mouse = pygame.mouse.get_pos()

        if rect_x + rect_w > mouse[0] > rect_x and rect_y + rect_h > mouse[1] > rect_y:
            pygame.draw.rect(window, red, (rect_x, rect_y, rect_w, rect_h), 0, 8)
            window.blit(button_text, (rect_x + 45, rect_y + 20))

        else:
            pygame.draw.rect(window, bright_red, (rect_x, rect_y, rect_w, rect_h), 0, 8)
            window.blit(button_text, (rect_x + 45, rect_y + 20))

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


main_menu()
