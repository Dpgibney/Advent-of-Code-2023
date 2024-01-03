import numpy as np

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
#file1 = open('p2_input.example','r')
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


cur_dir = 2
y,x = down
dist = 1
if y < 0 or y >= grid.shape[0] or x < 0 or x >= grid.shape[1]:
    pass
else:
    while True:
        char = grid[y,x]
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

#print(distance)
cur_dir = 0
y,x = 25-1,108
#
#y,x = 1, 4 
#cur_dir = 2
#prev_dir = 2
fill_map = [[0,-1],[-1,0],[0,1],[1,0]]
#fill_map = [[0,1],[1,0],[0,-1],[-1,0]]
np.set_printoptions(precision=0,edgeitems=30,linewidth=180)
change = True
while True:
    #if change:
    #    print(distance)
    change = False
    char = grid[y,x]
#    print(distance[y,x],"dir: ",cur_dir,"next dir: ",connects[char][cur_dir][2])
    if char == 'S':
        break
    if char == '.':
        break
    if connects[char][cur_dir] is None:
       break

    y0 = y + fill_map[cur_dir][0]
    x0 = x + fill_map[cur_dir][1]
    #print("old y0 x0: ",y0,x0)
    while distance[y0,x0] < 1:
        distance[y0,x0] = -1
        y0 += fill_map[cur_dir][0]
        x0 += fill_map[cur_dir][1]
        change = True
    y0 = y + fill_map[connects[char][cur_dir][2]][0]
    x0 = x + fill_map[connects[char][cur_dir][2]][1]
    y += connects[char][cur_dir][0]
    x += connects[char][cur_dir][1]
    cur_dir = connects[char][cur_dir][2]
    #print("new y0 x0: ",y0,x0)
    while distance[y0,x0] < 1:
        change = True
        distance[y0,x0] = -1
        y0 += fill_map[cur_dir][0]
        x0 += fill_map[cur_dir][1]
print(len(np.where(distance == -1)[0]))
#print(distance)
#print(distance[20:30,103:113])
found = True
found = False
while found:
    found = False
    for x in range(1,distance.shape[1]-1):
        for y in range(1,distance.shape[0]-1):
            #print(x,y)
            #print(distance[y,x])
            if distance[y,x] == 0:
                if distance[y+1,x] == -1 or distance[y-1,x] == -1 or distance[y,x+1] == -1 or distance[y,x-1] == -1:
                    distance[y,x] = -1
                    found = True
#print(distance)
print(len(np.where(distance == -1)[0]))


