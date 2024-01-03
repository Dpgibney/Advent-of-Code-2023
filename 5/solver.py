import re
values = []

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
Lines = file1.readlines()

old_seeds = []
new_seeds = []
p = re.compile('[a-zA-Z]+')

for index, line in enumerate(Lines):
    print(old_seeds)
    if index == 0:
        line = line.split(":")
        sds = line[1].split()
        for i in range(len(sds)//2):
            old_seeds.append((int(sds[2*i]),int(sds[2*i])+int(sds[2*i+1])))
    else:
        '''Reset seeds'''
        if line == '\n':
            for i in old_seeds:
                new_seeds.append(i)
            old_seeds = new_seeds
            new_seeds = []
        elif re.search(p,line) is None:
            line = line.split()
            dest = int(line[0])
            source = int(line[1])
            rang = int(line[2])
            to_remove = []
            for seed in old_seeds:
                print(seed)
                print(dest,source,rang)
                '''lets start with the bound completely encompass the original range'''
                if seed[0] >= source and seed[1] < (source +  rang):
                    new_seeds.append((seed[0] + dest - source,seed[1] + dest - source))
                    to_remove.append(seed)
                elif seed[0] < source and seed[1] > (source + rang):
                    new_seeds.append((dest,dest + rang))
                    to_remove.append(seed)
                    old_seeds.append((seed[0],source-1))
                    old_seeds.append((seed[1]+1,dest+rang))
                elif seed[1] > source and seed[1] < (source + rang):
                    new_seeds.append((dest,seed[1] + dest - source))
                    to_remove.append(seed)
                    '''add remaining to the end of the list'''
                    old_seeds.append((seed[0],source-1))
                elif seed[0] > source and seed[0] < (source + rang):
                    new_seeds.append((seed[0] + dest - source, dest + rang))
                    to_remove.append(seed)
                    '''add remaining to the end of the list'''
                    old_seeds.append((source + rang,seed[1]))
            for seed in to_remove:
                old_seeds.remove(seed)

print(old_seeds)
print(new_seeds)
#print(min(old_seeds))
print(min(new_seeds))

