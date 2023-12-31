# This v2 uses a cached recursive function. Otherwise, too slow
# It's faster, but still too slow when doing more than 1000 steps
# Optimization 1: Divide recursions in sets of blocks
# Optimization 2: when a tile is full, remove all it's starting points (failed)

import copy
import time
from functools import cache

def drawGrid(grid):
	for line in grid:
		print(''.join(line))
	print('')


def udim(pos, xwidth, ywidth):
	x = pos[0]
	y = pos[1]	
	ux = int(x / xwidth)
	uy = int(y / ywidth)
	return (ux, uy)


#@cache
def step(themap, positions, steps, udimfull, maxCells):
	reached = []
	xmax = len(themap[0])-1
	ymax = len(themap)-1
	for pos in positions:
		x = pos[0]
		y = pos[1]
		
		# move up
		sx = x % (xmax+1)
		sy = (y-1) % (ymax+1)
		if themap[sy][sx] != '#':
			newx = x
			newy = y-1
			reached.append((newx,newy))
		
		# move right
		sx = (x+1) % (xmax+1)
		sy = y % (ymax+1)
		if themap[sy][sx] != '#':
			newx = x+1
			newy = y
			reached.append((newx,newy))
		
		# move down
		sx = x % (xmax+1)
		sy = (y+1) % (ymax+1)
		if themap[sy][sx] != '#':
			newx = x
			newy = y+1
			reached.append((newx,newy))
		
		# move left
		sx = (x-1) % (xmax+1)
		sy = y % (ymax+1)
		if themap[sy][sx] != '#':
			newx = x-1
			newy = y
			reached.append((newx,newy))
	
	#check full udims
	udims = {}
	reachedus = []
	for pos in reached:
		x = pos[0]
		y = pos[1]
		u = udim(pos, xmax+1, ymax+1)
		reachedus.append(u)
		if u in udims:
			udims[u] += 1
		else:
			udims[u] = 1
		if udims[u] > maxCells:
			udimfull.add(u)
	
	reachedfiltered = []
	#Cull reached in full udims
	for i in range(len(reached)):
		if reachedus[i] not in udimfull:
			reachedfiltered.append(reached[i])
	
	reached = tuple(set(reachedfiltered))
	
	fullus = len(reachedus)
	if steps > 1:
		final, fullus = step(themap, reached, steps-1, udimfull, maxCells)
	else:
		final = reached
	
	return (final, fullus * maxCells)


def main():
	input = open("aoc2023_day21_testinput.txt", "r")
	#input = open("aoc2023_day21_input.txt", "r")
	total = 0

	mymap = [tuple(list(line)) for line in input.read().split('\n')]
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
	
	steps = 6
	blocksize = 1
	blocks = int(steps / blocksize)
	udimfull = set()
	tfullus = 0
	
	start = time.time()
	blocks = 1
	for b in range(blocks):
		elapsed = time.time() - start
		print('Block %d (%ds)' % ((b+1), elapsed))
		print('%d positions' % len(positions))
		positions, fullus = step(tuple(mymap), tuple(positions), blocksize, udimfull, maxPlots) # <-- tuples are hashable, for caching
		tfullus += fullus
		
	total = len(positions) + tfullus*maxPlots
	print(total)
	

main()
# Result: 3841