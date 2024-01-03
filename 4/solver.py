value = 0

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
Lines = file1.readlines()

for index, line in enumerate(Lines):
    winning = []
    correct = []
    nums, winners = line.split(":")[1].split("|")
    for n in winners.replace(',',' ').split():
        winning.append(int(n))
    for num in nums.split():
        if int(num) in winning:
            correct.append(int(num))
    if len(correct) > 0:    
        value += 2**(len(correct)-1)


    #liner = line[::-1]
    #'''Find first digit'''
    #first_d = None
    #for char in line:
    #    if char.isdigit():
    #        first_d = int(char)*10
    #        break

    #'''Find second digit'''
    #second_d = None
    #for char in liner:
    #    if char.isdigit():
    #        second_d = int(char)
    #        break

    #values.append(first_d+second_d)
    #print(first_d+second_d)


print(value)

