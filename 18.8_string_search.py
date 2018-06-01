# Given a string s and an array of smaller strings T, design a method to search s for each small string in T.
# output? first index of each string

# naive solution: for each string t in T, check all of s for t.
# Complexity: For each string: Let m = len(t), n = len(s). (n-m)m
# rolling hash? for each unique string length m, put each string in s with length m into a dictionary
# value is starting index
# check hash for each string in T
# Complexity: Start-up cost: (num unique lengths)*(n-m)m. For each string: m
# savings only occurs if there are multiple strings of the same length
#
# make a trie of all the strings in T
# do DFS in the trie from each letter in s
# startup cost: sum of lengths of each string in T
# n^2
# can do one pass over the string but for each letter still may need to do operations on each level
#   --but some may disappear



class StringSearcher:

    def __init__(self, s):
        self.tree = {}
        curr = self.tree
        for i in range(len(s)):
            for j in range(i, len(s)):
                curr_letter = s[j]
                if curr_letter not in curr:
                   curr[curr_letter] = {}
                curr = curr[curr_letter]
            curr = self.tree

    def search(self, t):
        curr = self.tree
        for letter in t:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True



s = "Hello"
searcher = StringSearcher(s)
T = ["Hello", "ell", "lo", "cat"]
print(searcher.tree)
for t in T:
    print(searcher.search(t))