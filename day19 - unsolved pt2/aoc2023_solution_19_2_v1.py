# Doesn't work right now, as I parse all workflows as if they all endend in
# acceptance ('A'). Need to start from end states 'A', and then parse backwards
# as I accumulate condition mins and maxes.

import re
import math

class Part:
	def __init__(self, x, m, a, s):
		self.x = x
		self.m = m
		self.a = a
		self.s = s
	
	def __repr__(self): 
		return ('Part x:' + str(self.x) + ',m:' + str(self.m) + ',a:' + str(self.a) + ',s:' + str(self.s))


class Workflow:
	def __init__(self, name):
		self.name = name
		self.conds = []
		self.targets = []
	
	def __repr__(self): 
		return ('Workflow ' + self.name)


def accConstraints(wflow, limits):
	cats = {'x':0, 'm':1, 'a':2, 's':3}
	result = limits
	for i,cond in enumerate(wflow.conds):
		cat = cond[0]
		sign = cond[1]
		val = int(cond[2:])
		
		# condition
		if sign == '>':
			current = result[cats[cat]][0]
			result[cats[cat]][0] = max(current, val+1)
		elif sign == '<':
			current = result[cats[cat]][1]
			result[cats[cat]][1] = min(current, val-1)
	return result


def main():
	input = open("aoc2023_day19_testinput.txt", "r")
	#input = open("aoc2023_day19_input.txt", "r")
	total = 0

	# Ingest input data
	workflows_strs, parts_strs = input.read().split('\n\n')
	
	# Parse workflows_str into list of workflow objects
	workflows_strs = [l for l in workflows_strs.split('\n')]
	workflows = []
	for line in workflows_strs:
		name,instructions = line.split('{')
		new_wflow = Workflow(name)
		instructions = instructions[:-1].split(',')
		for i,inst in enumerate(instructions):
			if ':' in inst:
				cond,target = inst.split(':')
				new_wflow.conds.append(cond)
			else:
				target = inst
			new_wflow.targets.append(target)
		workflows.append(new_wflow)
	
	# Accumulate constraints
	xmin = 0
	xmax = math.inf
	mmin = 0
	mmax = math.inf
	amin = 0
	amax = math.inf
	smin = 0
	smax = math.inf
	limits = [[xmin, xmax], [mmin, mmax], [amin, amax], [smin, smax]]
	for wflow in workflows:
		limits = accConstraints(wflow, limits)
	print(limits)
	
	# Calculate combinations
	xmin = limits[0][0]
	xmax = limits[0][1]
	mmin = limits[1][0]
	mmax = limits[1][1]
	amin = limits[2][0]
	amax = limits[2][1]
	smin = limits[3][0]
	smax = limits[3][1]
	total = (xmax-xmin) * (mmax-mmin) * (amax-amin) * (smax-smin)
	print('Total: %d' % total)
	
main()
# Result: 362930