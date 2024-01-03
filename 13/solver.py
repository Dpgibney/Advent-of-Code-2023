file1 = open('p1_input.example','r')
file1 = open('p1_input.txt','r')
Lines = file1.read().splitlines()
import numpy as np

'''shape is rows, columns'''
'''Check for a first match and then expand'''
def match(geom) -> int:
    for i in range(geom.shape[0]-1):
        tmp = 1
        if (geom[i] == geom[i+1]).all():
            found = True
            while 0 <= i - tmp and i + 1 + tmp < geom.shape[0]:
                if not (geom[i-tmp] == geom[i+tmp+1]).all():
                    found = False
                tmp += 1
            if found:
                '''adding one since its 1 ordered not 0 ordered'''
                return (i+1,i+2)

    return False
                


geoms = [[]]
'''Create list of lists of the different inputs'''
for line in Lines:
    if line == '':
        geoms.append([])
    else:
        tmp = []
        for char in line:
            tmp.append(char)
        geoms[-1].append(tmp)

summary = 0
for geom in geoms:
    geom = np.array(geom)
    '''shape is rows, columns'''
    '''Check for a first match and then expand'''
    result = match(geom)
    if result is False:
        result = match(geom.T)
        summary += result[0]
    else:
        summary += result[0] * 100
print(summary)

            
        

