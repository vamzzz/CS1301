#Vamshi Adimulam
#GTID: 903161218
#vamshi.adimulam@gatech.edu
#I worked on the homework assignment alone, using only this
#semester's course materials. 

from Myro import *

def makeGrayscale(pic):
    pix = makePicture(pic)
    width = getWidth(pix)
    height = getHeight(pix)
    for pixel in getPixels(pix):
        redvalue = getRed(pixel)
        greenvalue = getGreen(pixel)
        bluevalue = getBlue(pixel)
        greyvalue = (redvalue + greenvalue + bluevalue)/3                
        setRed(pixel, greyvalue)
        setGreen(pixel, greyvalue)
        setBlue(pixel, greyvalue)
    savePicture(pix, "grayed.jpg")
    return show(pix)
    
def getBlockValue(pic,x,y):
    count = 0
    avg = 0
    box = 8
    pixels=0
    for i in range (x,x+2):
        for j in range (y,y+4):  
            value = getPixel(pic,i,j)
            r = getRed(value)
            g = getGreen(value)
            b = getBlue(value)
            mean = (r+g+b)//3
            avg = avg + mean
            pixels=pixels+1
    hey=avg//pixels
    return hey
            
            
def getASCIIPixel(aNum):
    if aNum <26:
        aNum = "@"
    elif aNum <51:
        aNum = "#"
    elif aNum <76:
        aNum = "%"
    elif aNum <101:
        aNum = "*"   
    elif aNum <126:
        aNum = "="
    elif aNum <151:
        aNum = "+"
    elif aNum <176:
        aNum = "-"
    elif aNum <201:
        aNum = ":"  
    elif aNum <226:
        aNum = "."
    elif aNum <=255:
        aNum = " "
    return aNum
        
        
def getASCIIMatrix(pic):
    
    alist = []
    somePic = makePicture(pic)
    makeGrayscale(somePic)
    h = getHeight(somePic)
    w = getWidth(somePic)
    for d in range (0,h,4):
        sublist = []
        for x in range(0,w,2):
            block = getBlockValue(somePic,x,d)
            vam = getASCIIPixel(block)
            sublist.append(vam)
        alist.append(sublist)
        
    return (dlist)
     
    
def makeASCIIArt(pic):
    matrix = getASCIIMatrix(pic)
    pic = pic[:-3] + "txt"
    aFile = open(pic,"w")
    for val in matrix:
        for j in val:
            aFile.write(str(j))
        aFile.write("\n")
    aFile.close()
        