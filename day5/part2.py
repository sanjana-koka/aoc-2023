import sys
import string

def parse_map(lines):
	# strip empty values
	lines = [value for value in lines if value]
	map = {}
	for line in lines:
		vals = line.split(" ")
		#print(vals)
		dest = int(vals[0])
		source = int(vals[1])
		range_len = int(vals[2])
		#print(f"dest_range_start: {dest}, source_range_start: {source}, range_len: {range_len}")
		for i in range(range_len):
			map[source] = dest
			source += 1
			dest += 1
	return map

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
	
	# populate the internal maps
	seed = 79
	soil = 0
	fert = 0
	water = 0
	light = 0
	temp = 0
	humidity = 0
	loc = 0
	
	seeds = maps[0].split(": ")[1].split(" ")
	soils = []
	ferts = []
	waters = []
	lights = []
	temps = []
	humidities = []
	locs = []
	#print(f"seeds: {seeds}")
	for i, map in enumerate(maps[1:]):
		#print(map)
		lines = map.split('\n')
		name = lines[0].split(" ")[0]
		if name == "seed-to-soil":
			for seed in seeds:
				soil = find_match(int(seed), lines[1:]) 
				soils.append(soil)
				#print(f"seed: {seed}, soil: {soil}")
			#seed_to_soil = parse_map(lines[1:])
		elif name == "soil-to-fertilizer":
			for soil in soils:
				fert = find_match(soil, lines[1:])
				ferts.append(fert)
				#print(fert)
			#soil_to_fertilizer = parse_map(lines[1:])
		elif name == "fertilizer-to-water":
			for fert in ferts:
				water = find_match(fert, lines[1:])
				waters.append(water)
				#print(water)
			#fertilizer_to_water = parse_map(lines[1:])
		elif name == "water-to-light":
			for water in waters:
				light = find_match(water, lines[1:])
				lights.append(light)
				#print(light)
			#water_to_light = parse_map(lines[1:])
		elif name == "light-to-temperature":
			for light in lights:
				temp = find_match(light, lines[1:])
				temps.append(temp)
				#print(temp)
			#light_to_temp = parse_map(lines[1:])
		elif name == "temperature-to-humidity":
			for temp in temps:
				humidity = find_match(temp, lines[1:])
				humidities.append(humidity)
				#print(humidity)
			#temp_to_humidity = parse_map(lines[1:])
		elif name == "humidity-to-location":
			for humidity in humidities:
				loc = find_match(humidity, lines[1:])
				locs.append(loc)
				#print(loc)
			#humidity_to_location = parse_map(lines[1:])

	"""
	# translate each seed to location by going through each map
	locs = []
	for seed in seeds:
		seed = int(seed)
		#print(seed)
		
		soil = seed_to_soil.get(seed, seed)
		fertilizer = soil_to_fertilizer.get(soil, soil)
		water = fertilizer_to_water.get(fertilizer, fertilizer)
		light = water_to_light.get(water, water)
		temp = light_to_temp.get(light, light)
		humidity = temp_to_humidity.get(temp, temp)
		location = humidity_to_location.get(humidity, humidity)
		
		locs.append(location)
		#print(f"seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temp}, humidity {humidity}, location {location}")
	"""
	print(min(locs))
	
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python part1.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)
