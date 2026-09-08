import sys

def find_state():
	if len(sys.argv) != 2:
		return

	capital_arg = sys.argv[1]

	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	target_abbrev = None
	for abbrev, capital in capital_cities.items():
		if capital == capital_arg:
			target_abbrev = abbrev
			break

	if target_abbrev is None:
		print("Unknown capital city")
		return

	for state, abbrev in states.items():
		if abbrev == target_abbrev:
			print(state)
			return
			
	print("Unknown capital city")

if __name__ == '__main__':
	find_state()