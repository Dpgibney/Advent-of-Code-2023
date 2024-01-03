value = 0

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
Lines = file1.readlines()
cards_won = [1 for i in range(208)]

for index, line in enumerate(Lines):
    print(cards_won[index])
    winning = []
    correct = []
    nums, winners = line.split(":")[1].split("|")
    for n in winners.replace(',',' ').split():
        winning.append(int(n))
    for num in nums.split():
        if int(num) in winning:
            correct.append(int(num))
    for i in range(len(correct)):
        cards_won[index+1+i] += cards_won[index]


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

print(sum(cards_won))


