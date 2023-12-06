import re

def main():
	#input = open("aoc2023_day4_testinput.txt", "r")
	input = open("aoc2023_day4_input.txt", "r")
	total = 0

	for line in input:
		print("=========")
		print(line)
		
		score = 0
		
		lclean = line.split(":")[1]
		lsplit = lclean.split("|")
		swinners = lsplit[0] # string containing winning numbers
		sowned = lsplit[1] # string containting owned numbers
		
		nwinners = re.findall(r'\S+', swinners)
		nowned = re.findall(r'\S+', sowned)
		#print(nwinners)
		#print(nowned)
		
		for n in nowned:
			if n in nwinners:
				#print(n + " is a win")
				if score == 0:
					score = 1
				else:
					score *= 2
		total += score
	print("Total: " + str(total))
	
main()
# Result: 21568