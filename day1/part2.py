
import sys
import re

def convert_to_digits(raw):
	num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
	i = 0
	while i < len(raw):
		for key, value in num_dict.items():
			if raw[i:i + len(key)] == key:
				#print(key)
				before = raw[:i]
				after = raw[i:]
				#after = after.replace(key, value, 1)
				raw = before + value + after
				i = i + 1
				break
		i = i+1
	#processed_string = raw.replace("one", "1")
	#processed_string = raw.replace("two", "2")
	#processed_string = raw.replace("three", "3")
	#processed_string = raw.replace("four", "4")
	#processed_string = raw.replace("five", "5")
	#processed_string = raw.replace("six", "6")
	#proceseed_string = raw.replace("seven", "7")
	#processed_string = raw.replace("eight", "8")
	#processed_string = raw.replace("nine", "9")
	#return processed_string
	return raw

def regex_convert(file_path):
	with open(file_path, 'r') as file:
		pattern = re.compile("[0-9]|zero|one|two|three|four|five|six|seven|eight|nine")
		num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
		total = 0
		for line in file:
			digits = re.findall(pattern, line)
			if len(digits) > 0:
				first = digits[0]
				last = digits[len(digits)-1]
				if len(first) > 1:
					first = num_dict[first]
				if len(last) > 1:
					last = num_dict[last]
				curr = first + last
				print(curr)
				total += int(curr)
		print(total)
			 
	
def process_file(file_path):
	with open(file_path, 'r') as file:
		total = 0
		for line in file:
			print("raw: " + line)
			line = convert_to_digits(line)
			print("processed: " + line)
			foundFirst = False
			first = 0
			last = 0
			for i in line.strip():
				if i.isnumeric():
					if not foundFirst:
						first = i
						last = i
						foundFirst = True
					else:
						last = i
			curr = first + last
			print(curr)
			total += int(curr)
		print(total)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python your_script.py input.txt")
		sys.exit(1)

	input_file = sys.argv[1]
	process_file(input_file)
	#regex_convert(input_file)
