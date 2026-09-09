import sys

def all_in():
	if len(sys.argv) != 2:
		return

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

	state_lookup = {}
	capital_lookup = {}
	
	for state, abbrev in states.items():
		capital = capital_cities[abbrev]

		state_key = " ".join(state.split()).lower()
		capital_key = " ".join(capital.split()).lower()
		
		state_lookup[state_key] = (state, capital)
		capital_lookup[capital_key] = (state, capital)

	expressions = sys.argv[1].split(',')
	
	for expr in expressions:
		stripped_expr = expr.strip()
		
		if not stripped_expr:
			continue
			
		search_key = " ".join(stripped_expr.split()).lower()
		
		if search_key in state_lookup:
			orig_state, orig_cap = state_lookup[search_key]
			print(f"{orig_cap} is the capital of {orig_state}")
		elif search_key in capital_lookup:
			orig_state, orig_cap = capital_lookup[search_key]
			print(f"{orig_cap} is the capital of {orig_state}")
		else:
			print(f"{stripped_expr} is neither a capital city nor a state")

if __name__ == '__main__':
	all_in()