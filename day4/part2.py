import sys
import string


def process_file(file_path):
	total = 0
	instances = {1:1}
	with open(file_path, 'r') as file:
		for line in file:
			first, rest = line.split('|')
			id, card = first.split(':')
			id = int(id[5:])
			winners = [int(x) for x in card.split()]
			card_nums = [int(x) for x in rest.split()]
			combination = set(winners) & set(card_nums)
			matches = len(combination)
			
			# make map representing the number of instances of each card
			# id, num_instances
			copies = instances.setdefault(id, 1)
			for i in range(matches):
				ind = id + i + 1	
				instances[ind] = instances.setdefault(ind, 1) + 1*copies	

			#if matches < 0:
			#	card_total = 0
			#else:
			#	card_total = pow(2, matches)
			#total = total + card_total
		print(instances)
	
	print("total: ", sum(instances.values()))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python part1.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)
