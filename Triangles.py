import pygame
import random
import time
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
gray = (52, 52, 52)
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
    def __init__(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos
        return pos


def midpoint(p, q):
    return 0.5*(p[0] + q[0]), 0.5*(p[1] + q[1])


def main():
    run = True
    window.fill(black)
    n = 10000

    p1 = Point((Width/2, 100))
    p2 = Point((100, 600))
    p3 = Point((600, 600))

    points = [p1, p2, p3]

    for i in range(1, n):
        k = random.randint(0, 2)
        x, y = midpoint(points[k].pos, points[i-1].pos)
        p = Point((x, y))
        points.append(p)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            pygame.display.update()

            for i in range(len(points)):
                if points[i].pos[0] < 171.42:
                    pygame.draw.circle(window, RB_red, points[i].pos, 1)
                    time.sleep(0.001)

                elif 171.42 < points[i].pos[0] < 242.84:
                    pygame.draw.circle(window, RB_orange, points[i].pos, 1)
                    time.sleep(0.001)

                elif 242.84 < points[i].pos[0] < 314.26:
                    pygame.draw.circle(window, RB_yellow, points[i].pos, 1)
                    time.sleep(0.001)

                elif 314.26 < points[i].pos[0] < 385.69:
                    pygame.draw.circle(window, RB_green, points[i].pos, 1)
                    time.sleep(0.001)

                elif 385.69 < points[i].pos[0] < 457.10:
                    pygame.draw.circle(window, RB_blue, points[i].pos, 1)
                    time.sleep(0.001)

                elif 457.10 < points[i].pos[0] < 528.53:
                    pygame.draw.circle(window, RB_indigo, points[i].pos, 1)
                    time.sleep(0.001)

                elif 528.53 < points[i].pos[0] < 600:
                    pygame.draw.circle(window, RB_violet, points[i].pos, 1)
                    time.sleep(0.001)

                pygame.display.update()


main()
