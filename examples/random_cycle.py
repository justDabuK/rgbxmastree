from tree import RGBXmasTree
from colorzero import Color, Hue
from random import randint

tree = RGBXmasTree(brightness=0.05)
colors = [Color('red'), Color('green'), Color('blue')]  # add more if you like
tree_colors = []

for pixel in tree:
    tree_colors.append(colors[randint(0, 2)])

tree.value = tree_colors

while True:
    for i in range(len(tree_colors)):
        tree_colors[i] += Hue(deg=1)
    tree.value = tree_colors
