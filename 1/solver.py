value = 0
file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
Lines = file1.readlines()

for line in Lines:
    liner = line[::-1]
    '''Find first digit'''
    for char in line:
        if char.isdigit():
            value += int(char)*10
            break

    '''Find second digit'''
    for char in liner:
        if char.isdigit():
            value += int(char)
            break

print(value)


