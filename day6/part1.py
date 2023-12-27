import sys
import math

def process_file(file_path):
	with open(file_path, 'r') as file:
		lines = file.read().split('\n')
		times = lines[0].split(':')[1].split(' ')
		times = [char for char in times if char]
		dists = lines[1].split(':')[1].split(' ')
		dists = [char for char in dists if char]
	
	total = 1
	for i in range(len(times)):
		time = float(times[i])
		dist = float(dists[i])
		
		# x = time +- sqrt(time^2 - 4dist) / 2
		max = (time + math.sqrt((time**2) - (4.0*dist))) / 2.0
		min = (time - math.sqrt((time**2) - (4.0*dist))) / 2.0
		
		diff = math.ceil(max) - math.floor(min) - 1
		total *= diff
	print(total)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 part1.py input.txt")
		sys.exit(1)
	
	input_file = sys.argv[1]
	process_file(input_file)
