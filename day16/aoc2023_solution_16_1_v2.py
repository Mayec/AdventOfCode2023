# In this v2, avoid recursion

from functools import cache

def raystep(board, hot, start, dir):
	#dir; 0 up, 1 right, 2 down, 3 left
	if dir == 0: cell = (start[0], start[1]-1)
	elif dir == 1: cell = (start[0]+1, start[1])
	elif dir == 2: cell = (start[0], start[1]+1)
	else: cell = (start[0]-1, start[1])
	
	#print('from: (%d,%d)' % (start[0], start[1]))
	#print('dir: %d' % dir)
	#print('cell: (%d,%d)' % (cell[0], cell[1]))
	
	x = cell[0]
	y = cell[1]
	
	nextRays = []
	
	if x in range(len(board[0])) and y in range(len(board)):
		symbol = board[y][x]
		#print('symbol: %s' % symbol)
		
		if cell not in hot: hot.append(cell)
		
		newdir = dir
		#if symbol == '.' do nothing
			
		if symbol == '\\':
			if dir == 0: newdir = 3
			elif dir == 1: newdir = 2
			elif dir == 2: newdir = 1
			else: newdir = 0
			
		elif symbol == '/':
			if dir == 0: newdir = 1
			elif dir == 1: newdir = 0
			elif dir == 2: newdir = 3
			else: newdir = 2
		
		elif symbol == '|':
			# if perpendicular, split. Otherwise just keep going
			if dir == 1 or dir == 3:
				newdir = 0
				nextRays.append( (cell, newdir) )
				newdir = 2
		
		elif symbol == '-':
			# if perpendicular, split. Otherwise just keep going
			if dir == 0 or dir == 2:
				newdir = 1
				nextRays.append( (cell, newdir) )
				newdir = 3
		
		nextRays.append( (cell, newdir) )
		return nextRays
	else:
		#print('out')
		return None


def drawAreas(board, areas):
	for y in range(len(board)):
		line = ''
		for x in range(len(board[0])):
			if (x,y) in areas:
				line += '#'
			else:
				line += '.'
		print(line)


def main():
	#input = open("aoc2023_day16_testinput.txt", "r")
	input = open("aoc2023_day16_input.txt", "r")
	total = 0

	board = [list(line) for line in input.read().split('\n')]
	
	start = (0,0)
	hot = [start]
	
	solved  = []
	
	startsymbol = board[0][0]
	if startsymbol == '\\': startdir = 2
	elif startsymbol == '//': startdir = 0
	else:  startdir = 1
	
	nextRays = [(start, startdir)]
	
	while len(nextRays) > 0:
	
		#print('----')
		#print('nextRays: %s' % nextRays)
		
		next = nextRays.pop(-1)
		if next not in solved:
			solved.append(next)
			
			#print('next:')
			#print(next)
			
			cell = next[0]
			dir = next[1]
			rayheads = raystep(board, hot, cell, dir)
			if rayheads is not None:
				nextRays += rayheads
	
	#print(nextRays)
	#print(hot)
	
	drawAreas(board, hot)

	total = len(hot)
	print('Total energized tiles: %d' % total)

main()
# Result: 7034