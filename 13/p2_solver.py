file1 = open('p1_input.example','r')
file1 = open('p1_input.txt','r')
Lines = file1.read().splitlines()
import numpy as np

'''shape is rows, columns'''
'''Check for a first match and then expand'''
def match(geom, trans = True, orig_result = (-1,-1)) -> int:
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
                #print(geom)
                #print(i,i+1)
                if ((i+1, i+2), trans) != (orig_result):
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
    print(geom)
    print(geom.T)

    '''Generate original result that the new one should be different than'''
    geom_orig = geom.copy()
    result_orig = match(geom_orig)
    transposed = False
    if result_orig is False:
        result_orig = match(geom_orig.transpose())
        transposed = True
    #print(result_orig)
    results_orig = result_orig
    results_orig = (results_orig,transposed)

    '''Could be smart and remove locations that are not in the originals mirrored surface'''
    for i in range(geom.shape[0]):
        for j in range(geom.shape[1]):
            if geom[i,j] == '#':
                geom[i,j] = '.'
            else:
                geom[i,j] = '#'
                '''shape is rows, columns'''
                '''Check for a first match and then expand'''
                result = match(geom,False,results_orig)
                print(result)
                if result is False:
                    result = match(geom.transpose(),True,results_orig)
                    print(result)
                    if result is not False:
                        if not transposed:
                            print(result)
                            print(i,j)
                            summary += result[0]
                        #print(result)
                        #print(result_orig)
                        #print(result == result_orig)
                        else:
                            if not (result == result_orig):
                                print(result)
                                print(i,j)
                                summary += result[0]
                else:
                    if transposed:
                        print(result)
                        print(i,j)
                        summary += result[0] * 100
                    else:
                        if not (result == result_orig):
                            print(result)
                            print(i,j)
                            summary += result[0] * 100
            if geom[i,j] == '.':
                geom[i,j] = '#'
            else:
                geom[i,j] = '.'
    print(summary)
    #input()
print(summary)

            
        

