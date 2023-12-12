import re

def drawgrid(grid):
	for row in grid:
		print( ''.join(row) )
	print(' ')

def main():
	#input = open("aoc2023_day11_testinput.txt", "r")
	input = open("aoc2023_day11_input.txt", "r")
	total = 0

	expScale = 1000000

	galaxy = input.read().split('\n')
	
	#drawgrid(galaxy)
	
	#Step 1: expand universe
	#Store expansions of empty rows
	galaxyexp = []
	ExpAcc = 0
	for row in galaxy:
		galaxyexp.append( len(galaxy) * [ExpAcc] )
		charset = ''.join(set(row))		
		if charset == '.':
			ExpAcc += 1
	
	#for row in galaxyexp:
	#	print(row)
	
	galaxycoords = []
	
	# Expand empty cols
	ExpAcc = 0
	for x in range( len(galaxy[0]) ):
		col = ''
		for y in range( len(galaxy) ):
			expx = galaxyexp[y][x]
			galaxyexp[y][x] = (expx, ExpAcc) # record previous accumulated expansions
			s = galaxy[y][x]
			col += (s)
			# if this is a galaxy, add to list of # coordinates
			if s == '#':
				coords = (x, y)
				galaxycoords.append(coords)
		charset = ''.join(set(col))
		if charset == '.':
			# increment expansion
			ExpAcc += 1
	
	#print('Universe expansions:')
	#for row in galaxyexp:
	#	print(row)
	
	for gala in galaxycoords:
		for galb in galaxycoords:
			# base deltas
			dx = abs(gala[0] - galb[0])
			dy = abs(gala[1] - galb[1])
			# expansion deltas
			dxa = galaxyexp[gala[1]][gala[0]][0]
			dxb = galaxyexp[galb[1]][galb[0]][0]
			dya = galaxyexp[gala[1]][gala[0]][1]
			dyb = galaxyexp[galb[1]][galb[0]][1]
			# add expansion deltas to base deltas
			dx += abs(dxa-dxb) * (expScale-1)
			dy += abs(dya-dyb) * (expScale-1)
			
			dist = dx + dy
			total += dist
			#print('Distance between %s and %s is %d' % (gala, galb, dist))
	
	# halve, because counted every distance twice
	total = total/2
	
	print('Result: %d' % total)
	
main()
# Result: 598693078798