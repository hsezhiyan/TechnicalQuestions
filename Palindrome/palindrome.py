def return_with_no_spaces(input_string):
	new_string = ''
	for c in input_string:
		if c != ' ':
			new_string += c
	return(new_string)

def is_palindrome(input_string):
	string_len = len(input_string)
	for i in range(string_len):
		# print(i)
		if input_string[i].lower() != input_string[string_len-i-1].lower():
			return False
	return True

def longest_palindrome(input):
    max_size = 0
    max_palindrome = ''
    string_len = len(input) 
    for size in range(2, string_len + 1):
    	for starting_point in range(string_len - size + 1):
    		end_point = starting_point + size
    		sliced_string = input[starting_point:end_point+1]
    		if is_palindrome(return_with_no_spaces(sliced_string)) and size > max_size:
    			max_palindrome = sliced_string
    			max_size = size

    return max_palindrome
