# Naive solution. Takes too long without converging

import re

def advance(locs, move):
	newlocs = []
	for loc in locs:
		paths = nodes[loc]
		if move == 'L': 
			newlocs.append(paths[0])
		else:
			newlocs.append(paths[1])
	return newlocs

def main():
	#input = open("aoc2023_day8_testinput3.txt", "r")
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
	
	startnodes = [k for k,v in nodes.items() if k[2] == 'A']
	endnodes = [k for k,v in nodes.items() if k[2] == 'Z']
	
	#print(startnodes)
	#print('---')
	#print(endnodes)
	
	
	locs = startnodes #Starting locations
	arrived = False
	steps = 0
	moveidx = 0
	
	#print(locs)
	
	while not arrived:
		move = moves[moveidx]
		locs = advance(locs, move)
		#print(locs)
		steps += 1
		moveidx = (moveidx + 1) % len(moves)
		
		#Check if arrived
		arrived = True
		good = 0
		for loc in locs:
			if not (loc in endnodes):
				arrived = False
				break
		
		#Log progress
		if (steps % 1000000) == 0:
			print('Steps taken (M): ' + str(steps/1000000))
		
	print('Total steps: ' + str(steps))

main()
# Result: 17287