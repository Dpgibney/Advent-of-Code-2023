import re

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')

Lines = file1.read().splitlines()

digits = re.compile(r'\d+')
symbols = re.compile(r'[^\d\.]+')

digits_loc = []
symbols_loc = []

for line in Lines:
    tmp = []
    while True:
        found = re.search(digits,line)
        if found:
            tmp.append(found)
            start, end = found.span()
            line = line[0:start] + ('.' * (end - start)) + line[end:]
        else:
            break
    digits_loc.append(tmp)
    tmp = []
    while True:
        found = re.search(symbols,line)
        if found:
            start, end = found.span()
            tmp.append(start)
            line = line[0:start] + '.' + line[end:]
        else:
            break
    symbols_loc.append(tmp)

ans = 0
for index, nums in enumerate(digits_loc):
    for num in nums:
        loc = num.span()
        loc = (loc[0]-1,loc[1]+1)
        '''Check current line first for symbols then check previous and next line'''
        for symbol in symbols_loc[index]:
            if symbol in range(loc[0],loc[1]):
                ans += int(num[0])
        if index > 0:
            for symbol in symbols_loc[index-1]:
                if symbol in range(loc[0],loc[1]):
                    ans += int(num[0])
        if index < len(digits_loc)-1:
            for symbol in symbols_loc[index+1]:
                if symbol in range(loc[0],loc[1]):
                    ans += int(num[0])

print(ans)
        
