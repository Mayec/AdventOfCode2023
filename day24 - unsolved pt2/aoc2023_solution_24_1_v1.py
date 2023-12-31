import math

def sumVecs(v1, v2):
	x = v1[0] + v2[0]
	y = v1[1] + v2[1]
	z = v1[2] + v2[2]
	return (x,y,z)

def subVecs(v1, v2):
	x = v1[0] - v2[0]
	y = v1[1] - v2[1]
	z = v1[2] - v2[2]
	return (x,y,z)

def record2pts(record):
	pos = record[0]
	vel = record[1]
	pt1 = pos
	pt2 = sumVecs(pos, vel)
	return (pt1, pt2)


def linesIntersection2d(pts1, pts2):
	ptA = pts1[0]
	ptB = pts1[1]
	vel1 = subVecs(ptB,ptA)
	ptC = pts2[0]
	ptD = pts2[1]
	vel2 = subVecs(ptD,ptC)
	
	# Line AB represented as a1x + b1y = c1
	a1 = ptB[1] - ptA[1]
	b1 = ptA[0] - ptB[0]
	c1 = a1*ptA[0] + b1*ptA[1]
	
	# Line CD represented as a2x + b2y = c2
	a2 = ptD[1] - ptC[1]
	b2 = ptC[0] - ptD[0]
	c2 = a2*ptC[0] + b2*ptC[1]
	
	determinant = a1*b2 - a2*b1
	
	if determinant==0:
		# The lines are parallel. This is simplified
		# by returning a pair of infinites
		x = math.inf
		y = math.inf
	else:
		x = (b2*c1 - b1*c2)/determinant
		y = (a1*c2 - a2*c1)/determinant
		
	# Check that intersection did not happen in the past
	if ((x - ptA[0]) / vel1[0] < 0) or ((x - ptC[0]) / vel2[0] < 0):
		return (None, None)
	else:
		return (x,y)


def filterAoi(intersections, xmin, xmax, ymin, ymax):
	filtered = []
	for pt in intersections:
		x = pt[0]
		y = pt[1]
		if not (x<xmin or x>xmax or y<ymin or y>ymax):
			filtered.append(pt)
	return filtered


def filterPast(intersections):
	filtered = []
	for pt in intersections:
		x = pt[0]
		if x is not None:
			filtered.append(pt)
	return filtered


def main():
	#input = open("aoc2023_day24_testinput.txt", "r")
	input = open("aoc2023_day24_input.txt", "r")
	total = 0

	# Ingest input data
	records = [r.split(' @ ') for r in input.read().split('\n')]
	for index, r in enumerate(records):
		pos = list(map( int, r[0].split(',') ))
		vel = list(map( int, r[1].split(',') ))
		pos = tuple(pos)
		vel = tuple(vel)
		records[index] = tuple([pos, vel])
	records = tuple(records)
	
	#records = records[:2] # TEST reduced
	#print(records)
	
	intersects = []
	for i,r1 in enumerate(records):
		linepts1 = record2pts(r1)
		for r2 in records[i+1:]:
			linepts2 = record2pts(r2)
			intersectpt = linesIntersection2d(linepts1, linepts2)
			intersects.append(intersectpt)
	#print(*intersects, sep='\n')
	#print('')
	
	# Filter intersections in the past
	intersects = filterPast(intersects)
	
	# Filter intersections out of area of interest
	#min = 7
	#max= 27
	min = 200000000000000
	max = 400000000000000
	intersects = filterAoi(intersects, min, max, min, max)
	#print(*intersects, sep='\n')
	
	total = len(intersects)
	print('Total: %d' % total)

main()
# Result: 16589