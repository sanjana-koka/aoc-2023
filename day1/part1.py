
import sys

def process_file(file_path):
	with open(file_path, 'r') as file:
		total = 0
		for line in file:
			foundFirst = False
			first = 0
			last = 0
			for i in line.strip():
				if i.isdigit():
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
