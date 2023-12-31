# Unsolved. Handling these 3d grids is proving really unwieldy


def drawSlice(vol, axis):
	sx = len(vol)
	sy = len(vol[0])
	sz = len(vol[0][0])
	
	#print(sx)
	#print(sy)
	#print(sz)
	
	if axis == 0:
		for z in range(sz):
			dz = sz-1-z # reverse so draws top-to-bottom
			line = ''
			for y in range(sy):
				for x in range(sx):
					#print('(%d,%d,%d)' % (x,y,dz))
					voxel = vol[x][y][dz]
				if voxel is not False:
					line += '#'
				elif dz==0:
					line +='-'
				else:
					line += '.'
			print(line)
	
	print('')


def countFull(vol):
	sx = len(vol)
	sy = len(vol[0])
	sz = len(vol[0][0])
	count = 0
	for x in range(sx):
		for y in range(sy):
			for z in range(sz):
				if vol[x][y][z]: count += 1
	return count


def bricks2vol(bricks, sx, sy, sz):

	volume = [[[False for z in range(sz)] for y in range(sy)] for x in range(sx)]
	for index, brick in enumerate(bricks):
		xmin = brick[0][0]
		ymin = brick[0][1]
		zmin = brick[0][2]
		xmax = brick[1][0]
		ymax = brick[1][1]
		zmax = brick[1][2]
		for x in range(xmin,xmax+1):
			for y in range(ymin,ymax+1):
				for z in range(zmin,zmax+1):
					#print('fill: %d, %d, %d' % (x,y,z))
					volume[x][y][z] = index
	
	return volume


def fallBricks(bricks, vol):
	for index, brick in enumerate(bricks):
		#print(brick)
		sx = len(vol)
		sy = len(vol[0])
		sz = len(vol[0][0])
	
		xmin = brick[0][0]
		ymin = brick[0][1]
		zmin = brick[0][2]
		xmax = brick[1][0]
		ymax = brick[1][1]
		zmax = brick[1][2]
		
		if zmin > 1:
			#ray down
			hitMax = -1
			for x in range(xmin,xmax+1):
				for y in range(ymin,ymax+1):
					z = zmin-1
					hit = False
					while not hit:
						if vol[x][y][z] or z == 1:
							hit = True
							hitMax = max(hitMax, z)
						z -= 1
			#print(hitMax)
		
			# if empty space below, relocate brick downards
			if hitMax < zmin-1:
				dz = zmin-1 - hitMax
				bricks[index] = ([xmin,ymin,zmin-dz], [xmax,ymax,zmax-dz])
			
			vol = bricks2vol(bricks, sx, sy, sz)


def checkSupports(bricks, vol):
	supports = []
	for index, brick in enumerate(bricks):
		supports.append([])
		print(brick)
		sx = len(vol)
		sy = len(vol[0])
		sz = len(vol[0][0])
	
		xmin = brick[0][0]
		ymin = brick[0][1]
		zmin = brick[0][2]
		xmax = brick[1][0]
		ymax = brick[1][1]
		zmax = brick[1][2]
		
		if zmin > 0:
			#scan below for supports
			for x in range(xmin,xmax+1):
				for y in range(ymin,ymax+1):
					z = zmin-1
					if vol[x][y][z]:
						print('support found')
						supports[index].append( vol[x][y][z] )
	print(supports)

def main():
	input = open("aoc2023_day22_testinput.txt", "r")
	#input = open("aoc2023_day22_input.txt", "r")
	total = 0
	
	# ingest bricks data
	xmax = 0
	ymax = 0
	zmax = 0
	bricks = input.read().split('\n')
	
	bricks = bricks[0:2] # TEST
	
	for i, brick in enumerate(bricks):
		bricks[i] = brick.split('~')
		a = list(map(int, bricks[i][0].split(',')))
		b = list(map(int, bricks[i][1].split(',')))
		xmax = max(xmax, a[0], b[0])
		ymax = max(ymax, a[1], b[1])
		zmax = max(zmax, a[2], b[2])
		bricks[i] = (a, b)
	
	print(bricks)
	#print('max: %d, %d, %d' % (xmax,ymax,zmax))
	
	# initialize volume grid
	#sx = len(volume)
	#sy = len(volume[0])
	#sz = len(volume[0][0])
	#print('size: %d, %d, %d' % (sx,sy,sz))

	# record voxels filled by bricks
	
	volume = bricks2vol(bricks, xmax+1, ymax+1, zmax+1)
	print(volume)
	
	#print( countFull(volume) )
	
	drawSlice(volume, 0)

	fallBricks(bricks, volume)
	# update volume record
	volume = bricks2vol(bricks, xmax+1, ymax+1, zmax+1)

	drawSlice(volume, 0)
	
	supports = checkSupports(bricks, volume)

main()
# Result: 