import sys
import re

def process_file(file_path):
	sum_not_possible = 0
	total = 0
	with open(file_path, 'r') as file:
		for line in file:
			id_pattern = re.compile(r'Game (\d+): (.+)')
			match = id_pattern.match(line)
			#if match:
			game_id = int(match.group(1))
			total = total + game_id
			records = match.group(2)
			record_list = records.split(';')
			for record in record_list:
				set_pattern = re.compile(r'(\d+)\s+(\w+)')
				matches = set_pattern.findall(record)
				is_not_possible = False
				for match in matches:
					number, color = match
					if color == "red" and int(number) > 12:
						sum_not_possible = sum_not_possible + game_id
						#print(game_id)
						is_not_possible = True
						break
					if color == "green" and int(number) > 13:
						sum_not_possible = sum_not_possible + game_id
						#print(game_id)
						is_not_possible = True
						break
					if color == "blue" and int(number) > 14:
						sum_not_possible = sum_not_possible + game_id
						#print(game_id)
						is_not_possible = True
						break
				if is_not_possible:
					#print(record)
					break
	print(total-sum_not_possible)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python part1.py input.txt")
		sys.exit(1)

	input_file = sys.argv[1]
	process_file(input_file)
