

book = ['the', 'cat', 'jumped', 'off', 'the', 'table']
dict = {}

def processBook(book):
	for word in book:
		if word in dict:
			dict[word] += 1
		else:
			dict[word] = 1

def getFrequency(searchWord):
	if searchWord in book:
		return dict[searchWord]
	else:
		return "Not found"
		
processBook(book)
print getFrequency('the')
print getFrequency('dog')