import re

def extrapolate(seq):
	difs = []
	for i in range(1, len(seq)):
		difs.append( seq[i] - seq[i-1])
	
	if sum( [abs(n) for n in difs] ) == 0:
		# Reached last level of differences
		dif = 0
	else:
		dif = extrapolate(difs)
	result = seq[0] - dif
	
	#print(difs)
	#print('Extrapolated: ' + str(result))
	
	return result

def main():
	#input = open("aoc2023_day9_testinput.txt", "r")
	input = open("aoc2023_day9_input.txt", "r")
	total = 0

	sequences = [s.split() for s in input.read().split('\n')]
	#print(list(sequences))
	
	#testn = 80 # TESTS
	#for seq in sequences[testn-1:testn]: # TESTS
	for seq in sequences:
		#print('---\n' + str(seq))
	
		seq = [int(n) for n in seq]
		result = extrapolate(seq)
		#print('Result: ' + str(result))
		#print(result)
		
		total += result
	
	print('Total: ' +str(total))
main()

# Result: 1050
