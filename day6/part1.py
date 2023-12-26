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
		time = int(times[i])
		dist = int(dists[i])
		winners = 0
		for i in range(time):
			curr = i * (time - i)
			if curr > dist:
				winners += 1
		print(winners)
		total *= winners
		# x = time +- sqrt(time^2 - 4dist) / 2
		max = 2 * math.sqrt(time**2 - 4*dist)
		min = 2 * math.sqrt(time**2 - 4*dist)
		diff = math.floor(max) - math.floor(min) + 1
		#print(diff)
		#print(f"time: {time}, dist: {dist}")
	print(total)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 part1.py input.txt")
		sys.exit(1)
	
	input_file = sys.argv[1]
	process_file(input_file)
