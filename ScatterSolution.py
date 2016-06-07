import os
from PIL import Image, ImageDraw
from pylab import *
import csv

in_file = '/Users/cheriehuang/Desktop/altered.csv'

out_file = "/Users/cheriehuang/Desktop/scatterbinsresult.jpg"

rows = []

numImages = 0
with open(in_file, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)
        #holds the total amount of images or x-coordinates
        #used as a check with the dictionary
        numImages += 1
#popping off each row
rows.pop(0)
#saving the first column of each row as image paths
image_paths = [row[0] for row in rows]
print len(image_paths) #print statement for debugging
#saving the x coordinate and y coordinate into list of tuples 
dicts = {}
projected_features = array([(float(row[1]), float(row[2])) for row in rows])
h,w = 20000,20000
ns = (275,275)
img = Image.new('RGB',(w,h),(255,255,255))
#drawing the canvas
draw = ImageDraw.Draw(img)

#it takes the max in the projected_features array, the max coordinates essentially.
scale = abs(projected_features).max(0)
#for each p in the projected features, floor gives you the largest integer number equal or less than the list??
scaled = floor(array([ (p / scale) * (w/2-20,h/2-20) + (w/2,h/2) for p in projected_features]))
for i in range(len(image_paths)):
  theX = int(scaled[i][0]-ns[0]//2)
  theY = int(scaled[i][1]-ns[1]//2)
#saving the dict with the right key
  dicts[(image_paths[i], theY)] = theX
  #Will never have the same image path with the same Y

#getting the height which is the tallest y-coordinate
keys = dicts.keys()
#sorting in reverse
keys = sorted(keys, key = lambda x: x[1], reverse = True)
#got the largest y-value
height = keys[0]
XValues = dicts.values()
#instead of looping through the list, loop through the dicts keys and then the valus
numBins = 4 #will usually be a user provided number.
#now sorting this list from small to big
XValues.sort()
#getting the biggest x-coordinate and the smallest x-coordinate
smallest = XValues[0]
largest = XValues[len(XValues) - 1]
#gives you the distance between 
distance = int(largest - smallest)
divided = int(distance/numBins)
#changing the values to the right bin values
for u in dicts:
    currentX = dicts[u]
    binValue = (currentX - smallest)/divided
    dicts[u] = binValue
#the size of each image
#graphH = (size1 * height) 
#graphW = size1 * numBins
#creating the background graph image
#img = Image.new('RGB',(graphW,graphH),(255,255,255))
for t in dicts:
    path = t[0]
    y = t[1]
    bin = dicts[t]
    print bin
    im = Image.open(path)
    im = im.resize((275,275))
    img.paste(im, (bin, y))

#finishing by outputting the file
img.save(out_file)




