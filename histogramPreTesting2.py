import cv2
import csv
import numpy as np
from PIL import Image, ImageDraw


h,w = 500, 500
img = Image.new('RGB',(w,h),(0,0,0))
#the image pasting part
f = open('/Users/cheriehuang/Desktop/testing.csv', 'rb')
data = csv.reader(f)
size = 20,20
height1 = 465
height2= 465
height3 = 465
height4 = 465
Path = []
Bin = []
for row in data:
     Path.append(row[0])
     Bin.append(row[1])
for i in range(len(Path)):
    im = Image.open(Path[i])
    im = im.copy()
    im.thumbnail(size, Image.ANTIALIAS)
    if Bin[i] == '1':
            #img.paste(im,(i+20, 465))
            img.paste(im,( int(Bin[i]) +50, height1))
            height1 = height1 - 15
    elif Bin[i] == '2':
            #img.paste(im,(i+40, 465))
            img.paste(im,(int(Bin[i])+100, height2))
            height2 = height2 - 15
    elif Bin[i] == '3':
            #img.paste(im,(i+60, 465))
            img.paste(im,(int(Bin[i])+150, height3))
            height3 = height3 - 15
    else:
            #img.paste(im,(i+80, 465))
            img.paste(im,(int(Bin[i])+200, height4))
            height4 = height4 - 15

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
