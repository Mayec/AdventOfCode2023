from functools import cache

# functools.cache, used as the @cache decorator below, is vital to keep this speedy enough

@cache
def marchcombo( springs, groups ):
	
	#print(springs)
	#print(groups)
	
	# Stop conditions
	if len(groups) == 0: # no more # from groups to place
		#print('END A')
		return 1 if '#' not in springs else 0
	if sum(groups) + len(groups) -1 > len(springs): # no more space left for #
		#print('END B')
		return 0
		
	# '.' next -> Recursion skip
	if springs[0] == '.':
		return marchcombo( springs[1:], groups )

	# '?' next -> Recursion try as if it is '.'
	count = 0
	if springs[0] == '?':
		#print('? for .')
		count += marchcombo( springs[1:], groups)

	#print('cont.')
	#print(springs)
	#print(groups)

	# try to populate with groups of #
	# but first, check if enough space in springs, with a possible '.' right after:
	if '.' not in springs[:groups[0]]:
		if (len(springs) == groups[0]) or ((len(springs) > groups[0]) and (springs[groups[0]] != '#')):
			#print('place group: %s' % (groups[0] * '#'))
			offset = groups[0]+1
			count += marchcombo( springs[offset:], groups[1:] )
	return count

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
	#for i in range(2,3): # TEST single
		spLine = springs[i]
		grLine = groups[i]
		
		#print('Checking springs line %d: %s' % (i,spLine))
		
		# Unfold
		# replace the list of spring conditions with five copies of itself (separated by ?)
		mult = 5
		spLine = (mult * (spLine + '?'))[:-1]
		grLine = mult * grLine
		
		#print(spLine)
		#print(grLine)
		
		vcombos = marchcombo( tuple(spLine), tuple(grLine) ) #tuples are hashable, for cache
		#print(vcombos)
		total += vcombos
		
		print('checked line: %d' % i)
	
	print('Result: %d' % total)

main()
# Result: 850504257483930