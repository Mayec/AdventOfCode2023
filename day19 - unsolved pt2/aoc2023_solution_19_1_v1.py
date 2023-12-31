import re


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


def applyWorkflow(part, wflow):
	for i,cond in enumerate(wflow.conds):
		#print(cond)
		cat = cond[0]
		sign = cond[1]
		val = int(cond[2:])
		passed = False
		
		# category
		if cat == 'x':
			pval = part.x
		elif cat == 'm':
			pval = part.m
		elif cat == 'a':
			pval = part.a
		elif cat == 's':
			pval = part.s
			
		# condition
		if sign == '>':
			if pval > val:
				passed = True
		elif sign == '<':
			if pval < val:
				passed = True
		
		if passed:
			return wflow.targets[i]
	# by default, if no conditions met, return last target
	return wflow.targets[-1]


def main():
	#input = open("aoc2023_day19_testinput.txt", "r")
	input = open("aoc2023_day19_input.txt", "r")
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
	
	# Parse parts_str into list of part objects
	parts_strs = [l for l in parts_strs.split('\n')]
	parts = []
	for line in parts_strs:
		x = int(re.search('x=\\d+', line).group(0).replace('x=',''))
		m = int(re.search('m=\\d+', line).group(0).replace('m=',''))
		a = int(re.search('a=\\d+', line).group(0).replace('a=',''))
		s = int(re.search('s=\\d+', line).group(0).replace('s=',''))
		new_part = Part(x,m,a,s)
		parts.append(new_part)
	
	#print(workflows)
	#print('---')
	#print(parts)
	
	# Send parts through the workflows
	accepted = [] # list of accepted parts
	for part in parts:
		#print(part)
		wflowname = 'in'
		ended = False
		while not ended:
			wflow = next((item for item in workflows if item.name == wflowname), None)
			result = applyWorkflow(part, wflow)
			if result == 'A':
				accepted.append(part)
				ended = True
			elif result == 'R':
				ended = True
			else:
				wflowname = result
	
	# Add up the components of all the accepted parts
	for part in accepted:
		total += part.x + part.m + part.a + part.s
	
	print('Total: %d' % total)
	
main()
# Result: 362930