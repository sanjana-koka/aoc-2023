import sys
import string


def process_file(file_path):
	total = 0
	with open(file_path, 'r') as file:
		for line in file:
			first, rest = line.split('|')
			id_, card = first.split(':')
			winners = [int(x) for x in card.split()]
			card_nums = [int(x) for x in rest.split()]
			combination = set(winners) & set(card_nums)
			matches = len(combination) - 1
			if matches < 0:
				card_total = 0
			else:
				card_total = pow(2, matches)
			total = total + card_total
	print("total: ", total)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python part1.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)
