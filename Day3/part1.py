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
            if row[j].strip() == ".":
                matrix[i,j] = None
            else:
                matrix[i,j] = "*"


symbols = {}
for i in range(rows):
    for j in range(columns):
        if matrix[i,j] =="*":
            symbols[i,j] = "*"

# for key in symbols:
#     print(key, symbols[key])        


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
for key in numbers:
    minrow = key[0]-1
    maxrow = key[0]+1
    mincol = key[1]-1
    maxcol = key[1]+len(numbers[key])
    if minrow < 0:
        minrow=0
    if maxrow > rows:
        maxrow = rows
    if mincol < 0:
        mincol = 0
    if maxcol > columns:
        maxcol = columns
    
    countval = False
    for i in range(minrow, maxrow+1):
        for j in range(mincol, maxcol+1):
            if (i,j) in symbols:
                countval = True
    if countval:
        total += int(numbers[key])
    
            
print(total)
