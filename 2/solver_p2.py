value = 0

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
Lines = file1.readlines()

#red, green, blue

for index, games in enumerate(Lines):
    max_marbles = {"green":0,"blue":0,"red":0}
    games = games.split(":")
    games = games[1].replace(",","").strip()
    games = games.split(";")
    for game in games:
        tmp = game.split()
        for i in range(len(tmp)-1):
            if i % 2 == 0:
                if max_marbles[tmp[i+1]] < int(tmp[i]):
                    max_marbles[tmp[i+1]] = int(tmp[i])
    value += (max_marbles["green"] * max_marbles["red"] * max_marbles["blue"])

print(value)

