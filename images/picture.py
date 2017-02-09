import statistics
from PIL import Image
im = Image.open("1.png")
im2 = Image.open("2.png")
im3 = Image.open("3.png")
im4 = Image.open("4.png")
im5 = Image.open("5.png")
im6 = Image.open("6.png")
im7 = Image.open("7.png")
im8 = Image.open("8.png")
im9 = Image.open("9.png")
imgList = [im, im2, im3, im4, im5,im6,im7,im8, im9]

pictureWidth = im.size[0]
pictureHeight = im.size[1]
print("Opened images..", pictureWidth, pictureHeight)

greenList = []
blueList = []
redList = []

greenPixel = 0
bluePixel = 0
redPixel = 0



newImage = Image.new("RGB", (pictureWidth, pictureHeight),"white")
for x in range(0, pictureWidth):
    for y in range(0, pictureHeight):
        for myImage in imgList:
            myblue , mygreen , myred = myImage.getpixel((x,y))
            #bluePixel is added to blue list
            blueList.append(myblue)
            #greenpixel is added to green list
            greenList.append(mygreen)
            #redpixel is added to the red list
            redList.append(myred)
        redPixel = statistics.median(redList)
        greenPixel=statistics.median(greenList)
        bluePixel=statistics.median(blueList)
        greenList = []
        blueList = []
        redList = []
        newImage.putpixel((x, y),( redPixel, greenPixel, bluePixel))
   
    
    
    


print("Finished")
newImage.save('Diegoproject.jpg')
"""
median inside the loop

save the output of image.new
"""
"""
for theImage in theImages = []

def medianOdd(myList):

listLength = len(list)

sortedValues = sorted(myList)

middleIndex = ((listLength + 1)/2) - 1

return sortedValues

from PIL import Image
im.image.new("RBG", (512, 512)
"""