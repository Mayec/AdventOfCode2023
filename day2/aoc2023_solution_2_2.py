import re

input = open("aoc2023_day2_input.txt", "r")
total = 0

colors =  ["red", "green", "blue"]

for line in input:
	print(line)
	
	game = line.split(":")
	gameId = game[0].split(" ")[1]
	print("Game: " + gameId)
	
	maximums = [0,0,0]
	samples = game[1].split(";")
	for sample in samples:
		print ("---sample---")
		
		for i in range(len(colors)):
			color = colors[i]	
			match = re.search(r'\d* '+color, sample)
			if match:
				stringColor = match.group()
				amountColor = int(stringColor.split(" ")[0])
				print(color + ": " + str(amountColor))
				
				maximums[i] = max(maximums[i], amountColor)
	print("Maximums found: " + str(maximums))

	#The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
	power = 1
	for i in range(len(colors)):
		power *= maximums[i]
	print("Power: " + str(power))
	
	total += power
	
# What is the sum of the power of these sets?
print(total);

# Result: 54911