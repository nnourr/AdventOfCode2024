import sys

filePath = sys.argv[1] if len(sys.argv) > 1 else './day4/test.txt'
# filePath = './day3/input.txt'

'''       part 1        '''

grid = []

with open(filePath, 'r') as f:
  grid = [line.strip('\n') for line in f.readlines()]

def validateWord(word):
  if word == 'XMAS' or word == 'SAMX': return True
  

def check(slice, i):
  matches = 0
  if i >= 3:
    word = slice[i-3:i+1]
    if validateWord(word): matches+=1
  if i + 3 <= len(slice):
    word = slice[i:i+4]
    if validateWord(word): matches+=1
  
  return matches
    

def transformVertical(grid, x, y):
  return ''.join([grid[y][x] for y in range(len(grid))])

def transformDiagonalRight(grid, start_x, start_y):
  # return ''.join([grid[y][x] for y in range(len(grid))])
  diagonal = []
  x = start_x
  y = start_y
  offset = 0
  while x >=0 and y < len(grid):
    diagonal.append(grid[y][x])
    x -= 1
    y += 1
    offset += 1
  diagonal.reverse()

  x = start_x + 1 
  y = start_y - 1 
  # assuming consistent grid
  while x < len(grid[0]) and y >= 0:
    diagonal.append(grid[y][x])
    x += 1
    y -= 1
    
  return ''.join(diagonal), offset-1

def transformDiagonalLeft(grid, start_x, start_y):
  # return ''.join([grid[y][x] for y in range(len(grid))])
  diagonal = []
  x = start_x
  y = start_y
  offset = 0
  while x < len(grid[0]) and y < len(grid):
    diagonal.append(grid[y][x])
    x += 1
    y += 1
    offset += 1
  diagonal.reverse()
  
  x = start_x - 1
  y = start_y - 1
  
  while x >= 0 and y >= 0:
    diagonal.append(grid[y][x])
    x -= 1
    y -= 1
    
  return ''.join(diagonal), offset-1

xmasCount = 0
for y in range(len(grid)):
  for x in range(len(grid[y])):
    if grid[y][x] == 'X':
      xmasCount += check(grid[y], x)
      xmasCount += check(transformVertical(grid, x, y), y)
      xmasCount += check(*transformDiagonalRight(grid, x, y))
      xmasCount += check(*transformDiagonalLeft(grid, x, y))
print("XMAS Count:" + str(xmasCount))
      
      
'''       part 2        '''

def validateWord(word):
  if word == 'ASMSM' or word == 'AMSMS' or word == 'ASSMM' or word == 'AMMSS': return True

def checkXmas(grid, x, y):
  word = [grid[y][x]]
  word.append(grid[y-1][x-1])  
  word.append(grid[y-1][x+1])  
  word.append(grid[y+1][x-1])  
  word.append(grid[y+1][x+1])
  
  return validateWord(''.join(word))

xmasCount = 0
for y in range(1, len(grid) - 1):
  for x in range(1, len(grid[y]) - 1):
    if grid[y][x] == 'A':
      if checkXmas(grid, x, y): xmasCount += 1
      
print("X-MAS Count:" + str(xmasCount))
