import numpy as np
import sys

np.set_printoptions(threshold = sys.maxsize)

FILENAME = "input.txt"

with open(FILENAME) as f:
    data = f.readlines()
    rows = len(data)
    columns = len(data[0])



matrix = np.ndarray(shape=(rows,columns), dtype=object)
    
for i, row in enumerate(data):
    for j in range(len(row)-1):
        try:
            matrix[i,j] = int(row[j])
        except:
            if row[j].strip() == "*":
                matrix[i,j] = "*"
            else:
                matrix[i,j] = None


symbols = {}
for i in range(rows):
    for j in range(columns):
        if matrix[i,j] =="*":
            symbols[i,j] = "*"
  

numbers = {}
skip1=False
skip2=False
for i in range(rows):
    for j in range(columns):
        if skip2:
            skip2=False
            continue
        if skip1:
            skip1=False
            continue
        if matrix[i,j] != None and matrix[i,j] != "*":
            if matrix[i,j+1]!= None and matrix[i,j+1] != "*":
                if matrix[i,j+2]!= None and matrix[i,j+2] != "*":
                    numbers[i,j] = str(matrix[i,j])+str(matrix[i,j+1])+str(matrix[i,j+2])
                    skip1 = True
                    skip2 = True
                else:
                    numbers[i,j] = str(matrix[i,j])+str(matrix[i,j+1])
                    skip1 = True
            else:
                numbers[i,j] = str(matrix[i,j])


total = 0
correct = []
for key in symbols:
    minrow = key[0]-1
    maxrow = key[0]+1
    mincol = key[1]-1
    maxcol = key[1]+1
    if minrow < 0:
        minrow=0
    if maxrow > rows:
        maxrow = rows
    if mincol < 0:
        mincol = 0
    if maxcol > columns:
        maxcol = columns
    
    numval = 0
    for i in range(minrow, maxrow+1):
        last=None
        for j in range(mincol, maxcol+1):
            if matrix[i,j] != None and matrix[i,j] != "*":
                if last == None or last == "*":
                    numval += 1
            last = matrix[i,j]
    if numval == 2:
        correct.append(key)

total=0
for key in correct:
    to_multiply = []
    product = 1
    minrow = key[0]-1
    maxrow = key[0]+1
    mincol = key[1]-3
    maxcol = key[1]+1
    if minrow < 0:
        minrow=0
    if maxrow > rows:
        maxrow = rows
    if mincol < 0:
        mincol = 0
    if maxcol > columns:
        maxcol = columns
    
    for i in range(minrow, maxrow+1):
        for j in range(mincol, maxcol+1):
            if (i,j) in numbers and len(numbers[i,j])+j>key[1]-1:
                to_multiply.append(numbers[i,j])
    for number in to_multiply:
        product *= int(number)
    total += product           

print(total)


