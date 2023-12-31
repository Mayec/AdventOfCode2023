# Applies shoelace theorem to calculate area of polygon from its boundary coordinates
# Gives correct answer for test, but not for final puzzle input

def shoelaceArea(boundary_coords):
	ncoords = len(boundary_coords)
	nsegments = ncoords - 1
	
	l = [(boundary_coords[i+1][0] - boundary_coords[i][0]) * (boundary_coords[i+1][1] + boundary_coords[i][1]) for i in range(nsegments)]
	
	return abs(sum(l)) / 2


def main():
	input = open("aoc2023_day18_testinput.txt", "r")
	#input = open("aoc2023_day18_testinput2.txt", "r")
	#input = open("aoc2023_day18_input.txt", "r")
	total = 0

	# Ingest data
	instructions = input.read().split('\n')
	directions = []
	distances = []
	colors = []
	for line in instructions:
		dir, dist, col = line.split(' ')
		directions.append(dir)
		distances.append(int(dist))
		colors.append(col)

	# Build list of boundary coordinates
	boundary = []
	x = 0
	y = 0
	xmin = 0
	ymin = 0
	for i,dir in enumerate(directions):
		dist = distances[i]
		if dir == 'U': y -= dist
		elif dir == 'D': y += dist
		elif dir == 'L': x -= dist
		elif dir == 'R': x += dist
		boundary.append((x,y))
		xmin = min(x,xmin)
		ymin = min(y,ymin)
	# Normalize coordinates (minimum at 0,0)
	for i,coords in enumerate(boundary):
		x = coords[0] - xmin
		y = coords[1] - ymin
		boundary[i] = (x,y)
	print(*boundary, sep='\n')	
	
	# Apply shoelace to find inner area
	total = shoelaceArea(boundary)
	
	# Add missing half of the perimiter trench area
	total += sum(distances)/2 +1
	
	print(total)
	

main()
# Result: 51045 is too low.
# Should be 52035