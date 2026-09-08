import sys

def find_capital():
	if len(sys.argv) != 2:
		return

	state_arg = sys.argv[1]

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

	if state_arg in states:
		state_abbrev = states[state_arg]
		capital = capital_cities[state_abbrev]
		print(capital)
	else:
		print("Unknown state")

if __name__ == '__main__':
	find_capital()