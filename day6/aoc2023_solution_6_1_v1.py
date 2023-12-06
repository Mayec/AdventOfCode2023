import re

def main():
	#input = open("aoc2023_day6_testinput.txt", "r")
	input = open("aoc2023_day6_input.txt", "r")
	total = 1

	# x: distance to beat
	# t: total race time
	# a: acceleration time
	# r: running time (r = t-a)
	# d: distance (d = a * r) (d = -a^2 + ta)
	#
	# condition to win: d > x
	# condition to win: -a^2 + ta > x
	
	# Ingest input data
	
	times, thresholds = input.read().split('\n')
	times = list(map(int, times.split()[1:]))
	thresholds = list(map(int, thresholds.split()[1:]))

	for race in range( len(times) ):
		ways = 0 # ways to win race
		for a in range( times[race] ):
			t = times[race]
			x = thresholds[race]
			d = - (a * a) + (t * a)
			if d > x: ways+= 1
		print(ways)
		total *= ways
	print(total)
	
main()
# Result: 500346