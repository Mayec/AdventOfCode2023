import re

input = open("aoc2023_day2_input.txt", "r")
total = 0

# Games possible with 12 red cubes, 13 green cubes, and 14 blue cubes.
conditions = {
	"red": 12,
	"green": 13,
	"blue": 14
}

for line in input:
	print(line)
	
	game = line.split(":")
	gameId = game[0].split(" ")[1]
	print("Game: " + gameId)
	
	valid = True
	samples = game[1].split(";")
	for sample in samples:
		print ("---sample---")
		
		for color in conditions.keys():
			max = conditions[color]		
			match = re.search(r'\d* '+color, sample)
			if match:
				stringColor = match.group()
				amountColor = int(stringColor.split(" ")[0])
				print(color + ": " + str(amountColor))
				if amountColor > max:
					valid = False
	print("Valid: " + str(valid))
	
	if valid:
		total += int(gameId);

# What is the sum of the IDs of those games?
print(total);

# Correct answer: 2476