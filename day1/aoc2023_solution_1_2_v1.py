import re

input = open("aoc2023_day1_input.txt", "r")
total = 0
for line in input:
	print(line)
	
	digits = re.findall(r'\d{1}|one|two|three|four|five|six|seven|eight|nine', line)
	
	digits = list(map(lambda x: x.replace("one", "1"),digits))
	digits = list(map(lambda x: x.replace("two", "2"),digits))
	digits = list(map(lambda x: x.replace("three", "3"),digits))
	digits = list(map(lambda x: x.replace("four", "4"),digits))
	digits = list(map(lambda x: x.replace("five", "5"),digits))
	digits = list(map(lambda x: x.replace("six", "6"),digits))
	digits = list(map(lambda x: x.replace("seven", "7"),digits))
	digits = list(map(lambda x: x.replace("eight", "8"),digits))
	digits = list(map(lambda x: x.replace("nine", "9"),digits))
	print(digits)
	
	first = digits[0]
	last = digits[-1]
	value = int( str(first) + str(last))
	print("value: " + str(value))
	
	total += value
	
print("TOTAL: " + str(total))

# 55330 is too low