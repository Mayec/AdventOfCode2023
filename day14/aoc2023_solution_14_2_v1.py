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
			
	return platform


def transpose(platform):
	platform = list(map(list, zip(*platform)))
	return platform


def tiltWest(platform):
	platform = transpose(platform)
	platform = tiltNorth(platform)
	platform = transpose(platform)
	return platform


def tiltSouth(platform):
	platform.reverse()
	platform = tiltNorth(platform)
	platform.reverse()
	return platform

def tiltEast(platform):
	platform = transpose(platform)
	platform.reverse()
	platform = tiltNorth(platform)
	platform.reverse()
	platform = transpose(platform)
	return platform


def cycle(platform):
	platform = tiltNorth(platform)
	platform = tiltWest(platform)
	platform = tiltSouth(platform)	
	platform = tiltEast(platform)
	return platform
		

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
	
	start = platform.copy()
	
	#drawGrid(platform)
	
	loadHistory = []
	cycles = 1000000000
	for n in range(cycles):
		platform = cycle(platform)
		
		load = calcLoad(platform)
		#print('cycle %d: load %d' % (n+1, load))
		
		# Log progress
		#if (n % 1000) == 0:
		#	print('%dK cycles' % int(n/1000))
		
		load = calcLoad(platform)
		loadHistory.append(load)
		
		#detect cycle
		regex = re.compile(r'(.+ .+)( \1)+') 
		
		#(.+ .+) will match at least two numbers (as many as possible) and place the result into 
		# capture group 1. ( \1)+ will match a space followed by the contents of capture group 1, at 
		# least once.
		
		match = regex.search( str(loadHistory) )
		if match:
			print('Found cycle')
			print(match.group(1))
			patternList = match.group(1).split(', ')
			cycleLength = len( patternList )
			print('Length: %d ' % cycleLength)
			iniOffset = n+1
			print('Next Start: %d' % iniOffset)
			break
		#pattern = match.group(1)
		#print(pattern)

	#drawGrid(platform)
	
	# Extrapolate final load from repeated cycle
	allLoops = 1000000000
	loops = (allLoops - iniOffset) / cycleLength
	print('%d full loops' % loops)
	offset = int(loops) * cycleLength
	fullOffset = offset + iniOffset
	print('Last loop start: %d' % fullOffset)
	finalLoadIndex = allLoops - fullOffset
	total = int( patternList[finalLoadIndex] )
	
	#total = calcLoad(platform)
	print('Total load: %d' % total)

main()
# Result: 99875