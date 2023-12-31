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
		if (y-1) >= 0:
			newx = x
			newy = y-1
			symbol = themap[newy][newx]
			if symbol != '#':
				reached.append((newx,newy))
		
		# move right
		if (x+1) <= xmax:
			newx = x+1
			newy = y
			symbol = themap[newy][newx]
			if symbol != '#':
				reached.append((newx,newy))
		
		# move down
		if (y+1) <= ymax:
			newx = x
			newy = y+1
			symbol = themap[newy][newx]
			if symbol != '#':
				reached.append((newx,newy))
		
		# move left
		if (x-1) >= 0:
			newx = x-1
			newy = y
			symbol = themap[newy][newx]
			if symbol != '#':
				reached.append((newx,newy))
	
	reached = set(reached)
	return reached


def main():
	#input = open("aoc2023_day21_testinput.txt", "r")
	input = open("aoc2023_day21_input.txt", "r")
	total = 0

	mymap = [list(line) for line in input.read().split('\n')]
	drawGrid(mymap)
	for y in range(len(mymap)):
		for x in range(len(mymap[0])):
			symbol = mymap[y][x]
			if symbol == 'S':
				start = (x,y)
	positions = [start]
	
	steps = 64
	
	while steps > 0:
		positions = step(mymap, positions)
		steps -= 1
		maplive = copy.deepcopy(mymap)
		for pos in positions:
			x = pos[0]
			y = pos[1]
			maplive[y][x] = 'O'
			
		#drawGrid(maplive)
	
	total = len(positions)
	print(total)
	

main()
# Result: 3841