# In this v2, avoid recursion

from functools import cache

def raymarch(dir,symbol):
	newdirs = [dir]
	#if symbol == '.' do nothing
		
	if symbol == '\\':
		if dir == 0: newdirs = [3]
		elif dir == 1: newdirs = [2]
		elif dir == 2: newdirs = [1]
		else: newdirs = [0]
		
	elif symbol == '/':
		if dir == 0: newdirs = [1]
		elif dir == 1: newdirs = [0]
		elif dir == 2: newdirs = [3]
		else: newdirs = [2]
	
	elif symbol == '|':
		# if perpendicular, split. Otherwise just keep going
		if dir == 1 or dir == 3:
			newdirs = [0,2]
	
	elif symbol == '-':
		# if perpendicular, split. Otherwise just keep going
		if dir == 0 or dir == 2:
			newdirs = [1,3]	
	return newdirs
	

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
		newdirs = raymarch(dir, symbol)
		for newdir in newdirs:
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
	print('')


def main():
	#input = open("aoc2023_day16_testinput.txt", "r")
	input = open("aoc2023_day16_input.txt", "r")
	total = 0

	board = [list(line) for line in input.read().split('\n')]
	
	# try all possible start edge cells 
	xmax = len(board[0])-1
	ymax = len(board)-1
	
	startcells = list(zip( ([0] * (xmax+1)), range(xmax+1) )) # left border
	startcells += list(zip( ([ymax] * (xmax+1)), range(xmax+1) )) # right border
	startcells += list(zip( range(ymax+1), ([0] * (ymax+1)) )) # top border
	startcells += list(zip( range(ymax+1), ([xmax] * (ymax+1)) )) # bottom border
	startcells = set(startcells)
	
	#print(len(startcells))
	#print(list(startcells))
	
	#startcells = [(0,0)]# single TEST
	
	count = 0
	for startcell in startcells:
		#startcell = (0,0)
		#edgedir = 1
		
		count += 1
		print ('Checking start cell %d of %d' % (count, len(startcells)))
		
		edgedirs = []
		if startcell[0] == 0: edgedirs.append(1)
		if startcell[1] == 0: edgedirs.append(2)
		if startcell[0] == xmax: edgedirs.append(3)
		if startcell[1] == ymax: edgedirs.append(0)
	
		startsymbol = board[startcell[1]][startcell[0]]

		for edgedir in edgedirs:
			#print('startcell: (%d,%d)' % (startcell[0], startcell[1]))
			#print('edgedir: %d' % edgedir)
			
			# reset records
			nextRays = []
			solved  = []
			hot = [startcell]
			
			startdirs = raymarch(edgedir, startsymbol)

			for startdir in startdirs:
				nextRays.append( (startcell, startdir) )
			
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
		
			#drawAreas(board, hot)
			#print('Configuration score: %d' % len(hot))
			total = max( len(hot), total )
			print('Current total: %d' % total)
		
	print('Total energized tiles: %d' % total)

main()
# Result: 7759