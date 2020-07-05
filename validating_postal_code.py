regex_integer_in_range = r"_________"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.
# Option 1
# regex_integer_in_range = r'^[1-9][\d]{5}$'
# regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'

# Option 2
# regex_integer_in_range = r'^[1-9]\d{5}$'
# regex_alternating_repetitive_digit_pair = r'(.)(?=.\1)'

# # Option 3
regex_integer_in_range = r'\d{6}(?!\d)'
regex_alternating_repetitive_digit_pair = r'(.)(?=.\1)'

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)