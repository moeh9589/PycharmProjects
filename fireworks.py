import pygame
import random
import time
import numpy
import math

pygame.init()
pygame.font.init()

Width = 700
Height = 700

window = pygame.display.set_mode((Width, Height))

blue = (0, 0, 255)
white = (255, 255, 255)
red = (200, 0, 2)
black = (0, 0, 0)
green = (0, 205, 0)
light_red = (100, 0, 0)
yellow = (255, 255, 0)
bright_green = (0, 255, 0)
RB_red = (255, 0, 0)
RB_orange = (255, 165, 0)
RB_yellow = (255, 255, 0)
RB_green = (0, 128, 0)
RB_blue = (0, 0, 255)
RB_indigo = (75, 0, 130)
RB_violet = (238, 130, 238)


class Point:
    def __init__(self, x, y, vel_x, vel_y, color):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos
        return pos


def get_start():
    x = random.randrange(0, Width-100)
    y = random.randrange(0, Height-100)
    point = [x, y]
    return point


def update(x):
    x.pos[0] += x.vel_x
    x.pos[1] += x.vel_y


def choose_color():
    color = random.choice([blue, white, red, green, light_red, yellow, bright_green, RB_red, RB_orange,
                           RB_yellow, RB_green, RB_blue, RB_indigo, RB_violet])
    return color


def main():
    run = True
    arr = []
    point = get_start()

    for i in range(1000):
        v_x = random.uniform(-10, 10)
        v_y = random.uniform(-10, 10)
        v_x = v_x / 60.1
        v_y = v_y / 60.1
        p = Point(point[0], point[1], v_x, v_y, choose_color())
        arr.append(p)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(black)

        for n in range(5):

            for i in range(len(arr)):

                pygame.draw.circle(window, arr[i].color, (arr[i].x, arr[i].y), 2)
                arr[i].x += arr[i].vel_x
                arr[i].y += arr[i].vel_y

                if arr[i].x - point[0] > 360:
                    time.sleep(1)
                    main()
                elif arr[i].y - point[1] > 360:
                    time.sleep(1)
                    main()

            pygame.display.update()


main()
