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

print numImages

#popping off each row
rows.pop(0)
#saving the first column of each row as image paths
image_paths = [row[0] for row in rows]
print len(image_paths)
#creating the dictionary
dicts = {}
#saving the x coordinate and y coordinate into list of tuples 
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
  theKeyX = int(scaled[i][0]-ns[0]//2)
  theY = int(scaled[i][1]-ns[1]//2)
#saving the dict with the right key
  dicts[(theKeyX, theY)] = image_paths[i]
  #what happens if they have the same x-coordinate and y-coordinate?? 


#list of just the (x-coordinates, y-coordinates)
thekeys = dicts.keys()
numBins = 4 #will usually be a user provided number.
print len(thekeys)
#now sorting this list from small to big
thekeys.sort()
#making a clone of this list so you do not alter the original list.
tempList = list(thekeys)
#getting the biggest x-coordinate and the smallest x-coordinate
smallest = (thekeys[0])[0]
largest = (thekeys[len(thekeys)-1])[0]
#gives you the distance between 
distance = int(largest - smallest)
#there will be a user specified bin number
divided = int(distance/numBins)
#holds the x-coordinates for the bins
comparisons = []
comparisons.append(smallest)
x = 0
while x < numBins:
	comparisons.append(comparisons[x] + divided)
	x = (x + 1)
	#if 4 bins there should be 5 elements in the array. Last element should be equal to largest.
j = 1
binList = []
while j < len(comparisons):
	#need to get loop througn the list. Each time through this big for loop, is going through the comparisons. 
	#because less than. you need to grab the next comparison but the x-coord would be the comparison before it!
	#This means the last one will not be an x, unless there are things bigger than it or equal.
	theCurrentX = comparisons[j-1]
	theCompareX = comparisons[j]
	ebinList = []
    t = 0
	while t < len(tempList):
		theTuple = tempList[t]
		theX = theTuple[0]
		if theX < theCompareX:
			#not just appending the x, but the whole tuple
			ebinList.append(theTuple)
			tempList.pop(t)
			#don't increment t because just removed something
		else if theX >= theCompareX:
			#if it isn't less, you know the rest won't be because it is in order.
			#so you break so it goes to the bigger while loop
			break
	#breaking from the nested while loop
	binList.append(ebinList)
	#have to check later to make sure it is not NONE or empty list when pasting and iterating
	#incrementing to the next comparisons
	j = (j + 1)
m = 0
for n in range(len(binList)):
	#n being a list itself
	#the current x coordinate for the items
	XCOORD = comparisons[m]
	if not n:
		continue
	else:
		currentList = binList[n]
		for s in range(len(currentList)):
			PATH = dicts.get(currentList[s])
			#getting the y coordinate from the tuple
			YCOORD = (currentList[s])[1]
			im = Image.open(PATH)
			im = im.resize((275,275))
			img.paste(im, (XCOORD, YCOORD))

img.save(out_file)





