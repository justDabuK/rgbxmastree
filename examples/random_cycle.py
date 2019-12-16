from tree import RGBXmasTree
from colorzero import Color, Hue
from random import randint

tree = RGBXmasTree(brightness=0.05)
colors = [Color('red'), Color('green'), Color('blue')]  # add more if you like
tree_colors = []

for pixel in tree:
    tree_colors = colors[randint(0, 2)]

tree.value = tree_colors

while True:
    for pixel in tree_colors:
        pixel += Hue(deg=1)
    tree.value = tree_colors
