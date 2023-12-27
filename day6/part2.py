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
	time_long = ""
	dist_long = ""
	
	for i in range(len(times)):
		time_long += times[i]
		dist_long += dists[i]


	time = int(time_long)
	dist = int(dist_long)
	
	#x = time +- sqrt(time^2 - 4dist) / 2
	max = (time + math.sqrt((time**2) - (4*dist))) / 2
	min = (time - math.sqrt((time**2) - (4*dist))) / 2
	diff = math.floor(max) - math.ceil(min) + 1
	
	print(diff)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 part1.py input.txt")
		sys.exit(1)
	
	input_file = sys.argv[1]
	process_file(input_file)
