import re

def drawPattern(pattern):
	for line in pattern:
		print(line)

def seekMirrors(pattern):
	sumRowsBefore = 0
	span = len(pattern)
	for i in range(span-1):

		before = i+1
		after = span - before
		
		mirrored = True
		for c in range( min(before, after) ):
			rowa = pattern[i-c]
			rowb = pattern[i+c+1]
			
			#print('---')
			#print(rowa)
			#print(rowb)
			
			if rowa != rowb:
				mirrored = False
				break
		
		if mirrored:
			#print('mirror found')
			sumRowsBefore += i+1
	return sumRowsBefore

def main():
	#input = open("aoc2023_day13_testinput.txt", "r")
	input = open("aoc2023_day13_input.txt", "r")
	total = 0

	# ingest input data
	patterns = [p.split('\n') for p in input.read().split('\n\n')]

	#for p in patterns:
	#	drawPattern(p)
	#	print(' ')

	# find mirrored rows:
	sumRowsBefore = 0
	sumColsBefore = 0
	#for pattern in patterns[0:1]: # TEST SINGLE
	for pattern in patterns:
			
		sumRowsBefore += seekMirrors(pattern)
		#print('Sum of rows Before: %d' % sumRowsBefore)
		
		#transpose cols and rows
		transpattern = list(map(''.join, map(list, zip(*pattern))))
		
		sumColsBefore += seekMirrors(transpattern)
		#print('Sum of cols Before: %d' % sumColsBefore)

	# To summarize your pattern notes,
	#add up the number of columns to the left of each vertical line of reflection;
	#to that, also add 100 multiplied by the number of rows above each horizontal line of reflection
	
	total = sumRowsBefore * 100 + sumColsBefore
	print('Total: %d' % total)

main()
# Result: 39939