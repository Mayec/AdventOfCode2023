import copy

def drawGrid(grid):
	for line in grid:
		print(''.join(line))
	print('')


def step(themap, positions):
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
	
	reached = set(reached)
	return reached


def main():
	input = open("aoc2023_day21_testinput.txt", "r")
	#input = open("aoc2023_day21_input.txt", "r")
	total = 0

	mymap = [list(line) for line in input.read().split('\n')]
	drawGrid(mymap)
	for y in range(len(mymap)):
		for x in range(len(mymap[0])):
			symbol = mymap[y][x]
			if symbol == 'S':
				start = (x,y)
	positions = [start]
	
	steps = 100
	
	while steps > 0:
		positions = step(mymap, positions)
		steps -= 1
		#maplive = copy.deepcopy(mymap)
		for pos in positions:
			x = pos[0]
			y = pos[1]
			
			#maplive[y][x] = 'O'
		#drawGrid(maplive)
	
	total = len(positions)
	print(total)
	

main()
# Result: 3841