from tree import RGBXmasTree
from colorzero import Color, Hue
from random import randint

tree = RGBXmasTree(brightness=0.05)
colors = [Color('red'), Color('green'), Color('blue'), Color('orange'), Color('chocolate'), Color('yellow'),
          Color('cyan'), Color('magenta'), Color('purple'), Color('olive'), Color('navy'), Color('coral')]  # add more if you like
tree_colors = []

for pixel in tree:
    tree_colors.append(colors[randint(0, len(colors)- 1)])

tree_colors[3] = Color('cyan')
tree.value = tree_colors

while True:
    for i in range(len(tree_colors)):
        if i != 3:
            tree_colors[i] += Hue(deg=1)
    tree.value = tree_colors
