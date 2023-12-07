import functools

cardtypes = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

#input = open("aoc2023_day7_testinput.txt", "r")
input = open("aoc2023_day7_input.txt", "r")

def countCards(hand):
	counts = []
	seen = []
	for card in hand:
		if not card in seen:
			seen.append(card)
			n = hand.count(card)
			counts.append(n)
	counts.sort(reverse=True)
	return counts
	

def classifyHand(hand):
	counts = countCards(hand)
	match counts[0]:
		case 5: return 6 #Five of a kind (eg. AAAAA) is type 6
		case 4: return 5 #Four of a kind (eg. AA8AA) is type 5
		case 3:
			if counts[1] == 2:
				return 4 #Full house (eg. 23332) is type 4
			else:
				return 3 #Three of a kind (eg. TTT98) is type 3
		case 2:
			if counts[1] == 2:
				return 2 #Two pair (eg. 23432) is type 2
			else:
				return 1 #One pair (eg. 23432) is type 1
		case _: return 0 #High card (eg. 23456) is type 0


def compareHands(handid1, handid2):
	hand1 = hands[handid1]
	hand2 = hands[handid2]
	for c in range(len(hand1)):
		card1 = hand1[c]
		card2 = hand2[c]
		value1 = cardtypes.index(card1)
		value2 = cardtypes.index(card2)
		if value1 == value2:
			pass
		elif value1 > value2:
			return 1
		elif value1 < value2:
			return -1
	return 0
	

def main():
	total = 0

	global hands
	hands = []
	bids = []
	types = []
	
	for i in range(7):
		types.append([])

	for line in input:
		hand, bid = line.split()
		hands.append(hand)
		bids.append(int(bid))

	#print("Hands: " + str(hands))
	#print("Bids: " + str(bids))

	# First, classify hands by type
	for i in range(len(hands)):
		hand = hands[i]
		bid = bids[i]
		
		#print('---\n' + hand)
		
		t = classifyHand(hand)
		types[t].append(i)
		
		# Log classification
		'''
		match t:
			case 6: print('Five of a kind')
			case 5: print('Four of a kind')
			case 4: print('Full house')
			case 3: print('Three of a kind')
			case 2: print('Two pair')
			case 1: print('One pair')
			case 0: print('High card')
		'''
	
	'''
	print('=====')
	for type in types:
		print(type)
	'''
	
	rank = 1
	
	# Second, sort draws within types by strength of its cards, in priority from first to last.
	for type in types:
		type = sorted(type, key=functools.cmp_to_key(compareHands), reverse=True)
	
		# Then tally each hand's wins, equal to its bid multiplied by its rank
		for handid in type:
			bid = bids[handid]
			wins = bid * rank
			total += wins
			rank += 1
			#print('Wins: ' + str(wins)) 
	print('Total: ' + str(total))
	
main()

# Result: 255048101