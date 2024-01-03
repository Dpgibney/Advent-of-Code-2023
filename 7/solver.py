import functools

def compare(x,y):
    tmpx = x[0]
    tmpy = y[0]
    vals = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    for i in range(len(tmpx)):
        if tmpx[i] != tmpy[i]:
            return vals[tmpx[i]] - vals[tmpy[i]]
    return 0



file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
Lines = file1.readlines()

Five_kind = []
Four_kind = []
Full_house = []
Three_kind = []
Two_pair = []
One_pair = []
High_card = []

for line in Lines:
    line = line.split(" ")
    vals = {}
    for char in line[0]:
        if char in vals:
            vals[char] += 1
        else:
            vals.update({char:1})
    if len(vals) == 5:
        High_card.append((line[0],int(line[1])))
    if len(vals) == 4:
        One_pair.append((line[0],int(line[1])))
    '''Could be either two pair, or three of a kind'''
    if len(vals) == 3:
        three = False
        for char in vals:
            if vals[char] == 3:
                three = True
        if three:
            Three_kind.append((line[0],int(line[1])))
        else:
            Two_pair.append((line[0],int(line[1])))
    '''Could be either full house, or four of a kind'''
    if len(vals) == 2:
        four = False
        for char in vals:
            if vals[char] == 4:
                four = True
        if four:
            Four_kind.append((line[0],int(line[1])))
        else:
            Full_house.append((line[0],int(line[1])))
    if len(vals) == 1:
        Five_kind.append((line[0],int(line[1])))

#Hands = [Five_kind,Four_kind,Full_house,Three_kind,Two_pair,One_pair,High_card]
Hands = [High_card,One_pair,Two_pair,Three_kind,Full_house,Four_kind,Five_kind]
Sorted_Hands = []
for index, hand in enumerate(Hands):
    tmp = sorted(hand,key = functools.cmp_to_key(compare))
    Sorted_Hands.append(tmp)
print(Sorted_Hands)
tmp = 1
value = 0
for cat in Sorted_Hands:
    for hand in cat:
        value += tmp * hand[1]
        tmp += 1

print(value)
