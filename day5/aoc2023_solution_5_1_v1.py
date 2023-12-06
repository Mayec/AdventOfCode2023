import re

class Range:
	def __init__(self, sdestination, ssource, length):
		self.startSource = ssource
		self.startDestination = sdestination
		self.length = length

class Map:
	def __init__(self):
		self.ranges = []


def main():
	#input = open("aoc2023_day5_testinput.txt", "r")
	input = open("aoc2023_day5_input.txt", "r")
	answer = -1
	
	almanach = input.read()

	# Seeds input to list
	seedsEntry = re.search(r'seeds: [\d ]+', almanach).group()
	seeds = re.findall(r'\S+', seedsEntry.split(':')[1])
	
	# Store separate strings by input map entries
	mapEntries = []
	mapEntries.append( re.search(r'seed-to-soil map:[\n\d ]+', almanach).group() )
	mapEntries.append( re.search(r'soil-to-fertilizer map:[\n\d ]+', almanach).group() )
	mapEntries.append( re.search(r'fertilizer-to-water map:[\n\d ]+', almanach).group() )
	mapEntries.append( re.search(r'water-to-light map:[\n\d ]+', almanach).group() )
	mapEntries.append( re.search(r'light-to-temperature map:[\n\d ]+', almanach).group() )
	mapEntries.append( re.search(r'temperature-to-humidity map:[\n\d ]+', almanach).group() )
	mapEntries.append( re.search(r'humidity-to-location map:[\n\d ]+', almanach).group() )
	
	# Convert data from map entries strings to Map objectsand their list of Ranges
	maps = []
	for i in range( len(mapEntries) ):
		entry = mapEntries[i].split(':\n')[1]
		map = Map()
		maps.append(map)
		for line in entry.split('\n'):
			rangeData = line.split(' ')
			if len(rangeData) == 3:
				map.ranges.append( Range(int(rangeData[0]), int(rangeData[1]), int(rangeData[2])) )

	# Convert seeds to their locations
	for seed in seeds:
		print('----')
		print('Seed number: ' + seed)
		seednum = int(seed)
		
		i = 0
		for map in maps:
			i += 1
			#print('Checking map ' + str(i))
			
			if i == 1:
				sourcenum = seednum
			else:
				sourcenum = destnum
			# by default, if source is not found in maps, destiny will be the same
			destnum = sourcenum
			
			for rangevals in map.ranges:
				#print('startSource: ' + str(rangevals.startSource))
				#print('startDestination: ' + str(rangevals.startDestination))
				#print('length: ' + str(rangevals.length))
				
				rangeSource = range(rangevals.startSource, rangevals.startSource + rangevals.length)
				if sourcenum in rangeSource:
					index = rangeSource.index(sourcenum)
					destnum = rangevals.startDestination + index
			#print('Destination: ' + str(destnum))
		
		print('Location: ' + str(destnum))
		if answer == -1:
			answer = destnum
		else:
			answer = min(answer, destnum)
		print('Lowest location: ' + str(answer))

main()
# Result: 379811651