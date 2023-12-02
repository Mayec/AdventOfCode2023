import re

input = open("aoc2023_day1_input.txt", "r")
total = 0
for line in input:
	digits = re.findall(r'\d{1}', line)
	first = digits[0]
	last = digits[-1]
	value = int( str(first) + str(last))
	total += value
print(total)