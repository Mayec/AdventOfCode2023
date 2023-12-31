# Unsolved, not getting correct total distances for all possible
# paths in testinput

from functools import cache


def npaths(themap, pos):
	paths = []
	xmax = len(themap[0])
	ymax = len(themap)

	#try up
	x = pos[0]
	y = pos[1]-1
	if y>= 0:
		symbol = themap[y][x]
		if symbol == '.' or symbol == '^': paths.append( (x,y) )
	#try left
	x = pos[0]-1
	y = pos[1]
	if x>= 0:
		symbol = themap[y][x]
		if symbol == '.' or symbol == '<': paths.append( (x,y) )
	#try right
	x = pos[0]+1
	y = pos[1]
	if x < xmax:
		symbol = themap[y][x]
		if symbol == '.' or symbol == '>': paths.append( (x,y) )
	#try down
	x = pos[0]
	y = pos[1]+1
	if y < ymax:
		symbol = themap[y][x]
		if symbol == '.' or symbol == 'v': paths.append( (x,y) )
	
	return paths	

@cache
def linkNextJunction(themap, juncstart, walkstart, pseen):
	ymax =len(themap)-1

	seen = list(pseen)
	pos = walkstart
	next = []
	dist = 0
	links = []
	
	junction = False
	while not junction:
		seen.append(pos)
		next = npaths(themap, pos)
		next = [cell for cell in next if cell not in seen]
		if len(next) > 1:
			junction = True
			#print('Found junction at (%d,%d)' % (pos[0],pos[1]))
		elif next[0][1] == ymax:
			#reached exit
			dist += 1
			junction = True
			pos = 'end'
			next = []
		elif len(next) < 1:
			print('Dead end at (%d,%d)' % (pos[0],pos[1]))
		else:
			dist += 1
			pos = next[0]
	
	jlink = (juncstart, pos, dist)
	links.append(jlink)
	
	for nextstart in next:
		nextlinks = linkNextJunction(themap, pos, nextstart, tuple(seen))
		links += nextlinks
	
	return links


def edges2graph(edges):
	graph = {}
	for edge in edges:
		key = edge[0]
		if key in graph:
			graph[key].append((edge[1], edge[2]))
		else:
			graph[key] = [(edge[1], edge[2])]
	return graph


def linkJunctions(themap, start):
	seen = ()
	links = linkNextJunction(themap, start, start, seen)
	return links

paths = []

def depthFirst(graph, currentVertex, visited, distances):
	visited.append(currentVertex)
	for edge in graph[currentVertex]:
		vertex = edge[0]
		dist = edge[1]
		if vertex not in visited:
			distances.append(dist)
			if vertex != 'end':
				depthFirst(graph, vertex, visited.copy(), distances.copy())
	paths.append(visited)
	#pathDistances.append(distances)


def paths2distances(graph, paths):
	distances = []
	for path in paths:
		print('---')
		dist = 0
		for index in range(len(path)-1):
			src = path[index]
			dst = path[index+1]
			edges = graph[src]
			for edge in edges:
				if edge[0] == dst: dist += edge[1]
				print(edge[1])
		last = path[-1]
		edges = graph[last]
		for edge in edges:
			if edge[0] == 'end': dist += edge[1]
			distances.append(dist)
	return distances

	
def main():
	input = open("aoc2023_day23_testinput.txt", "r")
	#input = open("aoc2023_day23_input.txt", "r")
	total = 0

	mymap = tuple([tuple(line) for line in input.read().split('\n')])
	startx = mymap[0].index('.')
	startpos = (startx,0)
	
	edges = set(linkJunctions(mymap, startpos))
	print(*edges, sep='\n')
	print('')
	
	# Build graph dictionary (junction: [(destination1, distance1), (destination, distance2), ...])
	graph = edges2graph(edges)
	print(graph)
	print('')
	
	depthFirst(graph, startpos, [], [])
	print(paths)
	print('')
	
	dists = paths2distances(graph, paths)
	print(dists)
	print('')
	
	#total = list(map(sum, pathDistances))
	#print(total)

main()
# Result: 