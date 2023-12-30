import sys
from functools import reduce

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return abs(a * b) // gcd(a, b) if a and b else 0

def lcm_of_list(numbers):
	return reduce(lcm, numbers)

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
	#node = 'AAA'
	

	#find a all nodes ending with A
	nodes = []
	for key in map.keys():
		if key[2] == 'A':
			nodes.append(key)

	#print(nodes)

	step_found = []
	for n in nodes:
		step_found.append(0)
	num_z = 0
	
	while not isFound:	
		for dir in directions:
			#print(steps)
			steps += 1
			for i, node in enumerate(nodes):
				#steps += 1
				if dir == 'R':
					next_node = map[node][1]
				else:
					next_node = map[node][0]
				if next_node[2] == 'Z':
					if step_found[i] == 0:
						step_found[i] = steps
						num_z += 1
				#print(f"{node} -> {next_node}")
				nodes[i] = next_node
			if num_z == len(nodes):
				isFound = True
				break
			
	#print(step_found)
	print(lcm_of_list(step_found))
		
	
		
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage python3 part1.py input.txt")
		sys.exit(1)
	input_file = sys.argv[1]
	process_file(input_file)
