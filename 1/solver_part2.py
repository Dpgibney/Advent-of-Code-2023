import regex as re

p = re.compile(r'one|two|three|four|five|six|seven|eight|nine|\d',re.IGNORECASE)

value = 0
words = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

file1 = open('p1_input.txt','r')
#file1 = open('p2_input.example','r')
Lines = file1.readlines()

def to_digit(string):
    if string in words:
        return words[string]
    else:
        return int(string)

for line in Lines:
    tmp = re.findall(p,line,overlapped=True)
    value += to_digit(tmp[0]) * 10
    value += to_digit(tmp[-1])

print(value)


