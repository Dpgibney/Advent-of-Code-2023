import numpy as np

file1 = open('p1_input.example','r')
file1 = open('p1_input.txt','r')

Lines = file1.read().splitlines()

'''Direction of travel'''
right = 0
down = 1
left = 2
up = 3

'''Movement dictionary'''
movement = {0:[0,1], 1:[1,0], 2:[0,-1], 3:[-1,0]}

def light_beam(position: list, direction: int) -> int:
    while (0 <= position[0] and position[0] < len(layout)) and (0 <= position[1] and position[1] < len(layout[0])):
        key = (tuple(position),direction)
        if key in visited:
            return 0
        visited.update({key: 0})
        intensity[position[0]][position[1]] += 1
        '''Check for mirrors'''
        if layout[position[0]][position[1]] == '/':
            if   direction == 0: direction = 3
            elif direction == 1: direction = 2
            elif direction == 2: direction = 1
            elif direction == 3: direction = 0
        elif layout[position[0]][position[1]] == '\\':
            if   direction == 0: direction = 1
            elif direction == 1: direction = 0
            elif direction == 2: direction = 3
            elif direction == 3: direction = 2
        elif layout[position[0]][position[1]] == '|':
            if   direction == 0:
                light_beam([position[0] - 1,position[1]], 3)
                light_beam([position[0] + 1,position[1]], 1)
                return 0
            elif direction == 2:
                light_beam([position[0] - 1,position[1]], 3)
                light_beam([position[0] + 1,position[1]], 1)
                return 0
        elif layout[position[0]][position[1]] == '-':
            if   direction == 1:
                light_beam([position[0],position[1] - 1], 2)
                light_beam([position[0],position[1] + 1], 0)
                return 0
            elif direction == 3:
                light_beam([position[0],position[1] - 1], 2)
                light_beam([position[0],position[1] + 1], 0)
                return 0
        position[0] += movement[direction][0]
        position[1] += movement[direction][1]

layout = []
for line in Lines:
    tmp = []
    for char in line:
        tmp.append(char)
    layout.append(tmp)

intensity = [[0 for j in range(len(layout[i]))] for i in range(len(layout))]
visited = {}

max = 0
'''Check from top and bottom first'''
for i in range(len(layout[0])):
    print(i)
    intensity = [[0 for j in range(len(layout[i]))] for i in range(len(layout))]
    visited = {}
    light_beam([0,i], 1)
    intensity = np.array(intensity)
    tmp = len(np.where(intensity > 0)[0])
    if tmp > max:
        max = tmp

    intensity = [[0 for j in range(len(layout[i]))] for i in range(len(layout))]
    visited = {}
    light_beam([len(layout),i], 3)
    intensity = np.array(intensity)
    tmp = len(np.where(intensity > 0)[0])
    if tmp > max:
        max = tmp

'''Check from left and right'''
for i in range(len(layout)):
    print("left right: ",i)
    intensity = [[0 for j in range(len(layout[i]))] for i in range(len(layout))]
    visited = {}
    light_beam([i,0], 0)
    intensity = np.array(intensity)
    tmp = len(np.where(intensity > 0)[0])
    if tmp > max:
        max = tmp

    intensity = [[0 for j in range(len(layout[i]))] for i in range(len(layout))]
    visited = {}
    light_beam([i,len(layout[0])], 0)
    intensity = np.array(intensity)
    tmp = len(np.where(intensity > 0)[0])
    if tmp > max:
        max = tmp

print(max)

#print(np.array(layout))
#layout = np.array(layout)
#print(np.array(intensity))
#intensity = np.array(intensity)
#print(len(np.where(intensity > 0)[0]))



