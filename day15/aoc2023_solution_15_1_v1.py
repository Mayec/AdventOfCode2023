import re

# HASH algorithm:
# - Determine the ASCII code for the current character of the string.
# - Increase the current value by the ASCII code you just determined.
# - Set the current value to itself multiplied by 17.
# - Set the current value to the remainder of dividing itself by 256.
# - And so on for every character in the string...

def hash(text):
	val = 0
	for c in text:
		val += ord(c) # ascii value
		val *= 17 # mult by 17
		val = val % 256 # remainder of div by 256
	return val


def main():
	#input = open("aoc2023_day15_testinput.txt", "r")
	input = open("aoc2023_day15_input.txt", "r")
	total = 0

	steps = input.read().split(',')
	#print(steps)
	
	for step in steps:
		total += hash(step)
	
	print('Total: %d' % total)

main()
# Result: 511343