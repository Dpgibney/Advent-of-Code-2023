import numpy as np
from functools import lru_cache
file1 = open('p1_input.txt','r')
file1 = open('p1_input.example','r')

Lines = file1.read().splitlines()

mapped = []
'''Order is up, right, down, left'''
dir_mov = [[-1,0],[0,1],[1,0],[0,-1]]

for line in Lines:
    tmp = []
    for char in line:
        tmp.append(char)
    mapped.append(tmp)

@lru_cache(maxsize = 2000000)
def check_dir(position: tuple, direction: int, prev_dir: tuple) -> int:
    x,y = position
    if len(prev_dir) == 3:
        if (prev_dir[0] == prev_dir[1] and prev_dir[1] == prev_dir[2] and prev_dir[2] == direction):
            return 9999999
        else:
            prev_dir = tuple(prev_dir[1:])
    if x == 0 and y == 0:
        return 0
    elif (0 <= x and x < len(mapped)) and (0 <= y and y < len(mapped[x])):
        up    = 999999
        down  = 999999
        right = 999999
        left  = 999999
        if direction != 0:
            up    = check_dir((x-1,y),0,prev_dir + (0,))
        if direction != 1:
            right = check_dir((x,y+1),1,prev_dir + (1,))
        if direction != 2:
            down  = check_dir((x+1,y),2,prev_dir + (2,))
        if direction != 3:
            left  = check_dir((x,y-1),3,prev_dir + (3,))
        minum = min([up,right,left,down])
        return int(mapped[x][y]) + minum
    else:
        return 9999999

dist = [[999999 for j in range(len(mapped[i]))] for i in range(len(mapped))]
for i in range(len(mapped)):
    for j in range(len(mapped[i])):
        tmp = check_dir((i,j), 4, ())
        if tmp < dist[i][j]:
            dist[i][j] = tmp

#
#
#dist = [[[1000 for k in range(4)] for j in range(len(mapped[i]))] for i in range(len(mapped))]
#dist[0][0] = 0
#prev = [[[None for k in range(4)] for j in range(len(mapped[i]))] for i in range(len(mapped))]
#
#Q = []
#for i in range(len(mapped)):
#    for j in range(len(mapped[i])):
#        Q.append((i,j))
#
#last = np.array(dist)
#while Q != []:
#    #print(np.array(dist)-last)
#    last = np.array(dist)
#    '''Find minimum dist vertex'''
#    min_val = 100000000
#    min_loc = [0,0]
#    for vertex in Q:
#        if min_val > dist[vertex[0]][vertex[1]]:
#            min_loc[0] = vertex[0]
#            min_loc[1] = vertex[1]
#            min_val = dist[vertex[0]][vertex[1]]
#
#    #print(Q.index((min_loc[0],min_loc[1])))
#    del Q[Q.index((min_loc[0],min_loc[1]))]
#
#    tmp = dist[min_loc[0]][min_loc[1]]
#    dist[min_loc[0]][min_loc[1]] = -1
#    print(np.array(dist))
#    dist[min_loc[0]][min_loc[1]] = tmp
#
#    for direction,move in enumerate(dir_mov):
#        tmp = min_loc.copy()
#        tmp[0] += move[0]
#        tmp[1] += move[1]
#        print("moved to spot: ",tmp)
#        
#        '''Still in map'''
#        if (0 <= tmp[0] and tmp[0] < len(mapped)) and (0 <= tmp[1] and tmp[1] < len(mapped[tmp[0]])):
#            alt_dist = min_val + int(mapped[tmp[0]][tmp[1]])
#            is_line = True
#            '''Check that the previous three nodes don't form a line'''
#            for i in range(3):
#                x, y = min_loc.copy()
#                x = x - (move[0]*i)
#                y = y - (move[1]*i)
#                if (0 > x or x > len(mapped)) or (0 > y or y > len(mapped[tmp[0]])):
#                    is_line = False
#                    break
#                elif prev[x][y][direction] is None:
#                    print("direction: ",direction,prev[x][y][1])
#                    is_line = False
#                    break
#
#            for dir_from in range(4):
#                if dir_from == direction:
#                    if not is_line:
#                        print(alt_dist,dist[tmp[0]][tmp[1]][])
#                        if alt_dist < dist[tmp[0]][tmp[1]]:
#                            dist[tmp[0]][tmp[1]] = alt_dist
#                            prev[tmp[0]][tmp[1]][direction] = min_loc
#
#print(np.array(prev))
#print(np.array(dist))
#
#display = dist.copy()
#x,y = 12,12
#while prev[x][y] is not None:
#    display[x][y] = 0
#    x,y = prev[x][y][0]
#
#print(np.array(display))


    
