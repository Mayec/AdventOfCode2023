import re

def gearRatio(line, rangeStart, rangeEnd):
	ratio = 0
	numsFound = 0
	
	n = re.compile(r'\d+') #detects numbers
	for nmatch in n.finditer(line):
		number = nmatch.group()
		nstart = nmatch.start()
		nend = nmatch.end()
		nlen = nend - nstart
		
		#print("-----")
		#print("rangeStart: " + str(rangeStart))
		#print("rangeEnd: " + str(rangeEnd))
		#print("nstart: " + str(nstart))
		#print("nend: " + str(nend))
		#print("nlen :" + str(nlen))
		
		if (nstart+nlen > rangeStart) and (nstart <= rangeEnd):
			print("-----")
			print("Gear number: " + str(number))
			numsFound += 1
			# gear ratio is the result of multiplying those two numbers together.
			if ratio==0:
				ratio = int(number)
			else:
				ratio *= int(number)
	return [ratio, numsFound]

def calcGears(ltop, lcen, lbot):
	sum = 0
	if not lcen:
		print("Center line empty. Do nothing")
	else:		
		print("\n====================")
		print("line A: " + str(ltop[0:-1]))
		print("line B: " + str(lcen[0:-1]))
		print("line C: " + str(lbot[0:-1]))
		
		g = re.compile(r'\*{1}')
		for gmatch in g.finditer(lcen):
			
			# gear ratio is the result of multiplying those two numbers together.
			ratio = 1;
		
			# we found a number on the center line
			if gmatch:
				gpos = gmatch.start()
				
				print("---\nPotential gear")
				
				rangeStart = max(gpos-1, 0)
				rangeEnd = gpos+1
				
				numsFound = 0
				#Check for adjacent numbers on adjacent lines, and multiply them
				if ltop:
					resultTop = gearRatio(ltop, rangeStart, rangeEnd)
					ratioTop = resultTop[0]
					if ratioTop > 0:
						numsFound += resultTop[1]
						ratio *= ratioTop
				if lcen:
					resultCen = gearRatio(lcen, rangeStart, rangeEnd)
					ratioCen = resultCen[0]
					if ratioCen > 0:
						numsFound += resultCen[1]
						ratio *= ratioCen
				if lbot:
					resultBot = gearRatio(lbot, rangeStart, rangeEnd)
					ratioBot = resultBot[0]
					if ratioBot > 0:
						numsFound += resultBot[1]
						ratio *= ratioBot

			if numsFound>1:
				print("Gear Ratio: " + str(ratio)) 
				sum += ratio
				print("Ratios sum: " + str(sum)) 
			
	return sum

def main():
	#input = open("aoc2023_day3_testinput.txt", "r")
	input = open("aoc2023_day3_input.txt", "r")
	total = 0

	# storage for three working lines
	ltop = []
	lcen = []
	lbot = []

	for line in input:
		# shift line cursors down a position
		ltop = lcen
		lcen = lbot
		lbot = line
		
		total += calcGears (ltop, lcen, lbot)
		print("Total :" + str(total));
		
	# after reading whole file, one more run to check last line
	ltop = lcen
	lcen = lbot
	lbot = []
		
	total += calcGears(ltop, lcen, lbot)

	print("\n====================")
	print("Final Total: " + str(total))

main()
# Result: 79844424 is too high