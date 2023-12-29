import sys

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

		# handle case when there are multiple values with the max dup
		strength_arr = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
		
		#max_keys = [key for key, value in dups.items() if value == max(dups.values())]
		
		j = dups.get('J', 0)
		if j > 0:
			no_j = dups.copy()
			del no_j['J']
			#print(no_j)
			max_keys = [key for key, value in no_j.items() if value == max(no_j.values())]
			if len(max_keys) >= 1:
				max_key = max_keys[0]
				dups[max_key] += j
				del dups['J']
		#print(f"key: {max_key}, val: {max_val}")
		
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
		index = type.split('_')[2]
		types[int(index)].append(hand)

	# rank the hands
	#strengths = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
	strengths = {'A':2, 'K':3, 'Q':4, 'J':14, 'T':5, '9':6, '8':7, '7':8, '6':9, '5':10, '4':11, '3':12, '2':13}
		
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
