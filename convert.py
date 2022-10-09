def convert(s, numRows):
	if numRows == 1:
		return s
	l = ["" for i in range(len(s))]
	newIndex = 0
	for i in range(numRows):
		j = i
		if i == 0 or i == numRows-1:
			while j < len(s):
				l[newIndex] = s[j]
				j += numRows*2 - 2
				newIndex += 1
		else:
			diagonal = False
			while j < len(s):
				l[newIndex] = s[j]
				if diagonal:
					j += (i+1)*2 - 2
					diagonal = False
				else:
					j += (numRows - i)*2 - 2
					diagonal = True
				newIndex += 1

	return ''.join(l)

"""
     0   1   2   3   4   5   6   7  8  9  10 11 12 13
l = ["P","A","H","N","A","P","L","","","","","","",""]

i = 1
j = 5
newIndex = 6
     01234567890123
"""

s = "PAYPAL"

numRows = 2
print(convert(s, numRows))
