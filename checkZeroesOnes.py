def checkZeroOnes(s):
	in_zeroes = True
	longest_zeroes = 0
	longest_ones = 0
	current_zeroes = 0
	current_ones = 0
	for char in s:
		if in_zeroes:
			if char == "0":
				current_zeroes += 1
			elif char == "1":
				longest_zeroes = max(current_zeroes, longest_zeroes)
				in_zeroes = False
				current_zeroes = 0
				current_ones = 1
		else:
			if char == "1":
				current_ones += 1
			elif char == "0":
				longest_ones = max(current_ones, longest_ones)
				in_zeroes = True
				current_ones = 0
				current_zeroes = 1
	if in_zeroes:
		longest_zeroes = max(current_zeroes, longest_zeroes)
	else:
		longest_ones = max(current_ones, longest_ones)
	return longest_ones > longest_zeroes

s = "0" # false
s = "1" # true
s = "01" # false
s = "100" # false
s = "011" # true
s = "111100010" # true
print(checkZeroOnes(s))
