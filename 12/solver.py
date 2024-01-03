import re

file1 = open('p1_input.example','r')
file1 = open('p1_input.txt','r')
Lines = file1.read().splitlines()

possibilities = 0
for line in Lines:
    tmp = 0
    '''Count ? marks'''
    marks = 0
    for char in line:
        if char == '?':
            marks += 1

    '''Create regular expression for this line'''
    dmg_springs = line.split()[1].replace(',',' ')
    dmg_springs = dmg_springs.split()
    #print(dmg_springs)
    re_str = "\.*"
    for group in dmg_springs:
        for i in range(int(group)):
            re_str += '#'
        re_str += '\.+'
    '''Since it will always end with .+ alter the + to *'''
    re_str = re_str[:len(re_str)-1] + '*' + '\Z'
    #print(re_str)
    prog = re.compile(re_str)

    '''iterate through every possible ? possibility'''
    print("Original: ",line.split()[0])
    for i in range(2**marks):
        pos_str = line.split()[0]
        num_found = 0
        for index, char in enumerate(pos_str):
            if char =='?':
                bit_mask = 2**num_found
                num_found += 1
                if (i & bit_mask) != 0:
                    pos_str = pos_str[:index] + '.' + pos_str[index+1:]
                else:
                    pos_str = pos_str[:index] + '#' + pos_str[index+1:]
        if re.match(re_str,pos_str) is not None:
            tmp += 1
            #print(re.match(re_str,pos_str))
        #print(pos_str)
    possibilities += tmp
    print(tmp)
print(possibilities)
