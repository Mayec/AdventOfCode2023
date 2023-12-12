import re

def drawgrid(grid):
	for row in grid:
		print( ''.join(row) )
	print(' ')

def main():
	#input = open("aoc2023_day11_testinput.txt", "r")
	input = open("aoc2023_day11_input.txt", "r")
	total = 0

	galaxy = input.read().split('\n')
	galaxyexp = []
	
	#Step 1: expand universe
	# Expand empty rows
	emptyrow = len(galaxy[0]) * '.'
	for row in galaxy:
		galaxyexp.append(list(row))
		charset = ''.join(set(row))		
		if charset == '.':
			galaxyexp.append(list(emptyrow))
	
	#drawgrid(galaxyexp)
	
	galaxycoords = []
	
	# Expand empty cols
	added = 0
	for x in range( len(galaxyexp[0]) ):
		scanx = x + added
		col = ''
		for y in range( len(galaxyexp) ):
			s = galaxyexp[y][scanx]
			col += (s)
			# if this is a galaxy, add to list of # coordinates
			if s == '#':
				coords = (scanx, y)
				galaxycoords.append(coords)
		charset = ''.join(set(col))
		if charset == '.':
			# add new empty column
			for i in range( len(galaxyexp) ):
				galaxyexp[i].insert(scanx, '.')
			added += 1
	
	print('Expanded universe:')
	drawgrid(galaxyexp)
	
	for gala in galaxycoords:
		for galb in galaxycoords:
			dx = abs(gala[0] - galb[0])
			dy = abs(gala[1] - galb[1])
			dist = dx + dy
			total += dist
			#print('Distance between %s and %s is %d' % (gala, galb, dist))
	
	# halve, because counted every distance twice
	total = total/2
	
	print('Result: %d' % total)
	
main()
# Result: 10276166