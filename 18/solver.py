import numpy as np

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')

dir_map = {"R": np.array([0,1]), "L": np.array([0,-1]), "U": np.array([-1,0]), "D": np.array([1,0])}
fill_map = {"R": np.array([1,0]), "L": np.array([-1,0]), "U": np.array([0,1]), "D": np.array([0,-1])}
#fill_map = {"R": np.array([-1,0]), "L": np.array([1,0]), "U": np.array([0,-1]), "D": np.array([0,1])}

def in_grid(pos,grid):
    return pos[0] in range(len(grid)) and pos[1] in range(len(grid[pos[0]]))

def fill(distance, pos, direction, grid):
    for i in range(1,distance+1):
        pos = pos + dir_map[direction]
        new_pos = pos + fill_map[direction]
        while True:
            if grid[new_pos[0],new_pos[1]] != '*':
                grid[new_pos[0],new_pos[1]] = '#'
                new_pos = new_pos + fill_map[direction]
            else:
                break


dig_plan = [[group for group in line.split()] for line in file1.read().splitlines()]

lagoon = np.array([['*']])

pos = [0,0]
#origin = [0,0]
for dig in dig_plan:
    direction, distance, color = dig
    distance = int(distance)
    color = color[1:-1]

    for movement in range(1,distance+1):
        pos = pos + dir_map[direction]
        
        if in_grid(pos,lagoon) == False:
            if direction == "R":
                ncols = len(lagoon[0])
                lagoon = np.insert(lagoon, ncols, '.', axis=1)
            elif direction == 'L':
                lagoon = np.insert(lagoon, 0, '.', axis = 1)
                pos[1] += 1
                #origin[1] += 1
            elif direction == "D":
                nrows = len(lagoon)
                lagoon = np.insert(lagoon, nrows, '.', axis = 0)
            elif direction == 'U':
                lagoon = np.insert(lagoon, 0, '.', axis = 0)
                pos[0] += 1
                #origin[0] += 1
        #print(pos)

        lagoon[pos[0],pos[1]] = '*'
        #print(lagoon)

#np.savetxt('tmp.txt',lagoon, fmt='%c')
#exit()
#pos = [0,0]
print(pos)
#print(origin)
for dig_index, dig in enumerate(dig_plan):
    direction, distance, color = dig
    distance = int(distance)
    color = color[1:-1]

    fill(distance, pos.copy(), direction, lagoon)
    pos = pos + (distance * dir_map[direction])
    if dig_index < len(dig_plan)-1:
        pos = pos - dir_map[dig_plan[dig_index+1][0]]
        fill(1, pos.copy(), dig_plan[dig_index+1][0], lagoon)
        pos = pos + dir_map[dig_plan[dig_index+1][0]]

print(lagoon)

np.savetxt('tmp.txt',lagoon, fmt='%c')

count = 0
for i in range(len(lagoon)):
    for j in range(len(lagoon[0])):
        if lagoon[i][j] == '*' or lagoon[i][j] == '#':
            count += 1
print(count)
