import sys
import re

filePath = sys.argv[1]
# filePath = './day3/input.txt'

'''       part 1        '''
muls=[]

with open(filePath, 'r') as f:
  for line in f:
    lineMuls = re.findall('mul\(\d+,\d+\)+', line)
    muls += lineMuls

sums = 0
for mul in muls: 
  x, y = mul[4:].split(',')
  y=y.strip(')')
  sums += int(y) * int(x)
  
print(f"sums: {sums}")

'''       part 2        '''
muls=[]

with open(filePath, 'r') as f:
  for line in f:
    for section in line.split('do()'):
      valid = section.split('don\'t()')[0]
      lineMuls = re.findall('mul\(\d+,\d+\)+', valid)
      muls += lineMuls
      
      print(valid)

sums = 0
for mul in muls: 
  x, y = mul[4:].split(',')
  y=y.strip(')')
  sums += int(y) * int(x)
  
print(f"sums: {sums}")
