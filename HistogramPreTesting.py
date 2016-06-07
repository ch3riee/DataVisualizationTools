import cv2
import csv
import numpy as np
from PIL import Image, ImageDraw


#h,w = 500, 500
#img = Image.new('RGB',(w,h),(0,0,0))
#the image pasting part
f = open('/Users/cheriehuang/Desktop/testing.csv', 'rb')
data = csv.reader(f)
#size = 20,20
#height1 = 465
#height2= 465
#height3 = 465
#height4 = 465
totalNum = 0
Path = []
Bin = []
for row in data:
     totalNum = totalNum + 1
     Path.append(row[0])
     Bin.append(row[1])

h,w =  1000, 1000
img = Image.new('RGB',(w,h),(0,0,0))
size1 = (1000/totalNum)
size = size1, size1
height1 = 1000 - size1
height2 = 1000 - size1
height3 = 1000 - size1
height4 = 1000 - size1
theBins = []
match = False
for i in range(len(Path)):
    im = Image.open(Path[i])
    im = im.copy()
    im.thumbnail(size, Image.ANTIALIAS)
    for f in theBins:
        if f == Bin[i]:
            match = True
    if match == False:
        theBins.append(Bin[i])
        theBins = theBins.sort()

    if Bin[i] == theBins[0]:
            img.paste(im,( int(Bin[i]) * size1, height1))
            height1 = height1 - (size1)
    elif Bin[i] == '2':
            img.paste(im,(int(Bin[i]) * size1, height2))
            height2 = height2 - (size1)
    elif Bin[i] == '3':
            img.paste(im,(int(Bin[i]) * size1, height3))
            height3 = height3 - (size1)s
    else:
            img.paste(im,(int(Bin[i]) * size1, height4))
            height4 = height4 - (size1)

img = np.asarray(img)[:,:,::-1].copy()

#cv2.line(img,(0,480),(511,480),(255,0,0),2)
#cv2.line(img,(0,0),(0,480),(255,0,0),2)



cv2.imshow('image',img)
k = cv2.waitKey(0)
if k ==27: #wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('a'): #wait for 'a' key to save and exit
    cv2.imwrite('theGraph.png', img)
    cv2.destroyAllWindows()
