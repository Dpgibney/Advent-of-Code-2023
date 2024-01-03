import numpy as np

file1 = open('p1_input.example','r')
file1 = open('p1_input.txt','r')
Lines = file1.read().splitlines()

sky = []
for line in Lines:
    tmp = []
    for char in line:
        tmp.append(char)
    sky.append(tmp)
sky = np.array(sky,dtype=np.dtype('U1000'))

'''Find rows and columns without galaxies'''
row_exp = []
for row in range(sky.shape[1]):
    galaxy = False
    for col in range(sky.shape[0]):
        if sky[row][col] == '#':
            galaxy = True
            break
    if not galaxy:
        row_exp.append(row)
col_exp = []
for col in range(sky.shape[0]):
    galaxy = False
    for row in range(sky.shape[1]):
        if sky[row][col] == '#':
            galaxy = True
            break
    if not galaxy:
        col_exp.append(col)

'''Expand map in reverse order to not deal with later numbers moving'''
#for row in row_exp[::-1]:
#    sky = np.insert(sky,row,'.',axis=0)
#for col in col_exp[::-1]:
#    sky = np.insert(sky,col,'.',axis=1)

'''Label galaxies'''
galaxy_count = 1
for col in range(sky.shape[0]):
    for row in range(sky.shape[1]):
        if sky[col][row] == '#':
            sky[col][row] = galaxy_count
            galaxy_count += 1

#np.set_printoptions(precision=0,edgeitems=30,linewidth=180)
galx_loc = []
for galx_num in range(1,galaxy_count):
    x,y = np.where(sky == str(galx_num))
    x = x[0]
    y = y[0]
    galx_loc.append([x,y])

dist = 0
expansion = 1000000
for first in range(len(galx_loc)):
    print(first,len(galx_loc))
    for second in range(first+1,len(galx_loc)):
        row1,col1 = galx_loc[first]
        row2,col2 = galx_loc[second]
        dist += abs(col1-col2) + abs(row1-row2)
        '''Add in the extra distance here'''
        empty_rows = [row for row in row_exp if ((row2 > row and row > row1) or (row1 > row and row > row2))]
        dist += (len(empty_rows) * (expansion-1))
        empty_cols = [col for col in col_exp if ((col2 > col and col > col1) or (col1 > col and col > col2))]
        dist += (len(empty_cols)* (expansion-1))
print(dist)
