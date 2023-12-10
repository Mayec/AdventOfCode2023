import math, time, os

#input = open("aoc2023_day10_testinput1.txt", "r")
#input = open("aoc2023_day10_testinput2.txt", "r")
input = open("aoc2023_day10_input.txt", "r")

tileTypes = ['|','-','L','J','7','F','.','S']

directions = {}
directions['|'] = [1,0,1,0]
directions['-'] = [0,1,0,1]
directions['L'] = [1,1,0,0]
directions['J'] = [1,0,0,1]
directions['7'] = [0,0,1,1]
directions['F'] = [0,1,1,0]
directions['.'] = [0,0,0,0]
directions['S'] = [1,1,1,1]

# connectors index corresponds to direction as follows:
#   0 
# 1   2
#   3 
connectors = []
connectors.append(['|', '7', 'F', 'S']) # direction north (N), index 0
connectors.append(['-', 'J', '7', 'S']) # direction east (E), index 1
connectors.append(['|', 'L', 'J', 'S']) # direction south (S), index 2
connectors.append(['-', 'L', 'F', 'S']) # direction west (W), index 3

for d in directions.values():
	for i in range(len(d)):
		if d[i] == 1:
			d[i] = connectors[i]
		else:
			d[i] = []

#End of defining directions connections

displace = []
displace.append((-1,0))
displace.append((0,1))
displace.append((1,0))
displace.append((0,-1))

def main():
	
	total = 0
	
	lines = input.read().split('\n')
	
	map = [] 	# map is a list of lists. Each inner list is a row.
				# 1st index for rows, 2nd index for columns
	
	# Populate map from input
	i = 0
	for row in lines:
		map.append([])
		j = 0
		for s in row:
			map[i].append(s)
			# find starting tile
			if s == 'S': start = (i,j) # found and stored start position map coordinates
			j += 1
		i += 1
	
	pos = start
	camefrom = -1
	dist = 0
	
	# path = loop only map
	path = []
	for i in range(len(map[0])):
		path.append([])
		for j in range(len(map)):
			path[i].append('.')
	
	closed = False
	while not closed:
		tile = map[pos[0]][pos[1]]
		path[pos[0]][pos[1]] = tile
		#print('%s (%d,%d)' % (tile, pos[0], pos[1]))
		
		for d in range(4):
			#print('---')
			#print('d: %d' % d)
			#print('camefrom: %i' % camefrom)
			
			# check that this direction is an exit for this file
			if len(directions[tile][d]) > 0:
				if d != camefrom:
					#print('d: %d' % d)
					#print('displacex: %d' % displace[d][0])
					#print('displacey: %d' % displace[d][1])
				
					newx = pos[0] + displace[d][0]
					newy = pos[1] + displace[d][1]
					#print('newx: %d' % newx)
					#print('newy: %d' % newy)
					
					# Check that we're not exiting the map
					if (newx >= 0) and (newx < len(map[0])) and (newy >= 0) and (newy < len(map)):
						nexttile = map[newx][newy]
						tilesConnect = directions[tile][d]
						#print('Next tile: %s' % nexttile)
						#print('tilesConnect: %s' % tilesConnect)
						
						if nexttile in tilesConnect:
						
							if nexttile=='S':
								print('foo')
								closed=True #reached the end of the loop
							else:
								dist += 1
							camefrom = (d + 2) % 4
							pos = (newx, newy)
							break
		
		#exit() # TEST only one cycle
		#if dist > 10: break # TEST limited steps
		
		# print animated path
		#time.sleep(1)
		#os.system('cls')
		#for line in path:
		#	print(''.join(line))
		

	# print final path
	#for line in path:
	#	print(''.join(line))

	# count symbols in path
	#count = 0
	#for line in path:
	#	for s in line:
	#		if s != '.':
	#			count += 1
	#print('Symbols count: %d' % count)
	
	print('Loop length: %d' % dist)
	
	maxDist = math.ceil(0.5 * dist)
	print('Longest distance: %d' % maxDist)

main()
# Result: 7097