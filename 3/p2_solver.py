import re

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')

Lines = file1.read().splitlines()

digits = re.compile(r'\d+')
symbols = re.compile(r'\*')

digits_loc = []
symbols_loc = []

for index, line in enumerate(Lines):
    tmp = []
    while True:
        found = re.search(digits,line)
        if found is not None:
            tmp.append(found)
            start, end = found.span()
            line = line[0:start] + ('.' * (end - start)) + line[end:]
        else:
            break
    digits_loc.append(tmp)
    tmp = []
    line = line.replace('.','1')
    while True:
        found = re.search(symbols,line)
        if found is not None:
            start, end = found.span()
            tmp.append(start)
            line = line[0:start] + ('1' * (end - start + 1)) + line[end+1:]
        else:
            break
    symbols_loc.append(tmp)

gear_adj = []
for index, nums in enumerate(digits_loc):
    for num in nums:
        loc = num.span()
        loc = (loc[0]-1,loc[1]+1)
        '''Check current line first for symbols then check previous and next line'''
        for symbol in symbols_loc[index]:
            if symbol in range(loc[0],loc[1]):
                gear_adj.append((int(num[0]),index,symbol))
        if index > 0:
            for symbol in symbols_loc[index-1]:
                if symbol in range(loc[0],loc[1]):
                    gear_adj.append((int(num[0]),index-1,symbol))
        if index < len(digits_loc)-1:
            for symbol in symbols_loc[index+1]:
                if symbol in range(loc[0],loc[1]):
                    gear_adj.append((int(num[0]),index+1,symbol))

print(gear_adj)

ans = 0
for index, s1 in enumerate(gear_adj):
    for s2 in gear_adj[index+1:]:
        if s1[1] == s2[1] and s1[2] == s2[2]:
            print(s1,s2)
            ans += s1[0] * s2[0]

print(ans)
