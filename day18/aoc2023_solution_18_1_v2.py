# tracks horizontal moves forward and backward (dx)
# Multiplies them by y * dx
def accArea(steps):
	dx = 0
	ans = 1 #start with one square meter hole
	for (x,y), n in steps:
		dx += x*n
		ans += y*n * dx
		ans += n/2 # this correction compensates missing half of the permiter itself
	return int(ans)
	

def main():
	input = open("aoc2023_day18_testinput.txt", "r")
	input = open("aoc2023_day18_testinput2.txt", "r")
	input = open("aoc2023_day18_input.txt", "r")
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

	dirs = {'R': (1,0), 'D': (0,1), 'L': (-1,0), 'U': (0,-1)}

	funcInput = [(dirs[directions[i]], distances[i]) for i in range(len(distances))]
	total = accArea(funcInput)
	
	print(total)

main()
# Result: 52035