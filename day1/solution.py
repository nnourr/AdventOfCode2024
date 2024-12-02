# visit locations
# mark them with a star
# in the first 50 places
# ^^^ nvm this is the intro LMAOOO

'''     part 1      '''

# finding list of significant locations
# split in 2
# some duplicates

# pair up like this:
# "smallest number in the left list with the smallest number in the right list, 
# then the second-smallest left number with the second-smallest right number"
# add up distances between pairs

# read file
import sys

contents = []
filePath = sys.argv[1]

with open(filePath, 'r') as f:
  l1 = []
  l2 = []
  for content in f:
    splitL = content.split(' ')
    l1.append( int(splitL[0]))
    l2.append( int(splitL[3]))
    
# pair up lists
l1.sort()
l2.sort()

totalDist = 0
for i, item in enumerate(l1):
    totalDist += abs(item - l2[i])
    
print("total dist " + str(totalDist))
  

'''     part 2      '''

from collections import defaultdict

frequencyMap = defaultdict(int)
for i, item in enumerate(l1):
  frequencyMap[item] += 1
  
similarityScore = 0
for i, item in enumerate(l2):
  similarityScore += item * frequencyMap[item]
  
print("similarity score: " + str(similarityScore))