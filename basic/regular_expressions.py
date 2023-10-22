import re

names = ['Parth Shah',
	'Bangalore',
	'Ahmedabad',
	'Sachin Tendulkar',
	'Virat Kohli',
	'Sourav Ganguly',
	'MS Dhoni',
    'Delhi 6',
    'Bond0000007']

def search_pattern(pattern, names):
    """ Function to search for different patterns in provided list of strings """
    print("=" * 40, end=" ")
    print(f"pattern = {pattern}", end=" ")
    print("="*40)
    for name in names:
        result = re.search(pattern, name)
        if result:
            print(name, result.span(), result.group())
    print("=" * 80, end="\n\n")        

search_pattern('\w+', names)
search_pattern('\w+ \w+', names)
search_pattern('\d', names)
search_pattern('0+', names)
search_pattern('.', names)


result = re.search('\d+\.\d+\.\d+\.\d+', '192.168.255.254') #TODO incorrect
print(result)
