from tkinter import *

canvas_width = 1000
canvas_height = 500

boxx = []

for ratio in (0.2, 0.35):
    boxx.append((canvas_width * ratio, canvas_height * ratio, canvas_width * (1 - ratio), canvas_height * (1 - ratio)))

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()
