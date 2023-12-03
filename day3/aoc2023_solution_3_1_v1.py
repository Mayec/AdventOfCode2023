import re

def validNumbers(ltop, lcen, lbot):
	sum = 0
	if not lcen:
		print("Center line empty. Do nothing")
	else:		
		print("\n====================")
		print("line A: " + str(ltop[0:-1]))
		print("line B: " + str(lcen[0:-1]))
		print("line C: " + str(lbot[0:-1]))
		
		n = re.compile(r'\d+')
		for nmatch in n.finditer(lcen):
		
			# we found a number on the center line
			if nmatch:
				number = nmatch.group()
				start = nmatch.start()
				end = nmatch.end()
				
				print("---\nNumber: " + number)
				
				valid = False
				
				rangeStart = max(start-1, 0)
				rangeEnd = end+1
				
				regex = '[^.0-9\n]' #detects non-digits that are not a .
				
				#Check for adjacent symbols on top line
				if ltop:					
					substring = str(ltop[rangeStart:rangeEnd])					
					s = re.findall(regex, substring)
					print("A symbols: " + str(s))
					if s: valid = True
				
				#Check for adjacent symbols on center line
				if lcen:				
					substring = str(lcen[rangeStart:rangeEnd])
					s = re.findall(regex, substring)
					print("B symbols: " + str(s))
					if s: valid = True
					
				#Check for adjacent symbols on bottom line
				if lbot:
					substring = str(lbot[rangeStart:rangeEnd])					
					s = re.findall(regex, substring)
					print("C symbols: " + str(s))
					if s: valid = True
				
				if valid: sum += int(number)
				print ("valid: " + str(valid))
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
		
		total += validNumbers (ltop, lcen, lbot)
		
	# after reading whole file, one more run to check last line
	ltop = lcen
	lcen = lbot
	lbot = []
		
	total += validNumbers (ltop, lcen, lbot)

	print(total);

main()
# Result: 535235