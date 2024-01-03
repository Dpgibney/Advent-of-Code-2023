file1 = open('p1_input.txt','r')
#file1 = open('p2_input.example','r')
Lines = file1.readlines()

order = Lines[0].strip()
Lines = Lines[2:]

Nodes = {}

for line in Lines:
    line = line.split("=")
    key = line[0].strip()
    L = line[1][2:5]
    R = line[1][7:10]
    Nodes.update({key:(L,R)})

steps = 1
cur_nods = []
for node in Nodes:
    if node[2] == 'A':
        cur_nods.append(node)
order_step = 0
multiples = [[] for i in range(len(cur_nods))]

while steps < 100000:
    print(steps)
    Solved = True
    #print(cur_nods)
    #print(order[order_step])
    #for nod in cur_nods:
    #    print(nod,Nodes[nod])
    for index, node in enumerate(cur_nods):
        if node[2] != 'Z':
            Solved = False
        else:
            multiples[index].append(steps-1)

    if Solved:
        print(steps-1)
        exit()

    for node_index in range(len(cur_nods)):
        if order[order_step] == 'L':
            #print(Nodes[cur_nods[node_index]][0])
            cur_nods[node_index] = Nodes[cur_nods[node_index]][0]
        else:
            #print(Nodes[cur_nods[node_index]][1])
            cur_nods[node_index] = Nodes[cur_nods[node_index]][1]
    steps += 1
    order_step += 1
    if order_step == len(order):
        order_step = 0
print(steps-1)
print(multiples)
