def line_break() -> None:
		print(" "  * 20)
		print("-*" * 20)
		print(" "  * 20)


def is_valid_parentheses(input_string: str) -> bool:
		stack = []
		stack_len = 0
		brackets_dict = { "(": ")", "{": "}", "[": "]" }

		## check if first item is an opening bracket or last is closing bracket
		if not brackets_dict.get(input_string[0]) or not input_string[len(input_string) - 1] in brackets_dict.values(): 
				return False

		## implemenation O(n), go through the list 
		for  val in input_string:
				if brackets_dict.get(val):
						## it exists and is an opening bracket 
						## add to the stack
						stack.append(val)
						stack_len += 1
				else:
						# it is a closing bracket then (or some random other char)
						if stack_len == 0:
								# if stack is empty AND its a closing bracket FALSE
								return False
						else:
								# we have open brackets in the stack, match them 
								if brackets_dict.get(stack[stack_len - 1]) == val:
										## remove from stack, update size of stack
										stack.pop()
										stack_len -= 1
								else:
										## mismatching bracket or 'junk' char
										return False
		return True if stack_len == 0 else False


valid_first = '{}'
valid_second = '{}()[]'
valid_third = '(({}[]))'

invalid_first = ']{}()]'
invalid_second = '(){}[[]'
invalid_third = '(({]}))'

print ("An Example of first valid input: ")
print ("Input is: " + valid_first)
print(is_valid_parentheses(valid_first))
line_break()

print ("An Example of second valid input: ")
print ("Input is: " + valid_second)
print(is_valid_parentheses(valid_second))
line_break()

print ("An Example of third valid input: ")
print ("Input is: " + valid_third)
print(is_valid_parentheses(valid_third))
line_break()

print ("An Example of first invalid input: ")
print ("Input is: " + invalid_first)
print(is_valid_parentheses(invalid_first))
line_break()

print ("An Example of second invalid input: ")
print ("Input is: " + invalid_second)
print(is_valid_parentheses(invalid_second))
line_break()

print ("An Example of third invalid input: ")
print ("Input is: " + invalid_third)
print(is_valid_parentheses(invalid_third))
line_break()

