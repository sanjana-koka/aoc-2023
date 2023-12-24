import sys
import re

def process_file(file_path):
	sum_not_possible = 0
	total = 0
	sum_of_powers = 0
	with open(file_path, 'r') as file:
		for line in file:
			id_pattern = re.compile(r'Game (\d+): (.+)')
			match = id_pattern.match(line)
			#if match:
			game_id = int(match.group(1))
			total = total + game_id
			records = match.group(2)
			record_list = records.split(';')
			max_red = 0
			max_green = 0
			max_blue = 0
			for record in record_list:
				set_pattern = re.compile(r'(\d+)\s+(\w+)')
				matches = set_pattern.findall(record)
				#max_red = 0
				#max_blue = 0
				#max_green = 0
				for match in matches:
					number, color = match
					if color == "red":
						max_red = max(max_red, int(number))
					if color == "green":
						max_green = max(max_green, int(number))
					if color == "blue":
						max_blue = max(max_blue, int(number))
			print(f"red: {max_red}, green: {max_green}, blue: {max_blue}") 
			power = max_red * max_green * max_blue
			sum_of_powers = sum_of_powers + power
	print(sum_of_powers)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python part1.py input.txt")
		sys.exit(1)

	input_file = sys.argv[1]
	process_file(input_file)
