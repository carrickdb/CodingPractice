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

# how to know which index is the starting index?
# each node will have a list at which its substring started
# l: [2, 3]
# l: [2]    o: [3]
# ll: starts at 2; o: lo starts at o


class Node:

    def __init__(self, index):
        self.index = index
        self.children = {}


class StringSearcher:

    def __init__(self, s):
        self.tree = Node(None)
        curr = self.tree
        for i in range(len(s)):
            for j in range(i, len(s)):
                curr_letter = s[j]
                if curr_letter not in curr.children:
                    new_node = Node(i)
                    curr.children[curr_letter] = new_node
                curr = curr.children[curr_letter]
            curr = self.tree

    def search(self, t):
        if t == "":
            return -1
        curr = self.tree
        for i in range(len(t)):
            letter = t[i]
            if letter not in curr.children:
                return -1
            curr = curr.children[letter]
        return curr.index



s = "bibs"
searcher = StringSearcher(s)
T = ["b", "bi", "ib", "bib", "bibs", "sib", "s", "is", "ibs"]
for t in T:
    print(searcher.search(t))