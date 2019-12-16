from tree import RGBXmasTree
from colorzero import Hue
from random import random


def random_color():
    r = random()
    g = random()
    b = random()
    return r, g, b


def random_colors(n):
    return [random_color() for i in range(n)]


tree = RGBXmasTree(brightness=0.05)

tree.value = random_colors(25)

while True:
    tree.color += Hue(deg=1)
