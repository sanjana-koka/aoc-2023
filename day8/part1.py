import sys

def process_file(file_path):
	with open(file_path, 'r') as file:
		lines = file.read().split("\n")
		directions = ""
		dirComp = False
		map = {}
		
		# create a dict that represents the map input
		for i, line in enumerate(lines):
			#print(i)
			if not line.strip():
				#print(directions)
				dirComp = True
				continue
			if not dirComp:
				directions = directions + line
			else:
				halves = line.split("=")
				key = halves[0].strip()
				l_val = halves[1][2:5]
				r_val = halves[1][7:10]
				map[key] = [l_val, r_val]
				#print(f"{key} = ({l_val}, {r_val})")			
		#print(map)

	steps = 0
	isFound = False
	node = 'AAA'
			
	while not isFound:
		for dir in directions:
			steps += 1
			if dir == 'R':
				node = map[node][1]
			else:
				node = map[node][0]
			if node == 'ZZZ':
				isFound = True
				break
	print(steps)
		
		
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage python3 part1.py input.txt")
		sys.exit(1)
	input_file = sys.argv[1]
	process_file(input_file)
