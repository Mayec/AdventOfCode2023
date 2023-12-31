# Solution works well with test input data, but with full puzzle,
# would take way too long. Slowest part is dijkstra function

import math
import itertools

def sortq(queue, dists):
	sortedDists = sorted(dists.items(), key=lambda x:x[1])
	sortedVerts = [n[0] for n in sortedDists]
	newq = []
	for v in sortedVerts:
		if v in queue: newq.append(v)
	return newq


def dijkstra(verts, edges, source):
	dists = {}
	prev = {}
	queue = []
	# initialize
	for v in verts:
		dists[v] = math.inf
		prev[v] = None
		queue.append(v)
	dists[source] = 0
	
	while len(queue) > 0:
		queue = sortq(queue, dists)
		v = queue.pop(0)
		for nbor in edges[v]:
			if nbor in queue:
				altdist = dists[v] + 1
				if altdist < dists[nbor]:
					dists[nbor] = altdist
					prev[nbor] = v
	
	#print(dists)
	#print(prev)
	return dists, prev


def calcBtwns(verts, edges):
	betweenness = {}
	
	#totalpaths = len(pairwise(verts))
	totalpaths = 0.5*len(verts)*(len(verts)-1)
	print('Paths to calculate: %d' % totalpaths)
	paths = 0
	
	for i,v1 in enumerate(verts):
		print('calculating dijkstra')
		dists, prevs = dijkstra(verts, edges, v1)
		for v2 in verts[i+1:]:	
			path = []
			if (prevs[v2] is not None) or (v2 == v1):
				node = v2
				while node is not None:
					next = prevs[node]
					pathedge = (next,node)
					path.insert(0, pathedge)
					node = next
			path = path[1:] # remove redundant first
			#print('path %s -> %s'  % (v1,v2))
			#print(path)
			
			for edge in path:
				if edge not in betweenness:
					betweenness[edge] = 0
				betweenness[edge] += 1
				
			paths += 1
			print('%d of %d' % (paths, totalpaths))
			
	return betweenness

def graphGroup(start, edges, group):
	group.append(start)
	for nbor in edges[start]:
		if nbor not in group:
			group = graphGroup(nbor, edges, group)
	return group


def main():
	#input = open("aoc2023_day25_testinput.txt", "r")
	input = open("aoc2023_day25_input.txt", "r")
	total = 0

	# Ingest input data
	records = [line.split(': ') for line in input.read().split('\n')]
	for i,r in enumerate(records):
		records[i][1] = r[1].split(' ')
	#print(*records, sep='\n')
	#print('=========')
	
	# Build list of graph vertices, and list of graph edges:
	verts = []
	edges = {}
	for r in records:
		va = r[0]
		verts.append(va)
		verts += r[1]
		for vb in r[1]:
			if va in edges:
				edges[va].add(vb)
			else:
				edges[va] = set([vb])
			if vb in edges:
				edges[vb].add(va)
			else:
				edges[vb] = set([va])
	verts = list(set(verts))
	verts.sort()
	
	#for key,value in edges.items():
	#	print('%s: %s' % (key,value))
	#print('=========')
		
	# Will use something based on Girvan-Newman algorithm,
	# to find edges connecting two potentially separate groups.
	
	remedges = 3
	while remedges > 0:
		# 1. The betweenness of all existing edges in the network is calculated first.
		allbtwns = calcBtwns(verts, edges)
		
		# 2. The edge with the highest betweenness is removed.
		allbtwns = sorted(allbtwns.items(), key=lambda x:x[1], reverse=True)
		print(allbtwns)
		maxbtwns = allbtwns[0][0]
		#print(maxbtwns)
		v1 = maxbtwns[0]
		v2 = maxbtwns[1]
		edges[v1].remove(v2)
		edges[v2].remove(v1)
		remedges -= 1
		print('Removed edge %s-%s' % (v1,v2))
	
	# Calculate size of remaining isolated groups:
	queue = [v for v in verts]
	groups = []
	while len(queue) > 0:
		vgroup = graphGroup(queue[0], edges, [])
		print(vgroup)
		groups.append(vgroup)
		for v in vgroup:
			queue.remove(v)
		print(queue)
	print(groups)
	sizes = [len(g) for g in groups]
	print(sizes)
	
	total =sizes[0]*sizes[1]
	print('Total: %d' % total)

main()
# Result: 