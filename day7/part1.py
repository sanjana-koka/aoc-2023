import sys

#ranked = []

def find_matches(hands, card_ind, ranked):
	#if (len(hands) < 1):
	#	return

	strengths = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
	matches = []
	s_ind = len(strengths) - 1
	while len(matches) <= 0 and s_ind >= 0:
		for hand in hands:
			if hand[card_ind] == strengths[s_ind]:
				matches.append(hand)
				#print(hand[card_ind])
		s_ind -= 1
	
	leftover = list(set(hands) - set(matches))
	#print(f"hands: {hands}, ind: {card_ind}, matches: {matches}, leftover: {leftover}")
	#print(ranked)
	next = card_ind + 1
	#if len(matches) > 0 and next < 5:
	#find_matches(matches, next, ranked)
	#if len(leftover) > 0:
	#find_matches(leftover, card_ind, ranked)
	
	if len(hands) == 0:
		return ranked
	if len(hands) == 1:
		ranked.append(hands[0])
		hands = []
		#hands.remove(matches[0])
		#print(f"RANK: {ranked}")
		#find_matches(hands, card_ind, ranked)
	else:
		#next = card_ind + 1
		if len(matches) > 0 and next < 5:
			find_matches(matches, next, ranked)
		if len(leftover) > 0 and card_ind < 5:
			find_matches(leftover, card_ind, ranked)
		#leftover = list(set(hands) - set(matches))
		



def process_file(file_path):
	bids = {}
	with open(file_path, 'r') as file:
		for line in file:
			bids[line.split(" ")[0]] = line.split(" ")[1]	

	# map representing the cards for each type in order of their rank
	# 5 kind, 4 kind, full house, 3 kind, 2 pair, 1 pair, high card 
	types = {
		0: [],
		1: [],
		2: [],
		3: [],
		4: [],
		5: [],
		6: [],
	}

	for hand, bid in bids.items():
		#print(f"{hand} {bid}") 
		dups = {}
		for card in list(hand):
			#print(card)
			if card in dups:
				dups[card] += 1
			else:
				dups[card] = 1
		
		type = "high_card_0"
		for card, num_dups in dups.items():
			# 5 kind
			if num_dups == 5:
				type = "five_kind_6"
			# 4 kind
			if num_dups == 4:
				type = "four_kind_5"
			# 3 kind
			if num_dups == 3:
				# full house - check if the type has been set to 1 pair
				if type == "one_pair_1":
					type = "full_house_4"
				else:
					type = "three_kind_3"
			# 2 kind (1 pair)
			if num_dups == 2:
				# 2 pair - check if type has been set to 1 pair
				if type == "one_pair_1":
					type = "two_pair_2"
				# full house - check if type has been set to 3 kind
				elif type == "three_kind_3":
					type = "full_house_4"
				else:
					type = "one_pair_1"
		#print(type)
		index = type.split('_')[2]
		types[int(index)].append(hand)
	#print(types)

	# rank the hands
	#strengths = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
	strengths = {'A':1, 'K':2, 'Q':3, 'J':4, 'T':5, '9':6, '8':7, '7':8, '6':9, '5':10, '4':11, '3':12, '2':13}
		
	# first order based off of type
	# if there are multiple of the same type, rank by the strength of hand
	
	ranked = []
	
	for type, hands in types.items():
		#print(ind)
		#print(f"{type}: {hands}")
		if len(hands) == 0:
			continue
		elif len(hands) == 1:
			ranked.append(hands[0])
		else:
			
			strength_to_hand = {}
			
			for hand in hands:
				strength = 0
				for i in range(len(hand)):
					strength = strength * 100 + strengths[hand[i]]
				strength_to_hand[strength] = hand
			#print(strength_to_hand)
			
			s = list(strength_to_hand.items())
			n = len(s)
			for i in range(n):
				for j in range(0, n - i - 1):
					if s[j] < s[j + 1]:
						s[j], s[j + 1] = s[j + 1], s[j]

			for val in s:
				ranked.append(val[1])
			
				
			"""	
			# compare the strength of each hand left
			# find the strongest hand in the list hands
			card_ind = 0
			#while len(hands) > 0 :
			sub_ranked = find_matches(hands, 0, ranked)
			#print(f"sub_rank: {ranked}")
			#print(f"AFTER FUNC RANK: {ranked}")
				#hands = list(set(hands) - set(sub_ranked))

				#matches = []
				#s_ind = len(strengths) - 1
				#while len(matches) <= 0 and s_ind >= 0:
				#	for hand in hands:
				#		if hand[card_ind] == strengths[s_ind]:
				#			matches.append(hand)
				#			#print(hand[card_ind])
				#	s_ind -= 1
				#matches = find_matches(hands, card_ind)
				#print(f"hands: {hands}, matches: {matches}")
				#print(f"ranked: {ranked}")
				#if len(matches) == 0:
				#	break
				#elif len(matches) == 1:
				#	ranked.append(matches[0])
				#	hands.remove(matches[0])
				#	#print(f"ranked: {ranked}")
				#else:
				#	card_ind += 1
				#	if card_ind >= 5:
				#		print(f"hands: {hands}, matches: {matches}")
			"""
		#print(f"type: {type}, ranked: {ranked}")
	print(ranked)
	# calculate winnings
	winnings = 0
	for i, hand in enumerate(ranked):
		rank = i + 1
		bid = bids[hand]
		winnings += rank * int(bid)
		#print(f"hand: {hand}, rank: {rank}, bid: {bid}")
	print(winnings)	

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 part1.py input.txt")
		sys.exit(1)
	input_file = sys.argv[1]
	process_file(input_file)
