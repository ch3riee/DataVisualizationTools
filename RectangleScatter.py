import os
from PIL import Image, ImageDraw
from pylab import *
import csv
from  intersection import Rectangles
from Switch import switch

in_file = '/Users/cheriehuang/Desktop/altered.csv'

out_file = "/Users/cheriehuang/Desktop/rectHackResult.jpg"

#first reading in the file rows into a list array
rows = []
with open(in_file, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

#popping off each row
rows.pop(0)
#saving the first column of each row as image paths
image_paths = [row[0] for row in rows]
#saving the x coordinate and y coordinate into list of tuples 
projected_features = array([(float(row[1]), float(row[2])) for row in rows])
h,w = 20000,20000
ns = (275,275)


#it takes the max in the projected_features array, the max coordinates essentially.
scale = abs(projected_features).max(0)
#for each p in the projected features, floor gives you the largest integer number equal or less than the list??
scaled = floor(array([ (p / scale) * (w/2-20,h/2-20) + (w/2,h/2) for p in projected_features]))
allrectangles= []
for i in range(len(image_paths)):
  theObject = Rectangles()
  theObject.setpath(image_paths[i])
  theObject.setsize(275)
  theObject.setCoordinates(int(scaled[i][0]-ns[0]//2),int(scaled[i][1]-ns[1]//2))
  allrectangles.append(theObject)


    #print counter
    #print overlaps[i].getCoordinates()
  #nonoverlaps.append(overlaps[i])

#when none of them overlap
#start creating the actual canvas and pasting all the pictures down
img = Image.new('RGB',(w,h),(255,255,255))
#drawing the canvas
draw = ImageDraw.Draw(img)
for i in range(len(nonoverlaps)):
  theRectangle = nonoverlaps[i]
  nodeim = Image.open(theRectangle.getpath()) 
  nodeim = nodeim.resize((275,275))
  #pasting the image by getting the coordinates from the rectangle
  x1 = theRectangle.getX1()
  y1 = theRectangle.getY1()
  x4 = theRectangle.getX4()
  y4 = theRectangle.getY4()
  img.paste(nodeim, (x1, y1, x4, y4))


#saving the finished graph
img.save(out_file)







	


