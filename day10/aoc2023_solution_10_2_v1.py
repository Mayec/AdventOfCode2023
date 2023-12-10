import math, time, os

#input = open("aoc2023_day10_testinput1.txt", "r")
#input = open("aoc2023_day10_testinput3.txt", "r")
#input = open("aoc2023_day10_testinput4.txt", "r")
#input = open("aoc2023_day10_testinput5.txt", "r")
input = open("aoc2023_day10_input.txt", "r")

tileTypes = ['|','-','L','J','7','F','.','S']

vertedges = ['|','L','J'] # consider slightly above center, to avoid colinearity, so L J collide, but 7 F don't

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
displace.append((0,-1))
displace.append((1,0))
displace.append((0,1))
displace.append((-1,0))

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
			if s == 'S': start = (j,i) # found and stored start position map coordinates
			j += 1
		i += 1
	
	# Display map
	#for line in map:
	#	print(''.join(line))
	
	pos = start
	camefrom = -1
	dist = 0
	
	# path = loop only map
	path = []
	for i in range(len(map)):
		path.append([])
		for j in range(len(map[i])):
			path[i].append('.')
	
	# Display path
	#for line in path:
	#	print(''.join(line))
	
	closed = False
	while not closed:
		tile = map[pos[1]][pos[0]]
		path[pos[1]][pos[0]] = tile
		#print('=====')
		#print('%s (%d,%d)' % (tile, pos[1], pos[0]))
		
		for d in range(4):
			#print('---')
			#print('d: %d' % d)
			#print('camefrom: %i' % camefrom)
			
			# check that this direction is an exit for this tile
			if len(directions[tile][d]) > 0:
				if d != camefrom:
					#print('d: %d' % d)
					#print('displacex: %d' % displace[d][0])
					#print('displacey: %d' % displace[d][1])
				
					newx = pos[0] + displace[d][0]
					newy = pos[1] + displace[d][1]
					#print('newx: %d' % newx)
					#print('newy: %d' % newy)
					#print('maxx: %d' % len(map[0]))
					#print('maxy: %d' % len(map))
					
					# Check that we're not exiting the map
					if (newx >= 0) and (newx < len(map[0])) and (newy >= 0) and (newy < len(map)):
						nexttile = map[newy][newx]
						camefrom = (d + 2) % 4
						tilesConnect = directions[nexttile][camefrom]
						#print('Next tile: %s' % nexttile)
						#print('tilesConnect: %s' % tilesConnect)
						
						if tile in tilesConnect:
							if nexttile=='S':
								closed=True #reached the end of the loop
							else:
								dist += 1
							pos = (newx, newy)
							break
		
		#exit() # TEST only one cycle
		#if dist > 10: break # TEST limited steps
		
		# display animated path
		#time.sleep(1)
		#os.system('cls')
		#for line in path:
		#	print(''.join(line))
		

	# display final path
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
	
	# Part 2: calculate enclosed tiles.
	# For this I will use the CG raytracing trick: if ray from a point intersects a boundary
	# an even number of times, it is outside. If it number of intersections are off, it is inside.
	enclosed = 0
	for j in range( 1, len(path)-1 ):
		path.append([])
		for i in range( 1, len(map[j])-1):
			pos = (i,j)
			tile = path[j][i]
			# if tile is empty, can be inside
			if  tile == '.':
				edges = 0
				#print('ray')
				for rayx in range( i+1, len(map[j]) ):
					rayz = j
					#print('rayx: %d' % rayx)
					#print('rayz: %d' % rayz)
					raycell = path[rayz][rayx]
					#print(raycell)
					if raycell in vertedges:
						edges += 1
				#print('Edges: %d' % edges)
				if (edges % 2) != 0:
					enclosed += 1
	
	print('Enclosed tiles: %d' % enclosed)
	
	
main()
# Result: 7097