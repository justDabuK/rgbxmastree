from tree import RGBXmasTree
from colorzero import Hue
from random import randint

tree = RGBXmasTree(brightness=0.05)

for pixel in tree:
    pixel.color = Hue(deg=randint(0, 360))

while True:
    for pixel in tree:
        pixel.color += Hue(deg=1)
