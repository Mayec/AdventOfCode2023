# This one takes too long. About 15h to finish

import re
import time

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

	# Seeds input to list of seed ranges
	seedsEntry = re.search(r'seeds: [\d ]+', almanach).group()
	seedRangesStr = re.findall(r'\d+ \d+', seedsEntry.split(':')[1])
	seedRanges = []
	for s in seedRangesStr:
		seedRanges.append(s.split(' '))
	#print(seedRanges)
	
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
	
	# Total over 2.16 Billion seeds
	print('Exploding seed ranges...')
	tstart = time.time()
	seedcount = 0
	
	#for srange in seedRanges: # <----------------PRODUCTION
	for srange in seedRanges[0:1]: #TEST single
	
		srangeStart = int(srange[0])
		srangeLength = int(srange[1])	
		
		#TIME
		timeA = 0
		timeB = 0
		timeC = 0
		
		#for seednum in range(srangeStart, srangeStart+srangeLength): # <----------------PRODUCTION
		for seednum in range(srangeStart, srangeStart+10000): #TEST reduced	
			#print('Seed: ' + str(seednum))
			
			seedcount += 1
			
			# Iterate through maps to find location corresponding to seed
			i = 0
			for map in maps:
				time0 = time.time() #TIME
				i += 1
				#print('Checking map ' + str(i))
				
				timeA += time.time() - time0 #TIME
				time0 = time.time() #TIME
				
				if i == 1:
					sourcenum = seednum
				else:
					sourcenum = destnum
				# by default, if source is not found in maps, destiny will be the same
				destnum = sourcenum
				
				timeB += time.time() - time0 #TIME
				time0 = time.time() #TIME
				
				for rangevals in map.ranges:			
					#rangeSource = range(rangevals.startSource, rangevals.startSource + rangevals.length)
					#if sourcenum in rangeSource:
					#	index = rangeSource.index(sourcenum)
					#	destnum = rangevals.startDestination + index
					
					if (sourcenum >= rangevals.startSource) and (sourcenum < rangevals.startSource + rangevals.length):
						index = sourcenum - rangevals.startSource
						destnum = rangevals.startDestination + index
					
				#print('Destination: ' + str(destnum))		
				
				timeC += time.time() - time0 #TIME
				time0 = time.time() #TIME
			
			#print('Location: ' + str(destnum))
			if answer == -1:
				answer = destnum
			else:
				answer = min(answer, destnum)
			
			# print progress ever certain amount of seeds
			if (seedcount % 100000) == 0:
				print("---")
				print("Checked " + str(seedcount/1000000) + " million seeds")
				print('Lowest location: ' + str(answer))
				telapsed = time.time() - tstart
				print('Time elapsed: ' + str(round(telapsed, 2)) + 's')
				testimate = (2160000000 / seedcount) * telapsed
				print('ETA: ' + str( round((testimate - telapsed) / 60, 2) ) + 'min. (' + str( round(testimate / 60, 2) ) + 'min total)')
	
	print('Lowest location: ' + str(answer))
	
	#TIME
	print("----Profiling----")
	timeTotal = timeA + timeB + timeC
	if timeTotal > 0:
		print("time Total: " + str(timeTotal))
		print("time A: " + str(timeA) + " (" + str(100*timeA/timeTotal) + "%)")
		print("time B: " + str(timeB) + " (" + str(100*timeB/timeTotal) + "%)")
		print("time C: " + str(timeC) + " (" + str(100*timeC/timeTotal) + "%)")
	
main()
# Result: 