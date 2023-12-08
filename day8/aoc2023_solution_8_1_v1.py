import re

def advance(loc, move):
	paths = nodes[loc]
	if move == 'L': 
		return paths[0]
	else:
		return paths[1]
	

def main():
	#input = open("aoc2023_day8_testinput.txt", "r")
	#input = open("aoc2023_day8_testinput2.txt", "r")
	input = open("aoc2023_day8_input.txt", "r")

	moves, nodestrs = input.read().split('\n\n')
	nodestrs = nodestrs.split('\n')
	
	# Store nodes data as a dictionary
	global nodes
	nodes = {}
	for s in nodestrs:
		s = s.split(' = ')
		s[1] = s[1][1:-1].split(', ')
		nodes[s[0]] = s[1]
	
	#print(moves)
	#print(nodes)
	
	loc = 'AAA' #Starting location
	steps = 0
	moveidx = 0
	
	print(loc)
	while loc != 'ZZZ':
		move = moves[moveidx]
		loc = advance(loc, move)
		#print(loc)
		steps += 1
		moveidx = (moveidx + 1) % len(moves)
	
	print('Total steps: ' + str(steps))

main()
# Result: 17287