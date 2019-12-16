from tree import RGBXmasTree
from colorzero import Color, Hue
from random import randint

tree = RGBXmasTree(brightness=0.05)
colors = [Color('red'), Color('green'), Color('blue')]  # add more if you like

for pixel in tree:
    pixel.color = colors[randint(0, 2)]

while True:
    for pixel in tree:
        pixel.color += Hue(deg=1)
