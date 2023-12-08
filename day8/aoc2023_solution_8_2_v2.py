# Trying to optimize on v1, which was naive solution
# We check how many cycles per starting location, then calculate their
# least common multiple. This should be the total number of cycles we
# need to do for them all to arrive simultaneously.

import re
import math

def advance(locs, move):
	newlocs = []
	for loc in locs:
		paths = nodes[loc]
		if move == 'L': 
			newlocs.append(paths[0])
		else:
			newlocs.append(paths[1])
	return newlocs
	
# Least Common Multiple of n numbers. Brute force, takes too long. Using math.lcm instead
def lcm1(numbers):
	numbers.sort(reverse=True)
	greater = numbers[0]
	
	found = False
	while(not found):
		modtotal = 0
		for n in numbers:
			modtotal += greater % n
		if modtotal == 0:
			found = True
		else:
			greater += 1
		
		#Log progress
		if (greater % 1000000) == 0:
			print('Checked (M): ' + str(greater/1000000))
		
	return greater


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
	endcycles = []
	#print(locs)
	
	# Find how many cycles each start location needs to reach an end location
	# Store each one's total steps in endcycles list
	for loc in startnodes:
		startloc = loc
		#print(startloc)
		
		moveidx = 0
		steps = 0
		arrived = False
		
		while not arrived:
			move = moves[moveidx]
			loc = advance([loc], move)[0]
			#print(loc)
			steps += 1
			moveidx = (moveidx + 1) % len(moves)
			
			#Check if arrived
			if loc in endnodes:
				arrived = True

			#Log progress
			if (steps % 1000000) == 0:
				print('Steps taken (M): ' + str(steps/1000000))
				
		cycles = steps / len(moves)
		if steps % len(moves) != 0:
			print('ERROR: number of cycles not an integer')
			exit()
		endcycles.append(int(cycles))
		print(startloc + ' arrived to ' + loc + ' in ' + str(steps) + ' steps (' + str(cycles) + ' cycles)')
	
	totalcycles = math.lcm(*endcycles)
	print('lcm is ' + str(totalcycles) + ' cycles')
	# from online calculator, lcm should be 63,568,204,859
	#totalcycles = 63568204859
	total = totalcycles * len(moves)
	
	print('Total steps for simultaneous convergence: ' + str(total))

main()
# Result: 18625484023687