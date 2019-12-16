from tree import RGBXmasTree
from colorzero import Color, Hue

tree = RGBXmasTree(brightness=0.05)

tree.color = Color('red')

while True:
    tree.color += Hue(deg=1)
