import re

file1 = open('p1_input.example','r')
file1 = open('p1_input.txt','r')
Lines = file1.read().splitlines()

def check_match(str_input: str, dmg_springs: list) -> int:
    if dmg_springs == []:
        for char in str_input:
            if char == '#':
                return 0
        return 1

    pattern = '^\.*#+\.'
    check = re.search(pattern,str_input)
    if check is not None:
        tmp = 0
        for char in check[0]:
            if char == '#':
                tmp += 1
        if tmp != int(dmg_springs[0]):
            return 0

    #tmp = 0
    #for char in str_input:
    #    if char == '#' or char == '?':
    #        tmp += 1
    #for val in dmg_springs:
    #    tmp -= int(val)
    #tmp -= (len(dmg_springs) - 1)
    #if tmp < 0:
    #    return 0

    pattern = '^\.*'
    for i in range(int(dmg_springs[0])):
        pattern = pattern + '#'
    pattern = pattern + "\.|" + pattern + '\Z'

    str_dot = str_input
    str_pound = str_input
    found = False
    for index, char in enumerate(str_input):
        if char == '?':
            str_dot = str_input[:index] + '.' + str_input[index+1:]
            str_pound = str_input[:index] + '#' + str_input[index+1:]
            found = True
            break
   
    '''Same string if not found'''
    if not found:
        results = re.search(pattern,str_dot)
        if results is not None:
            return check_match(str_dot[len(results[0]):],dmg_springs[1:])
    results_dot = re.search(pattern,str_dot)
    results_pound = re.search(pattern,str_pound)
    if (results_dot is not None) and (results_pound is not None):
        return check_match(str_dot[len(results_dot[0]):],dmg_springs[1:]) + check_match(str_pound[len(results_pound[0]):],dmg_springs[1:])
    elif results_dot is not None:
        return check_match(str_dot[len(results_dot[0]):],dmg_springs[1:]) + check_match(str_pound,dmg_springs)
    elif results_pound is not None:
        return check_match(str_pound[len(results_pound[0]):],dmg_springs[1:]) + check_match(str_dot,dmg_springs)
    elif not found:
        return 0
    else:
        return check_match(str_dot,dmg_springs) + check_match(str_pound,dmg_springs)
    

possibilities = 0
for line_num, line in enumerate(Lines):
    if line_num % 4 == 3:
        print(line_num)
        '''Create regular expression for this line'''
        dmg_springs = line.split()[1].replace(',',' ')
        dmg_springs = dmg_springs.split()
        dmg_springs = dmg_springs*5

        '''iterate through every possible ? possibility'''
        line = line.split()[0]
        #line = line + '?'
        #marks = 0
        #for char in line:
        #    if char == '?':
        #        marks += 1
        line = line + '?' + line + '?' + line + '?' + line + '?' + line
        print(line)
        print(dmg_springs)
            
        
        
        #print(line)
        tmp = check_match(line,dmg_springs)
        print(tmp)
        possibilities += tmp
        #tmp = 0
        #for block in line:
        #    '''Count ? marks'''
        #    marks = 0
        #    for char in block:
        #        if char == '?':
        #            marks += 1
        #    block_pos = 0
        #    for i in range(2**marks):
        #        pos_str = line.split()[0]
        #        num_found = 0
        #        for index, char in enumerate(pos_str):
        #            if char =='?':
        #                bit_mask = 2**num_found
        #                num_found += 1
        #                if (i & bit_mask) != 0:
        #                    pos_str = pos_str[:index] + '.' + pos_str[index+1:]
        #                else:
        #                    pos_str = pos_str[:index] + '#' + pos_str[index+1:]
        #        if re.match(re_str,pos_str) is not None:
        #            block_pos += 1
        #        #print(re.match(re_str,pos_str))
        #    #print(pos_str)
print(possibilities)
