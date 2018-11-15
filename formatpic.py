from PIL import Image
from numpy import *

import morphologyoperation as mo

def convert():
    img = Image.open("test.jpg")
    img1 = img.convert("L")
    img1.save("L.jpg")
    img2 = array(img1)

    for line in img2:
        for i in range(len(line)):
            line[i] = (line[i]<188)*255
    print(img2)
    img2 = Image.fromarray(img2)
    img2.save("1.jpg")


def dilation_test():
    img = Image.open("1.jpg")
    img = array(img)
    se = [[1,1],[1,1]]
    img = mo.bi_dilation(img,se)
    img = Image.fromarray(img)
    img = img.convert("RGB")
    img.save("dilation.jpeg")


def erosion_test():
    img = Image.open("1.jpg")
    img = array(img)
    se = [[1,1],[1,1]]
    img = mo.bi_erosion(img,se)
    img = Image.fromarray(img)
    img = img.convert("RGB")
    img.save("erosion.jpeg")
    print(img.size)

def combine_test():
    img = Image.open("1.jpg")
    img = array(img)
    se = [[1]*2]*2
    img = mo.bi_erosion(img,se)
    img = mo.bi_dilation(img,se)
    img = mo.bi_dilation(img,se)
    img = Image.fromarray(img)
    img = img.convert("RGB")
    img.save("combind.jpg")
    

combine_test()
##dilation_test()
##erosion_test()
