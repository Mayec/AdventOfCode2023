# Unfinished
# This solution is not mine, WIP of rebuilding a code 95% lifted from a reddit post
# yet is an elegant way to immplement the main ideas I was trying to hack with my v2

import re
from functools import reduce
	
input = open("aoc2023_day5_testinput.txt", "r")
#input = open("aoc2023_day5_input.txt", "r")
answer = -1

#open('data.txt').read().split('\n\n')

seedsEntry, *mappingsEntries = input.read().split('\n\n')
seeds =  list(map(int, seedsEntry.split()[1:]))

mappings = []
for entry in mappingsEntries:
	mapping = entry.split('\n')[1:]
	mappings.append(mapping)


def lookup(inputs, mapping):
	print('---')
	print(inputs)
	print(mapping)
	
	for start, length in inputs:
		yield (start, length)
	
	'''	
	for start, length in inputs:
		while length > 0:
			for l in mapping:
				dst, src, len = map(int, l.split())
				delta = start - src
				if delta <= len:
					len = min(len - delta, length)
					yield( dst + delta, len)
					start += len
					length -= len
					break
				else:
					yield (start, length)
					break
	'''
	
#alist = zip(seeds, [1] * len(seeds)), zip(seeds[0::2], seeds[1::2])
#print(list(alist[0]))
#print(list(alist[1]))

seedRanges = zip(seeds[0::2], seeds[1::2])
print(list(seedRanges))

#foo = reduce(lookup, mappings, alist)
#print(foo)

for s in list(seedRanges):
	goo = lookup(s, mappings[0])
	print(goo)


# Result: 