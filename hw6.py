# CS1301-A1, Spring 2016, Georgia Institute of Technology
#Vamshi Adimulam & Jisoon Lim 
# vamshi.adimulam@gatech.edu
# "My partner and I worked on the homework assignment alone, using only this semester's course materials"

from Myro import *
init()

def changepic(image):
    for pix in getPixels(image):
        if getGreen(pix)<50: 
            setRed(pix,0)
            setGreen(pix,0)
            setBlue(pix,0)
        else:
            setRed(pix,255)
            setGreen(pix,255)
            setBlue(pix,255)
    
def horizontal(image):
    h = getHeight(image)
    w = getWidth(image)
    for y in range(h):
        pix = getPixel(image,0,y)
        if getGreen(pix) == 0:
            count = 0
            for x in range(w):
                pixel = getPixel(image,x,y)
                if getGreen(pixel) == 0:
                    count += 1
                if count == w:
                    return "horizontal"
    
def vertical(image):
    h = getHeight(image)
    w = getWidth(image)
    for x in range(w):
        pix = getPixel(image,x,0)
        if getGreen(pix) == 0:
            count = 0
            for y in range(h):
                pixel = getPixel(image,x,y)
                if getGreen(pixel) == 0:
                    count += 1
                if count == h:
                    return "vertical"
                    
def action():
    image = takePicture()
    changepic(image)
    if vertical(image) == "vertical":
        forward(1,1)
        backward(1,1) 
    if horizontal(image) == "horizontal":
        turnLeft(1,1)
        turnRight(1,1)
         

    

    


