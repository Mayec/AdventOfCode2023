import re

def main():
	#input = open("aoc2023_day4_testinput.txt", "r")
	input = open("aoc2023_day4_input.txt", "r")
	total = 0

	copies = {}
	i = 0

	for line in input:
		print("=========")
		print(line)
		
		if i in copies:
			copies[i] += 1;
		else:
			copies[i] = 1;
		
		wins = 0
		
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
				print (n + " is a winner")
				wins += 1
				icopy = i + wins
				if icopy in copies:
					copies[icopy] += copies[i];
				else:
					copies[icopy] = copies[i];
				#print("Copies: " + str(copies))
		
		#print("Copies: " + str(copies))
		i += 1
		
	for value in copies.values():
		total += value
	
	print("Total: " + str(total))
	
main()
# Result: 11827296