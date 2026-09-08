def print_numbers():
	with open("numbers.txt", "r") as f:
		content = f.read()

		numbers = content.split(",")
		for num in numbers:
			print(num.strip())

if __name__ == '__main__':
    print_numbers()