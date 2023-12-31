# Using Dijkstra's algorithm, with additional constraints
# TODO: Additional constraints:
# 	A) The crucible can move at most three blocks in a single direction.
# 	B) The crucible also can't reverse direction.
#		B is probably already implicit in Dijkstra's
#		(You never go back to the cell you came from, it's inefficient)
 
# To try to enforce constraint, in this v2, I will store 4 per cell, one for each incoming direction.
# WIP. It's a mess right now, can't make it work.
# What I think I need to fix it: graph nodes in the queue should not just be cell coordinates, but also the last move made to arrive to them.
# Then base cost will not be inf. anymore, since it will be a known quantity

import math


def drawGrid(grid):
	for line in grid:
		print( str(line).replace('inf', '-').replace('None', '-').replace('False', '-').replace('True', 'S') )
	print('')


def minCost(cells, distsGrid):
	minDist = math.inf
	result = None
	for cell in cells:
		x = cell[0]
		y = cell[1]
		dist = distsGrid[y][x]
		if dist < minDist:
			minDist = dist
			result = cell
	return result
	
	
def adjCells(cell, xmax, ymax):
	x = cell[0]
	y = cell[1]
	adjacents = []
	moves = []
	if (y-1) >= 0:
		nextCell = (x, y-1)
		adjacents.append(nextCell)
		moves.append(0) # move 0=up
	if (x+1) <= xmax:
		nextCell = (x+1, y)
		adjacents.append(nextCell)
		moves.append(1) # move 1=right
	if (y+1) <= ymax:
		nextCell = (x, y+1)
		adjacents.append(nextCell)
		moves.append(2) # move 2=down
	if (x-1) >= 0:
		nextCell = (x-1, y)
		adjacents.append(nextCell)
		moves.append(3) # move 3=left	
	return (adjacents, moves)
	

def main():
	input = open("aoc2023_day17_testinput.txt", "r")
	#input = open("aoc2023_day17_input.txt", "r")
	total = 0

	cCostsGrid = [list(map(int, list(l))) for l in input.read().split('\n')]
	xmax = len(cCostsGrid[0]) - 1
	ymax = len(cCostsGrid) - 1
	
	start = (0,0)
	#start = ((xmax), (ymax))
	
	# START INITIALIZE RECORDS
	tCostsGrid = [[]]
	for y in range(ymax+1):
		tCostsGrid.append([])
		for x in range(xmax+1):
			tCostsGrid[y].append([])
			tCostsGrid[y][x] = [math.inf, math.inf, math.inf, math.inf]
	
	seenGrid = [[[None]]*(xmax+1) for i in range(ymax+1)] # stores direction ids 0-3 from where this cell has been seen
	
	#parentsGrid = [[None]*(xmax+1) for i in range(ymax+1)]
	
	movesGrid = [[]]
	for y in range(ymax+1):
		movesGrid.append([])
		for x in range(xmax+1):
			movesGrid[y].append([])
			movesGrid[y][x] = [[None], [None], [None], [None]]
	
	queue = [start]
	# END INITIALIZE RECORDS
	
	# Cost to starting cell is 0
	x = start[0]
	y = start[1]
	for i in range(4):
		tCostsGrid[y][x][i] = 0
	
	#while len(queue) > 0:
	for i in range(10): # TEST limited steps
		print(queue)
		#pos = minCost(queue, tCostsGrid)
		pos = queue.pop()
		x = pos[0]
		y = pos[1]
		print('pos: (%d,%d)' % (x,y))
		#seenGrid[y][x] = True
		
		#for indir in range(4):

		adjacents, moves =  adjCells(pos, xmax, ymax)
		
		for id in range(len(adjacents)):
			move = moves[id]
			prevMoves = movesGrid[y][x][move]
			baseCost = tCostsGrid[y][x][move] # <-- should not be indexed to [move], but to the move made to the origin node (see note about next steps, at the top)
			
			# Enforce first constraint. If this would be fourth repeat of same move, skip
			if prevMoves[-3:] == [move]*3:
				pass
			else:		
				cell = adjacents[id]
				ax = cell[0]
				ay = cell[1]
				if move not in seenGrid[y][x]:
					seenGrid[y][x] = seenGrid[y][x] + [move]
					cellCost = cCostsGrid[ay][ax]
					recCost = tCostsGrid[ay][ax][move]
					cost = baseCost + cellCost
					print('---')
					print(baseCost)
					print(cellCost)
					print('cell: (%d,%d), cost: %s' % (ax,ay, cost))
					print(recCost)
					for m in range(4):
						if cost < recCost:
							tCostsGrid[ay][ax][move] = cost
							#parentsGrid[ay][ax] = pos
							movesGrid[ay][ax][move] = prevMoves + [move]
							queue.append(cell)
		
	drawGrid(tCostsGrid)
	drawGrid(seenGrid)
	#drawGrid(parentsGrid)
	#drawGrid(movesGrid)
	#print(queue)
	
	print('Best moves: %s' % movesGrid[ymax][xmax])
	
main()
# Result: 877 is too high