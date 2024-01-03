import numpy as np

def slide(arr):
    tmp_fixed = []
    tmp_mobile = []
    mapping = []
    for elem in arr:
        if elem != '#':
            if len(tmp_fixed) is not 0:
                mapping.append(tmp_fixed.copy())
                tmp_fixed = []
            tmp_mobile.append(elem)
        else:
            if len(tmp_mobile) is not 0:
                mapping.append(tmp_mobile.copy())
                tmp_mobile = []
            tmp_fixed.append(elem)
    if len(tmp_mobile) is not 0:
        mapping.append(tmp_mobile.copy())
    if len(tmp_fixed) is not 0:
        mapping.append(tmp_fixed.copy())

    for indx, subset in enumerate(mapping):
        if subset[0] is not '#':
            mapping[indx] = sorted(subset,reverse=True)
    
    matrix_map = []
    tmp = []
    for line in mapping:
        for group in line:
            for char in group:
                tmp.append(char)
    matrix_map.append(tmp)
    return matrix_map


file1 = open('p1_input.txt','r')
file1 = open('p1_input.example','r')
Lines = file1.read().splitlines()

geometry = []
for line in Lines:
    tmp = []
    for char in line:
        tmp.append(char)
    geometry.append(tmp)

geometry = np.rot90(geometry,-3)
cycle = -1
cycle_res = []
for i in range(1000000000):
    geometry = np.rot90(geometry,-1)
    geometry = np.array(geometry).transpose()
    
    for line_indx in range(geometry.shape[0]):
        geometry[line_indx] = np.array(slide(geometry[line_indx]))
    
    geometry = geometry.transpose()
    if i % 4 == 3:
        north = (np.rot90(geometry,-(4 - (i % 4))))
        #print(cycle)
        cycle += 1
        result = 0
        for row_num, row in enumerate(north):
            for elem in row:
                if elem == 'O':
                    result += north.shape[1] - row_num
        cycle_res.append(result)
        print(cycle_res)

