import re

def drawPattern(pattern):
	for line in pattern:
		print(line)
	print("---")

def seekMirrors(pattern):
	mirrorsRows = []
	span = len(pattern)
	for i in range(span-1):

		before = i+1
		after = span - before
		
		mirrored = True
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
			mirrorsRows.append(i+1)	
	return mirrorsRows

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
	sumRowsBefore1 = 0
	sumColsBefore1 = 0
	sumRowsBefore2 = 0
	sumColsBefore2 = 0
	#for pattern in patterns[4:5]: # TEST SINGLE
	# TEST CASE: for pattern 4, smudge in (10,0) should cause a detectable mirror
	for pattern in patterns:
		
		#print('\n=================')
		#print('pattern:')
		#drawPattern(pattern)
		
		# find reflections in original pattern
		oMirrorsRows = seekMirrors(pattern)
		#transpose cols and rows
		transpattern = list(map(''.join, map(list, zip(*pattern))))
		oMirrorsCols = seekMirrors(transpattern)
		
		sumRowsBefore1 += sum(oMirrorsRows)
		sumColsBefore1 += sum(oMirrorsCols)
		
		#print('OG Rows Before: %s' % oMirrorsRows)
		#print('OG Cols Before: %s' % oMirrorsCols)
		
		# scan until you find smudge (a symbol whose change manifests a new mirror)
		found = False
		for y in range(len(pattern)):
			if not found:
				for x in range(len(pattern[0])):
					#print('\nsmudge (%d,%d):' % (x,y))
					#print('before:')
					#drawPattern(pattern)
				
					altpattern = pattern.copy()
					row = pattern[y]
					symbol = pattern[y][x]
					newsymbol = '.' if (symbol == '#') else '#'
					newrow = row[:x] + newsymbol + row[x+1:] 
					altpattern[y] = newrow
					
					#print('after:')
					#drawPattern(altpattern)
					
					mirrorsRows = seekMirrors(altpattern)
					#if reflection already in original pattern, remove
					mirrorsRows = [item for item in mirrorsRows if item not in oMirrorsRows]
			
					#transpose cols and rows
					transpattern = list(map(''.join, map(list, zip(*altpattern))))
			
					#print('\nSeek Column Mirrors:')
			
					mirrorsCols = seekMirrors(transpattern)
					#print('mirrorsCols: %s' % mirrorsCols)
					#if reflection already in original pattern, don't count
					mirrorsCols = [item for item in mirrorsCols if item not in oMirrorsCols]
					
					#print('mirrorsRows: %s' % mirrorsRows)
					#print('mirrorsCols: %s' % mirrorsCols)
					
					rowsBefore =sum(mirrorsRows)
					colsBefore =sum(mirrorsCols)
					if (rowsBefore + colsBefore) > 0:
						#print('Smudge found')
						#drawPattern(altpattern)
						
						#print('Rows Before: %d' % rowsBefore)
						#print('Cols Before: %d' % colsBefore)
						
						sumRowsBefore2 += rowsBefore
						sumColsBefore2 += colsBefore
						#print('Sum of rows Before: %d' % sumRowsBefore2)
						#print('Sum of cols Before: %d' % sumColsBefore2)
						
						found = True
						break
		if (rowsBefore + colsBefore == 0):
			print('\n***************\n' + 'NO SMUDGE FOUND' + '\n***************\n')

	# To summarize your pattern notes,
	#add up the number of columns to the left of each vertical line of reflection;
	#to that, also add 100 multiplied by the number of rows above each horizontal line of reflection
	
	total = sumRowsBefore1 * 100 + sumColsBefore1
	print('Total 1: %d' % total)
	
	total = sumRowsBefore2 * 100 + sumColsBefore2
	print('Total 2: %d' % total)

main()
# Result: 32069