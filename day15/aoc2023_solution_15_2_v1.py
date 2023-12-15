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


def place(boxes, boxid, label, focal):
	lens = label + ' ' + focal

	#if empty, initialize with new lens
	if len( boxes[boxid] ) == 0: 
		boxes[boxid] = [lens]
		return
	
	#check if lens with this label exists
	found = False
	for l in boxes[boxid]:
		found = label in l
		if found:
			index = boxes[boxid].index(l)
			break
	
	if found:
		boxes[boxid][index] = lens
	else:
		boxes[boxid].append(lens)
	

def remove(boxes, boxid, label):
	found = False
	for lens in boxes[boxid]:
		found = label in lens
		if found:
			index = boxes[boxid].index(lens)
			break
	
	if found:
		del boxes[boxid][index]
	

def focusPower(boxes):
	power = 0
	for nbox in range(len(boxes)):
		for nlens in range(len(boxes[nbox])):
			lens = boxes[nbox][nlens]
			focal = int( lens.split(' ')[1] )
			power += (1 + nbox) * (1 + nlens) * focal
	return power


def main():
	#input = open("aoc2023_day15_testinput.txt", "r")
	input = open("aoc2023_day15_input.txt", "r")
	total = 0

	id_place = 0
	id_remove = 1
	
	steps = input.read().split(',')
	
	# initialize empty boxes 0-255
	boxes = [[]] * 256
	
	for step in steps:
		#print(step)
		
		operation = None
		split = step.split('=')
		if len(split)>1:
			operation = id_place
			label = split[0]
			focal = split[1]
		else:
			operation = id_remove
			label = split[0].split('-')[0]
		
		boxid = hash(label)
		
		if operation == id_place:
			place(boxes, boxid, label, focal)
		else:
			remove(boxes, boxid, label)
	
	#print(boxes)
	
	total = focusPower(boxes)
	
	print('Total: %d' % total)

main()
# Result: 294474