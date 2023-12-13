import re

def main():
	#input = open("aoc2023_day12_testinput.txt", "r")
	input = open("aoc2023_day12_input.txt", "r")
	total = 0
	
	springs = []
	groups = []
	for line in input:
		spring, group = line.split()
		springs.append(spring)
		groups.append(list(map(int, group.split(','))))

	#print(springs)
	#print(groups)
	
	for i in range(len(springs)):
		spLine = springs[i]
		grLine = groups[i]
		
		print('Checking springs line %d: %s' % (i,spLine))
		
		
		valid = 0
		slots = spLine.count('?')
		ncombos = pow(2, slots)
		#scan all different combos of ? replacements
		for j in range(ncombos):
			binary = format(j, '0'+str(slots)+'b')
			combo = ''
			replaceindex = 0
			for c in spLine:
				if c == '?':
					if binary[replaceindex] == '0': newchar = '#'
					else: newchar = '.'
					replaceindex += 1
				else:
					newchar = c	
				combo += newchar
			combogroups = re.findall('#+', combo)
			combolengths = list(map(len, combogroups))
			
			#print('---')
			#print(combo)
			#print(combogroups)
			#print(combolengths)
			
			if combolengths == grLine:
				valid += 1
				
		total += valid
	
	print('Result: %d' % total)

main()
# Result: 