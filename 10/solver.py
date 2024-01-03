import numpy as np

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
Lines = file1.readlines()
'''
0 = north
1 = east
2 = south
3 = west
Has format pipe shape: NS movement, EW movement, cur_dir
'''
connects = {'|':[[-1,0,0],None,[1,0,2],None],'-':[None,[0,1,1],None,[0,-1,3]],'L':[None,None,[0,1,1],[-1,0,0]],'J':[None,[-1,0,0],[0,-1,3],None],'7':[[0,-1,3],[1,0,2],None,None],'F':[[0,1,1],None,None,[1,0,2]]}

grid = []
for line in Lines:
    line = line.strip()
    tmp = []
    for char in line:
        tmp.append(char)
    grid.append(tmp)

grid = np.array(grid)
distance = np.zeros(grid.shape)
print(grid)

x = np.where(grid == 'S')
up = [x[0][0],x[1][0]]
down = up.copy()
left = up.copy()
right = up.copy()
up[0] -= 1
down[0] += 1
right[1] += 1
left[1] -= 1
directions = [up,right,down,left]
for direc, pos in enumerate(directions):
    cur_dir = direc
    y,x = pos
    dist = 1
    if y < 0 or y >= grid.shape[0] or x < 0 or x >= grid.shape[1]:
        pass
    else:
        while True:
            char = grid[y,x]
            print(char,cur_dir)
            distance[y,x] = dist
            if char == 'S':
                break
            if char == '.':
                break
            if connects[char][cur_dir] is None:
                break
            y += connects[char][cur_dir][0]
            x += connects[char][cur_dir][1]
            cur_dir = connects[char][cur_dir][2]
            dist += 1
print(distance.max())
