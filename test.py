import LuhnCard

def valid():
	tests = [
		("0000000000000000", True),
		("4111111111111111", True),
		("5500000000000004", True),
		("6250941006528599", True),
		("5425233430109903", True),
		("6034883265619896", True),
		("4242424242424249", False),
	]

	for t in tests:
        	number,result = t
        	assert LuhnCard.CheckValidNumber(number)

