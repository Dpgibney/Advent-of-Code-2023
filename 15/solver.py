file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')

Lines = file1.read().splitlines()

def hash_string(sequence: str) -> int:
    cur_val = 0
    for char in sequence:
        val = ord(char)
        cur_val += val
        cur_val *= 17
        cur_val = cur_val % 256
    return cur_val

boxes = [[] for i in range(256)]

for line in Lines:
    line = line.split(',')
    for sequence in line:
        print(sequence)
        if sequence[-1] == '-':
            label = sequence[:-1]
            hash_val = hash_string(label)
            for i in range(len(boxes[hash_val])):
                if boxes[hash_val][i][0] == label:
                    del boxes[hash_val][i]
                    break
        else:
            label, lens = sequence.split('=')
            hash_val = hash_string(label)
            found = False
            for i in range(len(boxes[hash_val])):
                if boxes[hash_val][i][0] == label:
                    found = True
                    boxes[hash_val][i][1] = int(lens)
            if not found:
                boxes[hash_val].append([label,int(lens)])

        for box in boxes:
            if box != []:
                print(box)

sum = 0
for box_num, box in enumerate(boxes):
    box_num += 1
    for slot_num, slot in enumerate(box):
        slot_num += 1
        sum += (box_num * slot_num * slot[1])
    

print(sum)
