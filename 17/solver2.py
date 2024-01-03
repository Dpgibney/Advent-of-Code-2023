from heapq import heappop, heappush
file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')

Lines = file1.read().splitlines()

mapped = []
'''Order is up, right, down, left'''
DIR = [[-1,0],[0,1],[1,0],[0,-1]]

for line in Lines:
    tmp = []
    for char in line:
        tmp.append(char)
    mapped.append(tmp)

costs = {}
visited = set()
# cost, x, y, invalid direction. Includes both sides of direction
Q = [(0,0,0,-1)]

def in_map(pos,mapped):
    return pos[0] in range(len(mapped)) and pos[1] in range(len(mapped[pos[0]]))

while Q:
    cost, x, y, inv_dir = heappop(Q)
    
    '''If in bottom right corner we found it'''
    if x == len(mapped) - 1 and y == len(mapped[x]) - 1:
        print(cost)
        exit()
    if (x,y,inv_dir) in visited:
        pass
    else:
        visited.add((x,y,inv_dir))
        '''Propagate out from current position along available axis'''
        for direction in range(4):
            heat_change = 0
            if direction == inv_dir or (direction - 2) % 4 == inv_dir:
                pass
            else:
                for dist in range(1,11):
                    x2 = x + dist * DIR[direction][0]
                    y2 = y + dist * DIR[direction][1]
                    if in_map((x2,y2),mapped):
                        heat_change += int(mapped[x2][y2])
                        adj_val = cost + heat_change
                        if dist > 3:
                            if costs.get((x2,y2,direction),1000000000) > adj_val:
                                costs[(x2,y2,direction)] = adj_val
                            heappush(Q, (adj_val,x2,y2,direction))
exit()
#
#
#    #print(np.array(dist)-last)
#    last = np.array(dist)
#    '''Find minimum dist vertex'''
#    min_val = inf + 1
#    min_loc = [0,0,0]
#    for vertex in Q:
#        if min_val > dist[vertex[0]][vertex[1]][vertex[2]]:
#            min_loc[0] = vertex[0]
#            min_loc[1] = vertex[1]
#            min_loc[2] = vertex[2]
#            min_val = dist[vertex[0]][vertex[1]][vertex[2]]
#
#    #print(Q.index((min_loc[0],min_loc[1])))
#    #print(min_val)
#    del Q[Q.index((min_loc[0],min_loc[1],min_loc[2]))]
#    #print(Q)
#    #print(dist)
#
#    tmp = min_loc.copy()
#    mov_dir = tmp[2]
#    x = tmp[0] + dir_mov[mov_dir][0]
#    y = tmp[1] + dir_mov[mov_dir][1]
#    print("moved to spot: ",tmp)
#        
#    '''Still in map'''
#    if (0 <= x and x < len(mapped)) and (0 <= y and y < len(mapped[x])):
#        alt_dist = min_val + int(mapped[x][y])
#        is_line = True
#        '''Check that the previous three nodes don't form a line'''
#        for i in range(3):
#            x2, y2, _ = min_loc.copy()
#            x2 = x2 - (dir_mov[mov_dir][0]*i)
#            y2 = y2 - (dir_mov[mov_dir][1]*i)
#            if (0 > x2 or x2 >= len(mapped)) or (0 > y2 or y2 >= len(mapped[x2])):
#                is_line = False
#                break
#            elif dist[x2][y2][mov_dir] == inf:
#                is_line = False
#                break
#
#        if not is_line:
#            for i in range(4):
#                if i == mov_dir:
#                    if dist[x][y][mov_dir] > alt_dist:
#                        dist[x][y][mov_dir] = alt_dist
#                else:
#                    if dist[x][y][i] == inf:
#                        dist[x][y][i] -= 1
#        else:
#            tmp = dist[x][y][:mov_dir] + dist[x][y][mov_dir+1:]
#            tmp = min(tmp)
#            if tmp < 10000:
#                dist[x][y][mov_dir] = tmp
#
#
#        #else:
#        #    min_dist = min(dist[x][y][:mov_dir] + dist[x][y][mov_dir+1:])
#        #    if alt_dist < min_dist:
#        #        dist[x][y][mov_dir] = alt_dist
#
##print(np.array(prev))
#print(np.array(dist))
#print(dist[12][12])
#
#display = dist.copy()
#x,y = 12,12
#while prev[x][y] is not None:
#    display[x][y] = 0
#    x,y = prev[x][y][0]
#
#print(np.array(display))


    
