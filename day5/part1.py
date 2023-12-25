import sys
import string

def find_match(search_val, lines):
	# strip empty values
	lines = [value for value in lines if value]
	# search for search val in map
	for line in lines:
		vals = line.split(" ")
		dest = int(vals[0])
		start = int(vals[1])
		range_len = int(vals[2])
		end = start + range_len
		
		if start <= search_val <= end:
			return dest + (search_val - start)

	#return val if it's not in map
	return search_val

def process_file(file_path):
	with open(file_path, 'r') as file:
		maps = file.read().split('\n\n')
		#for line in file:
		#	print(line)
	
	seeds = maps[0].split(": ")[1].split(" ")
	soils = []
	ferts = []
	waters = []
	lights = []
	temps = []
	humidities = []
	locs = []
	
	for i, map in enumerate(maps[1:]):
		lines = map.split('\n')
		name = lines[0].split(" ")[0]
		if name == "seed-to-soil":
			for seed in seeds:
				soil = find_match(int(seed), lines[1:]) 
				soils.append(soil)
		elif name == "soil-to-fertilizer":
			for soil in soils:
				fert = find_match(soil, lines[1:])
				ferts.append(fert)
		elif name == "fertilizer-to-water":
			for fert in ferts:
				water = find_match(fert, lines[1:])
				waters.append(water)
		elif name == "water-to-light":
			for water in waters:
				light = find_match(water, lines[1:])
				lights.append(light)
		elif name == "light-to-temperature":
			for light in lights:
				temp = find_match(light, lines[1:])
				temps.append(temp)
		elif name == "temperature-to-humidity":
			for temp in temps:
				humidity = find_match(temp, lines[1:])
				humidities.append(humidity)
		elif name == "humidity-to-location":
			for humidity in humidities:
				loc = find_match(humidity, lines[1:])
				locs.append(loc)

	print(min(locs))
	
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python part1.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)
