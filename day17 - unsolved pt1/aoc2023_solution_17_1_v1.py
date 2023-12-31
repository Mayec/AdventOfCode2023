# Using Dijkstra's algorithm, with additional constraints
# TODO: Additional constraints:
# 	A) The crucible can move at most three blocks in a single direction.
# 	B) The crucible also can't reverse direction.
#		B is probably already implicit in Dijkstra's
#		(You never go back to the cell you came from, it's inefficient)

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
	
	# initialize records
	tCostsGrid = [[math.inf]*(xmax+1) for i in range(ymax+1)]
	seenGrid = [[[None]]*(xmax+1) for i in range(ymax+1)] # stores direction ids 0-3 from where this cell has been seen
	parentsGrid = [[None]*(xmax+1) for i in range(ymax+1)]
	movesGrid = [[[None]]*(xmax+1) for i in range(ymax+1)] # stores the moves to get to this cell, for current stored total cost
	queue = [start]
	
	# Cost to starting cell is 0
	x = start[0]
	y = start[1]
	tCostsGrid[y][x] = 0
	
	#while len(queue) > 0:
	for i in range(10): # TEST limited steps
		#print(queue)
		pos = minCost(queue, tCostsGrid)
		posindex = queue.index(pos)
		queue.pop(posindex)
		x = pos[0]
		y = pos[1]
		print('pos: (%d,%d), cost: %d' % (x,y, tCostsGrid[y][x]))
		#seenGrid[y][x] = True
		baseCost = tCostsGrid[y][x]
		#prevMoves = [ n for n in movesGrid[y][x] if n is not None] # from movesGrid data, but cleanup initial None
		prevMoves = movesGrid[y][x]
		adjacents, moves =  adjCells(pos, xmax, ymax)
		
		for id in range(len(adjacents)):
			move = moves[id]
			
			# Enforce first constraint. If this would be fourth repeat of same move, skip
			if prevMoves[-3:] == [move]*3:
				pass
			else:		
				cell = adjacents[id]
				ax = cell[0]
				ay = cell[1]
				print(move)
				print(seenGrid[ay][ax])
				if move not in seenGrid[ay][ax]:
					seenGrid[ay][ax] = seenGrid[ay][ax] + [move]
					cellCost = cCostsGrid[ay][ax]
					recCost = tCostsGrid[ay][ax]
					cost = baseCost + cellCost
					if cost < recCost:
						tCostsGrid[ay][ax] = cost
						parentsGrid[ay][ax] = pos
						movesGrid[ay][ax] = prevMoves + [move]
						queue.append(cell)
		
	drawGrid(tCostsGrid)
	drawGrid(seenGrid)
	#drawGrid(parentsGrid)
	#drawGrid(movesGrid)
	#print(queue)
	
	print('Best moves: %s' % movesGrid[ymax][xmax])

main()
# Result: 877 is too high