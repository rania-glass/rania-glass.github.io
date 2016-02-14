import os
from os.path import isfile
from PIL import Image


abspath = os.path.abspath(__file__)
basepath = os.path.basename(__file__)

abspath = abspath[:-len(basepath)]
imgpath = abspath + "images"
files = os.listdir(imgpath)
grayscaledir = imgpath + "\grayscaled"
if not os.path.exists(grayscaledir):
    os.mkdir(grayscaledir)

for item in files:
    if isfile(imgpath + "\\" + item):
        im = Image.open(imgpath + "\\" + item).convert('L')
        im.save("images\grayscaled\\" + item)
