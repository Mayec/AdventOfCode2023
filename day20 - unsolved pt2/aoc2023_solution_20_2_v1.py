import math

class Module:
	def __init__(self, name, type, destinations):
		self.name = name
		self.destinations = destinations
		
	def __repr__(self):
		#return self.type + '/' + self.name + ' -> [' + str(self.destinations)[1:] + ']'
		return self.name
		
	def resolve(self, pulse, time):
		return []
		
	def reset(self):
		pass

class Broadcaster(Module):
	def __init__(self, name, destinations):
		self.name = name
		self.type = 'bc'
		self.destinations = destinations
	
	def resolve(self, pulse, time):
		new_pulses = []
		for dest in self.destinations:
			new_pulse = Pulse(time+1, pulse.type, self.name, dest)
			new_pulses.append(new_pulse)
		return new_pulses

class FlipFlop(Module):
	def __init__(self, name, destinations):
		self.name = name
		self.type = '%'
		self.destinations = destinations
		self.onstate = False
		
	def resolve(self, pulse, time):
		new_pulses = []
		if pulse.type == 0:
			if self.onstate:
				type = type = 0
			else:
				type = 1
			for dest in self.destinations:
				new_pulse = Pulse(time+1, type, self.name, dest)
				new_pulses.append(new_pulse)
			self.onstate = not self.onstate # flip module onstate
		return new_pulses
		
	def reset(self):
		self.onstate = False

class Conjunction(Module):
	def __init__(self, name, destinations):
		self.name = name
		self.type = '&'
		self.destinations = destinations
		self.memory = {}
		
	def resolve(self, pulse, time):
		new_pulses = []
		inmod = pulse.origin
		self.memory[inmod] = pulse.type
		fullmem = 1
		#print('%s: %s' % (self.name, self.memory))
		for bit in self.memory.values():
			fullmem *= bit
		if fullmem == 1:
			type = 0
		else:
			type = 1
		for dest in self.destinations:
			new_pulse = Pulse(time+1, type, self.name, dest)
			new_pulses.append(new_pulse)
		return new_pulses
		
	def reset(self):
		for reg in self.memory:
			reg = 0
		
class Pulse():
	def __init__(self, time, type, origin, destination):
		self.time = time
		self.type = type # 0 for low pulse, 1 for high pulse
		self.origin = origin
		self.destination = destination
	
	def __repr__(self):
		return str(self.time) + '|' + self.origin + ':' + str(self.type) + '->' + self.destination

def propagate(time):
	global pulses
	global modules
	global hiCount
	global loCount
	
	# split out pulses that match current time into "pending"
	pending = list( filter(lambda x: x.time == time, pulses) )
	pulses = list( filter(lambda x: x.time > time, pulses) )
	
	for pulse in pending:
		if pulse.type == 1:
			hiCount += 1
		else:
			loCount +=1
		modname = pulse.destination		
		
		#print(modules)
		#print(modname)
		
		module = list( filter(lambda x: x.name == modname, modules) )[0]
		newPulses = module.resolve(pulse, time)
		pulses += newPulses

def waitFirstPulse(mod, type):
	global pulses
	global modules
	cycles = 0
	found = False
	while not found: # Repeat enlessly until hero sends pulse of specified type
		cycles += 1
		#print('Cycle %d:' % c)
		# Start first cycle by sending pulse to broadcast
		time = 0
		pulses = [Pulse(time, 0, 'button', 'broadcaster')]
		
		while len(pulses) > 0:
			#print(pulses)
			for pulse in pulses:
				if pulse.origin == mod and pulse.type == type:
					found = True
			else:
				propagate(time)
				time += 1
	return cycles


def main():
	#input = open("aoc2023_day20_testinput.txt", "r")
	#input = open("aoc2023_day20_testinput2.txt", "r")
	input = open("aoc2023_day20_input.txt", "r")
	total = 0

	cycles = 1000
	#cycles = 1 # TEST single cycle
	
	global modules
	global pulses
	global hiCount
	global loCount

	# Ingest input data into modules list
	input = input.read().split('\n')
	modules	= []
	conjunctions = []
	for line in input:
		name, destinations = line.split(' -> ')
		destinations =destinations.split(', ')
		# New module is Flip-flop
		if name[0] == '%':
			name = name[1:]
			mod = FlipFlop(name, destinations)
		# New module is Conjunction
		elif name[0] == '&':
			name = name[1:]
			mod = Conjunction(name, destinations)
			conjunctions.append(mod)
		# New module is Broadcaster
		else:
			mod = Broadcaster(name, destinations)
		modules.append(mod)
	#print(modules)
	
	# Add deadend modules (listed as destinations, but never as origins)
	for mod in modules:
		for dest in mod.destinations:
			if dest not in modules:
				modules.append( Module(dest, None, []) )
	
	# For all conjunction modules, initialize the memory for all their input modules
	for con in conjunctions:
		cname = con.name
		for mod in modules:
			if cname in mod.destinations:
				con.memory[mod.name] = 0
	
	hiCount = 0
	loCount = 0
	
	# [rx] receiving low pulse dependes on:
	# [mp, qt, qb, ng] all sending high pulses
	
	heroes = ['mp', 'qt', 'qb', 'ng']
	cycles = []
	
	for hero in heroes:
		print(hero)
		for mod in modules:
			mod.reset()
		cycles.append( waitFirstPulse(hero, 1) )
		print(cycles)
	
	total = math.lcm(*cycles)
	print('Total: %d' % total)
	

main()
# Result: 5916687255 is too low (5,916,687,255)
# Correct answer should be: 247702167614647 (247,702,167,614,647)