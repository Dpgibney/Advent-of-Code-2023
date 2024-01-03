file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
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
cur_nod = 'AAA'
order_step = 0
while cur_nod != 'ZZZ':
    print(cur_nod,Nodes[cur_nod])
    if order[order_step] == 'L':
        cur_nod = Nodes[cur_nod][0]
    else:
        cur_nod = Nodes[cur_nod][1]
    steps += 1
    order_step += 1
    if order_step == len(order):
        order_step = 0
print(steps-1)
