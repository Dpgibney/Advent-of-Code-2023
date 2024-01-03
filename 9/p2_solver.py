file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
Lines = file1.readlines()

def not_zero(numbers: list) -> bool:
    for val in numbers:
        if val != 0:
            return True
    return False

def gen_history(sequence: list) -> list:
    while True:
        tmp = []
        for i in range(len(sequence[-1]) - 1):
            tmp.append(sequence[-1][i+1] - sequence[-1][i])
        sequence.append(tmp)
        if len(sequence[-1]) == 1:
            sequence.append([0])
            return sequence
        if not not_zero(sequence[-1]):
            return sequence

def next_value(sequences: list) -> int:
    sequences = sequences[::-1]
    for index, sequence in enumerate(sequences):
        if index < len(sequences) - 1:
            sequences[index+1].insert(0,sequences[index + 1][0] - sequence[0])
        if index == len(sequences) - 1:
            return sequences[-1][0]
            

sequences = []
for line in Lines:
    line = line.split()
    row = []
    for item in line:
        row.append(int(item))
    sequences.append([row])
    #while not_zero

for sequence in range(len(sequences)):
    sequences[sequence] = gen_history(sequences[sequence])
#print(sequences)

val = 0
for sequence in sequences:
    print(sequence)
    val += next_value(sequence)
print(val)


