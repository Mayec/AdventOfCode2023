import re

def main():
	#input = open("aoc2023_day6_testinput.txt", "r")
	input = open("aoc2023_day6_input.txt", "r")
	
	# x: distance to beat
	# t: total race time
	# a: acceleration time
	# r: running time (r = t-a)
	# d: distance (d = a * r) (d = -a^2 + ta)
	#
	# condition to win: d > x
	# condition to win: -a^2 + ta > x
	
	# Ingest input data
	

	time, threshold = input.read().split('\n')
	time = int( ''.join( time.split()[1:] ) )
	threshold = int( ''.join( threshold.split()[1:] ) )
	
	ways = 0 # ways to win race
	for a in range( time ):
		t = time
		x = threshold
		d = - (a * a) + (t * a)
		if d > x: ways+= 1
		
		#total time: 51,926,890
		if (a % 1000000) == 0:
			print("---")
			print("Checked " + str(a/1000000) + " million seeds")
		
	print(ways)

main()
# Result: 42515755

