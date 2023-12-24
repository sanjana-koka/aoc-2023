import sys
import string
from collections import defaultdict

def is_symbol(char):
	#return char in ['!', '@', '#', '$', '%', '^', '&', '*', '/', '-', '+', '=']
	return char == '*'
	
def process_file(file_path):
	schematic = []
	sum = 0
	with open(file_path, 'r') as file:
		for line in file:
			row = list(line.strip())
			schematic.append(row)
	#print(schematic)
	row_ind = 0
	# make a map of coordinates of symbols to an array of adjacent numbers
	gear_map = defaultdict(list)
	gear_map[(0,0)] = []
	while row_ind < len(schematic):
		row = schematic[row_ind]
		col = 0
		while col < len(row):
			element = row[col]
			# check if it is a number
			if element.isdigit():
				# keep note of the start index
				start = col
				num = 0
				end = col
				# iterate forward to get rest of number
				adj_symbol = False
				coords = []
				while end < len(row) and row[end].isdigit():
					# check to see if there is a symbol adjacent to the current value
					# make a list of coordinates of adjacent symbols
					n = row_ind - 1
					if n >= 0 and is_symbol(schematic[n][end]):
						#print(schematic[n][end])
						coords.append((n,end))
						adj_symbol = True
					s = row_ind + 1
					if s < len(schematic) and is_symbol(schematic[s][end]):
						#print(schematic[s][col])
						coords.append((s,col))
						adj_symbol = True
					w = end - 1
					if w >= 0 and is_symbol(schematic[row_ind][w]):
						#print(schematic[row_ind][w])
						coords.append((row_ind,w))
						adj_symbol = True
					e = end + 1
					if e < len(row) and is_symbol(schematic[row_ind][e]):
						#print(schematic[row_ind][e])
						coords.append((row_ind,e))
						adj_symbol = True
					
					# check diagonals
					if n >= 0 and w >= 0 and is_symbol(schematic[n][w]):
						#print(schematic[n][w])
						coords.append((n,w))
						adj_symbol = True
					if n >= 0 and e < len(row) and is_symbol(schematic[n][e]):
						#print(schematic[n][e])
						coords.append((n,e))
						adj_symbol = True
					if s < len(schematic) and w >= 0 and is_symbol(schematic[s][w]):
						#print(schematic[s][w])
						coords.append((s,w))
						adj_symbol = True
					if s < len(schematic) and e < len(row) and is_symbol(schematic[s][e]):
						#print(schematic[s][e])
						coords.append((s,e))
						adj_symbol = True
					
					num = num * 10 + int(row[end])
					end += 1
				#if adj_symbol:
					#print(num)
				#	sum += num
				coords = list(set(coords))
				for coord in coords:
					#print(coord)
					#print(num)
					gear_map[coord].append(num)	
				col += len(str(num))
			else:
				#print(element)
				col += 1
			
		row_ind += 1

	for key, value in gear_map.items():
		#print(key)
		#print(value)
		if (len(value) == 2):
			ratio = value[0] * value[1]
			#print(ratio)
			sum += ratio
	print(sum)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python part1.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)
