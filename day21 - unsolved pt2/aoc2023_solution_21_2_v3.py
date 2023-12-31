# This v2 uses a cached recursive function. Otherwise, too slow
# It's faster, but still too slow when doing more than 1000 steps
# Optimization: when a tile is full, remove all it's starting points

import copy, math

def drawGrid(grid):
	for line in grid:
		print(''.join(line))
	print('')


def udim(pos, xwidth, ywidth):
	x = pos[0]
	y = pos[1]	
	ux = math.floor(x / xwidth)
	uy = math.floor(y / ywidth)
	return (ux, uy)


def step(themap, positions, udimfull, maxCells):
	reached = []
	for pos in positions:
		x = pos[0]
		y = pos[1]
		xmax = len(themap[0])-1
		ymax = len(themap)-1
		
		# move up
		sx = x % (xmax+1)
		sy = (y-1) % (ymax+1)
		symbol = themap[sy][sx]
		if symbol != '#':
			newx = x
			newy = y-1
			reached.append((newx,newy))
		
		# move right
		sx = (x+1) % (xmax+1)
		sy = y % (ymax+1)
		symbol = themap[sy][sx]
		if symbol != '#':
			newx = x+1
			newy = y
			reached.append((newx,newy))
		
		# move down
		sx = x % (xmax+1)
		sy = (y+1) % (ymax+1)
		symbol = themap[sy][sx]
		if symbol != '#':
			newx = x
			newy = y+1
			reached.append((newx,newy))
		
		# move left
		sx = (x-1) % (xmax+1)
		sy = y % (ymax+1)
		symbol = themap[sy][sx]
		if symbol != '#':
			newx = x-1
			newy = y
			reached.append((newx,newy))
	
	#check full udims
	udims = {}
	
	reached = list(set(reached))
	reachedus = []
	
	for pos in reached:
		x = pos[0]
		y = pos[1]
		u = udim(pos, xmax+1, ymax+1)
		#reachedus.append(u)
		if u in udims:
			udims[u] += 1
		else:
			udims[u] = 1
		if udims[u] >= 0.5 * maxCells:
			udimfull.add(u)
	
	print('udimfull count: %d' % len(udimfull))
	print(udimfull)
	
	# cull positions from full udims
	cullcells = []
	for pos in reached:
		x = pos[0]
		y = pos[1]
		u = udim(pos, xmax+1, ymax+1)
		if u in udimfull:
			cullcells.append(pos)
	for cullcell in cullcells:
		reached.remove(cullcell)
	print(len(cullcells))
	print(cullcells)
	
	#print('full udims: %d' % len(udimfull))
	#print(udimfull)
	
	reached = set(reached)
	return reached, udimfull


def main():
	input = open("aoc2023_day21_testinput.txt", "r")
	#input = open("aoc2023_day21_input.txt", "r")
	total = 0

	mymap = [list(line) for line in input.read().split('\n')]
	drawGrid(mymap)
	maxPlots = 0
	for y in range(len(mymap)):
		for x in range(len(mymap[0])):
			symbol = mymap[y][x]
			if symbol == 'S':
				start = (x,y)
			if symbol != '#':
				maxPlots += 1
	positions = [start]
	
	print('maPlots: %d' % maxPlots)
	
	steps = 1
	
	udimfull = set()
	while steps > 0:
		positions, udimfull = step(mymap, positions, udimfull, maxPlots)
		steps -= 1
		#maplive = copy.deepcopy(mymap)
		for pos in positions:
			x = pos[0]
			y = pos[1]
			
			#maplive[y][x] = 'O'
		#drawGrid(maplive)
	
	total = len(positions)
	print(total)
	print(len(udimfull)*maxPlots)
	print(len(udimfull)*0.5*maxPlots + total)
	

main()
# Result: 3841