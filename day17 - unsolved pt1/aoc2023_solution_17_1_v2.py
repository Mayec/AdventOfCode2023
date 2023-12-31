# Using Dijkstra's algorithm, with additional constraints
# TODO: Additional constraints:
# 	A) The crucible can move at most three blocks in a single direction.
# 	B) The crucible also can't reverse direction.
#		B is probably already implicit in Dijkstra's
#		(You never go back to the cell you came from, it's inefficient)
 
# To try to enforce constraint, in this v2, I store 4 distances per cell,
# one for each incoming direction.
# Graph nodes in the queue are not just x,y cell coordinates, but also a third dimension for the
# the last move made to arrive to them.

# Close to working, but I get a non-optimal path with a cost of 105 for the test input,
# instead of the optimal one with a cost of 102.

import math


def drawGrid(grid):
	for line in grid:
		print( str(line).replace('inf', '-').replace('None', '-').replace('False', '-').replace('True', 'S') )
	print('')


def drawPath(moves, bgGrid):
	grid = bgGrid
	cell = (0,0)
	for move in moves:
		x = cell[0]
		y = cell[1]
		if move == 0: #up
			offset = (0,-1)
			symbol = '^'
		elif move == 1: #right
			offset = (1,0)
			symbol = '>'
		elif move == 2: #down
			offset = (0,1)
			symbol = 'v'
		elif move == 3: #left
			offset = (-1,0)
			symbol = '<'
		nx = x + offset[0]
		ny = y + offset[1]
		grid[ny][nx] = symbol
		cell = (nx,ny)
		#print('cell: (%d,%d)' % cell)
		
	# draw resulting grid
	for y in range(len(grid)):
		print(''.join( map(str, grid[y]) ))

def minCost(cells, distsGrid):
	minDist = math.inf
	result = None
	for index,cell in enumerate(cells):
		x = cell[0]
		y = cell[1]
		inmove = cell[2]
		dist = distsGrid[y][x][inmove]
		if dist < minDist:
			minDist = dist
			result = cell
			resultIndex = index
	return resultIndex
	
	
def adjCells(cell, xmax, ymax):
	x = cell[0]
	y = cell[1]
	adjacents = []
	if (y-1) >= 0:
		nextCell = (x, y-1, 0) # move 0=up
		adjacents.append(nextCell)
	if (x+1) <= xmax:
		nextCell = (x+1, y, 1) # move 1=right
		adjacents.append(nextCell)
	if (y+1) <= ymax:
		nextCell = (x, y+1, 2) # move 2=down
		adjacents.append(nextCell)
	if (x-1) >= 0:
		nextCell = (x-1, y, 3) # move 3=left
		adjacents.append(nextCell)	
	return (adjacents)
	

def main():
	input = open("aoc2023_day17_testinput.txt", "r")
	#input = open("aoc2023_day17_input.txt", "r")
	total = 0

	cCostsGrid = [list(map(int, list(l))) for l in input.read().split('\n')]
	xmax = len(cCostsGrid[0]) - 1
	ymax = len(cCostsGrid) - 1
	
	start = (0,0,0) # x, y and entering move
	
	# START INITIALIZE RECORDS
	tCostsGrid = []
	for y in range(ymax+1):
		tCostsGrid.append([])
		for x in range(xmax+1):
			tCostsGrid[y].append([])
			tCostsGrid[y][x] = [math.inf, math.inf, math.inf, math.inf]
	
	seenGrid = [[[None]]*(xmax+1) for i in range(ymax+1)] # stores direction ids 0-3 from where this cell has been seen
	
	#parentsGrid = [[None]*(xmax+1) for i in range(ymax+1)]
	
	prevMovesGrid = []
	for y in range(ymax+1):
		prevMovesGrid.append([])
		for x in range(xmax+1):
			prevMovesGrid[y].append([])
			prevMovesGrid[y][x] = [[None], [None], [None], [None]]
	
	queue = [start]
	# END INITIALIZE RECORDS
	
	# Cost to enter starting cell is 0 for all 4 incoming directions
	x = start[0]
	y = start[1]
	for i in range(4):
		tCostsGrid[y][x][i] = 0
	
	while len(queue) > 0:
	#for i in range(10): # TEST limited steps
		#print('====')
		#print('Queue: %s' % queue)
		index = minCost(queue, tCostsGrid)
		pos = queue.pop(index)
		x = pos[0]
		y = pos[1]
		inmove = pos[2]
		#print('pos: (%d,%d,%d)' % (x,y,inmove))

		adjacents =  adjCells(pos, xmax, ymax)
		
		for i in range(len(adjacents)):
			move = adjacents[i][2]
			prevMoves = prevMovesGrid[y][x][inmove]
			baseCost = tCostsGrid[y][x][inmove]
			
			reverse = [2,3,0,1]
			lastMove = prevMoves[-1]
			# Enforce first constraint. If this would be fourth repeat of same move, skip
			if prevMoves[-3:] == [move]*3:
				pass
				
			# Enforce second constraint. If this is a reversal of previous move, skip
			elif lastMove is not None and move == reverse[lastMove]:
				pass
				
			else:		
				cell = adjacents[i]
				ax = cell[0]
				ay = cell[1]
				if move not in seenGrid[y][x]:
					if seenGrid[y][x] == [None]:
						seenGrid[y][x] = [move]
					else:
						seenGrid[y][x] = seenGrid[y][x] + [move]
					
					cellCost = cCostsGrid[ay][ax]
					recordCost = tCostsGrid[ay][ax][move]
					cost = baseCost + cellCost
					
					if cost < recordCost:
						tCostsGrid[ay][ax][move] = cost
						prevMovesGrid[ay][ax][move] = prevMoves + [move]
						queue.append(cell)
		
		#drawGrid(tCostsGrid)
			
	#drawGrid(tCostsGrid)
	#drawGrid(seenGrid)
	#drawGrid(parentsGrid)
	#drawGrid(prevMovesGrid)
	#print(queue)
	
	# Extract shortest path:
	x = xmax
	y = ymax
	min_cost = math.inf
	last_move = None
	for m in range(4):
		total_cost = tCostsGrid[y][x][m]
		if total_cost < min_cost:
			min_cost = total_cost
			last_move = m
	prevMoves = prevMovesGrid[y][x][last_move][1:] #skip first 'None' move
	
	print('Lowest cost: %d' % min_cost)
	#print('Best last move: %d' % last_move)
	print('Best moves: %s' % prevMoves)
	print('Path on grid:') 
	drawPath(prevMoves, cCostsGrid)
	
	#print('Best moves: %s' % prevMovesGrid[ymax][xmax])
	
main()
# Result: 870 is too high