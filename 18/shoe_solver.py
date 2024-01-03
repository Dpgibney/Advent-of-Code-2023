import numpy as np

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
#file1  = open('danny.example','r')


'''Uses the shoelace algorithm'''

dir_map = {0: np.array([0,1]), 2: np.array([0,-1]), 3: np.array([-1,0]), 1: np.array([1,0])}

dig_plan = [[group for group in line.split()] for line in file1.read().splitlines()]

def print_map(corners,x,y):
    to_print = [['.' for j in range(x)] for i in range(y)]
    for spot in corners:
        y,x = spot
        to_print[y][x] = '#'
    print(np.array(to_print))

corners = [[0,0]]
perimeter = 0
for dig in dig_plan:
    direction, distance, color = dig
    distance = int(distance)
    color = color[2:-1]
    distance = int(color[:5],16)
    direction = int(color[-1])
    perimeter += distance
    #distance = int(color[])

    pos = [0,0]
    pos[0] = corners[-1][0] + (distance * dir_map[direction][0])
    pos[1] = corners[-1][1] + (distance * dir_map[direction][1])
    corners.append(pos)

#corners = corners[1:]
array = np.array(corners)
tmp = 0
for i in range(len(array)-1):
    print(array[i:i+2,0:2])
    print(i)
    print(tmp/2)
    print(perimeter/2+1)
    tmp += np.linalg.det(array[i:i+2,0:2])
print(np.linalg.det(array))

#corners = corners[::-1]
size = 0

'''p1 goes in reverse order'''
p1 = -1
p2 = 0

prev_dx = {}

while len(corners) > 0:
    '''Only doing up and down'''
    print(size)
    #print(corners)
    #input()
    dy1 = corners[p1][0] - corners[p1 - 1][0]
    dy2 = corners[p2][0] - corners[p2 + 1][0]

    y1 = corners[p1][0]
    y2 = corners[p2][0]

    dx = abs(corners[p1][1] - corners[p2][1]) + 1

    if (y1 == y2 and y1 == max(corners)[0]):
        if (dy1 > 0 and dy2 > 0):
            if dy1 < dy2:
                size += dx * (dy1)
                corners.insert(1,[y2-dy1,corners[p2][1]])
            elif dy2 < dy1:
                size += dx * (dy2)
                corners.insert(1,[y1-dy2,corners[p1][1]])
            elif dy2 == dy1:
                size += dx * (dy1)
            corners.pop(p1)
            corners.pop(p2)
        elif (dy1 == 0 and dy2 == 0):
            size += dx
            #size -= 1 * (corners[p1][1] - corners[p1 - 1][1] + corners[p2][1] - corners[p2 + 1][1])
            corners.pop(p1)
            corners.pop(p2)
        elif dy1 == 0:
            #size -= 1 * (corners[p1][1] - corners[p1 - 1][1])
            corners.pop(p1)
        elif dy2 == 0:
            #size -= 1 * (corners[p2][1] - corners[p2 + 1][1])
            corners.pop(p2)
    else:
        '''Rotate through list'''
        corners.append(corners[0].copy())
        corners.pop(0)
print(size)
print(len(corners))
#if


