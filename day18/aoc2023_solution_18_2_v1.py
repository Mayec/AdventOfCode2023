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
	#input = open("aoc2023_day18_testinput.txt", "r")
	#input = open("aoc2023_day18_testinput2.txt", "r")
	input = open("aoc2023_day18_input.txt", "r")
	total = 0

	# Ingest data
	instructions = input.read().split('\n')
	directions = []
	distances = []
	for line in instructions:
		fluffa, fluffb, col = line.split(' ')
		col = col.replace('#','').replace('(','').replace(')','')
		dir = col[-1]
		dist = int(col[:-1],16)
		directions.append(dir)
		distances.append(dist)
	#print(*distances, sep='\n')

	dirs = {'0': (1,0), '1': (0,1), '2': (-1,0), '3': (0,-1)}

	funcInput = [(dirs[directions[i]], distances[i]) for i in range(len(distances))]
	total = accArea(funcInput)
	
	print(total)

main()
# Result: 60612092439765