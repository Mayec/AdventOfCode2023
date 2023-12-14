import re


def drawGrid(grid):
	for row in grid:
		print(''.join(row))
	print('')


def tiltNorth(platform):
	stop = [0] * len(platform[0])
	for y in range(len(platform)):
		for x in range(len(platform[y])):
			s = platform[y][x]
			
			#if stone, roll
			if s == 'O':
				endRow = stop[x]
				# roll
				if endRow < y:
					platform[y][x] = '.'
					platform[endRow][x] = 'O'
				# don't roll, just add one to stop
				stop[x] += 1
			
			#if block, this is new stop
			if s == '#':
				stop[x] = y+1
			
	return(platform)


def calcLoad(platform):
	# The amount of load caused by a single rounded rock (O) is equal to the number of rows
	# from the rock to the south edge of the platform, including the row the rock is on.
	# (Cube-shaped rocks (#) don't contribute to load.)
	load = 0
	for y in range(len(platform)):
		for x in range(len(platform[y])):
			s = platform[y][x]
			
			if s == 'O':
				load += len(platform) - y
	return load
	

def main():
	#input = open("aoc2023_day14_testinput.txt", "r")
	input = open("aoc2023_day14_input.txt", "r")
	total = 0

	platform = [list(l) for l in input.read().split('\n')]
	
	#drawGrid(platform)
	
	platform = tiltNorth(platform)
	
	#print('After tilt north:')
	#drawGrid(platform)
	
	total = calcLoad(platform)
	print('Total load: %d' % total)

main()
# Result: 109833