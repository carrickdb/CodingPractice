def groupAnagrams(strs):
    strToList = {}
    for s in strs:
        buckets = [0 for i in range(26)]
        for char in s:
            buckets[ord(char) - ord('a')] += 1
        alphabetizedList = []
        for i in range(len(buckets)):
            alphabetizedList += [chr(i + ord('a')) for j in range(buckets[i])]
        s_alphabetized = ''.join(alphabetizedList)
        if s_alphabetized not in strToList:
            strToList[s_alphabetized] = [s]
        else:
            strToList[s_alphabetized].append(s)
    ret = []
    for _, strList in strToList.items():
        ret.append(strList)
    return ret

"""
strToList["ab"] = ["ab", "ba"]
"""



strs = [""]
# strs = ["a"]
strs = ["ab", "ba"]
strs = ["ab", "cb"]
strs = ["aab", "ab"]
print(groupAnagrams(strs))

"""
alphabetize the letters in each word
hash the alphabetized word
map tuples to strings pertaining to that tuple
time: O(nlogn)
space: O(n)

for each string:
    create a set with the letters in the string

strs = ["eat","tea","tan","ate","nat","bat"]

set("e", "a", "t")

set("t", "e", "a")


alphabetize the letters
create a trie
at the end of each sequence, have a pointer to a list

"""
