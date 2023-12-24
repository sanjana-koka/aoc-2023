import sys
import string

def is_symbol(char):
	return char in ['!', '@', '#', '$', '%', '^', '&', '*', '/', '-', '+', '=']

def process_file(file_path):
	schematic = []
	sum = 0
	with open(file_path, 'r') as file:
		for line in file:
			row = list(line.strip())
			schematic.append(row)
	#print(schematic)
	# make a value_map containing coordinates to values
	# make a start ma
	# iterate through each value in the schematic
	row_ind = 0
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
				while end < len(row) and row[end].isdigit():
					# check to see if there is a symbol adjacent to the current value
					# up
					n = row_ind - 1
					if n >= 0 and is_symbol(schematic[n][end]):
						#print(schematic[n][end])
						adj_symbol = True
					s = row_ind + 1
					if s < len(schematic) and is_symbol(schematic[s][end]):
						#print(schematic[s][col])
						adj_symbol = True
					w = end - 1
					if w >= 0 and is_symbol(schematic[row_ind][w]):
						#print(schematic[row_ind][w])
						adj_symbol = True
					e = end + 1
					if e < len(row) and is_symbol(schematic[row_ind][e]):
						#print(schematic[row_ind][e])
						adj_symbol = True
					
					# check diagonals
					if n >= 0 and w >= 0 and is_symbol(schematic[n][w]):
						#print(schematic[n][w])
						adj_symbol = True
					if n >= 0 and e < len(row) and is_symbol(schematic[n][e]):
						#print(schematic[n][e])
						adj_symbol = True
					if s < len(schematic) and w >= 0 and is_symbol(schematic[s][w]):
						#print(schematic[s][w])
						adj_symbol = True
					if s < len(schematic) and e < len(row) and is_symbol(schematic[s][e]):
						#print(schematic[s][e])
						adj_symbol = True
					
					num = num * 10 + int(row[end])
					end += 1
				if adj_symbol:
					#print(num)
					sum += num
				#print(num)
				col += len(str(num))
			else:
				#print(element)
				col += 1
			
		row_ind += 1


	print(sum)
		# if the curr value is a symbol
		# check the value_map values adjacent to it
			# check the seen_map to see if that value has already been seen
				# if not add value to map
				# add all coordinates of that value to this seen map
					# find the length of the len(str(x))  	
	#for row in schematic:
		# iterate through each value
		# if curr is a symbol is_symbol()
		# check values all around the symbol
		
	#go through each line keep track of the index of numbers

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python part1.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)
