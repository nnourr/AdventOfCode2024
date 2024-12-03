# count how many are safe
# safe=
#   increasing or decreasing
#   by 1 - 3 inclusive

import sys

contents = []
filePath = sys.argv[1]
# filePath = './day2/test.txt'

numSafe = 0

with open(filePath, 'r') as f:
  for content in f:
    for report in f:
      prev = -1
      mode = 0
      safe = True
      for i, level in enumerate(report.split(' ')):
        level = int(level)
        if i == 0:
          prev = level
          continue
        diff = prev-level
        prev = level
        if abs(diff) > 3 or abs(diff) < 1:
          safe = False
          break

        if diff > 0:
          if mode == 0 or mode == 1:
            mode = 1
          else:
            safe = False
            break
        else:
          if mode == 0 or mode == -1:
            mode = -1
          else:
            safe = False
            break

      if safe: numSafe += 1


print("num safe: " + str(numSafe))

'''   pt2   '''

def removeIndex(arr, i):
  return arr[:i]+arr[i+1:]

def dampCheck(levels):
  if (isReportSafe(levels)): return True
  
  for i in range(len(levels)):
    dampenedList = removeIndex(levels, i)
    if isReportSafe(dampenedList): return True
  return False    

def isReportSafe(levels):
  mode = 0
  for i in range(len(levels) -1):
    diff = levels[i] - levels[i+1]
    if abs(diff) > 3 or abs(diff) < 1:
      return False
    if diff > 0:
      if mode == -1: return False
      mode = 1
    else:
      if mode == 1: return False
      mode = -1
  return True

def pt2():
  numSafe = 0

  with open(filePath, 'r') as f:
    for report in f:
      levels = [int(level) for level in report.split(' ')]
      if dampCheck(levels):
        numSafe += 1

  return numSafe

print("num safe now: " + str(pt2()))
