#!/bin/python3

import sys
from math import factorial

metadata = {}
answers = {}
string = ""

class Metadata:
    def __init__(self, pairs, buckets):
        self.pairs = pairs
        self.buckets = buckets

def print_metadata():
    global metadata
    for k, v in metadata.items():
        print(k, end='')
        print(": ", end='')
        print(v.buckets)

def initialize(s):
    # This function is called once before all queries.
    global string
    global metadata
    string = s
    strlen = len(string)
    buckets = [0 for i in range(26)]
    pairs = 0
    # for i in range(3):
    #     char = ord(string[i]) - ord('a')
    #     buckets[char] += 1
    #     if buckets[char] % 2 == 0:
    #         pairs += 1
    # metadata[(0, 2)] = Metadata(pairs, buckets[:])
    # print(str(0) + ", " + str(2) + ": ", end="")
    # print(buckets)
    # for i in range(1, strlen - 2):
    #     char = ord(string[i - 1]) - ord('a')
    #     buckets[char] -= 1
    #     if buckets[char] % 2 == 1:
    #         pairs -= 1
    #     char = ord(string[i + 2]) - ord('a')
    #     buckets[char] += 1
    #     if buckets[char] % 2 == 0:
    #         pairs += 1
    #     metadata[(i, i + 2)] = Metadata(pairs, buckets[:])
    for span in range(1, strlen):
        if (0, span - 1) in metadata:
            buckets = metadata[(0, span - 1)].buckets[:]
        else:
            bucket = [0 for i in range(26)]
        char = ord(string[span]) - ord('a')
        buckets[char] += 1
        if buckets[char] % 2 == 0:
            pairs += 1
        metadata[(0, span)] = Metadata(pairs, buckets[:])
        for i in range(1, strlen - span):
            char = ord(string[i - 1]) - ord('a')
            buckets[char] -= 1
            if buckets[char] % 2 == 1:
                pairs -= 1
            char = ord(string[i + span]) - ord('a')
            buckets[char] += 1
            if buckets[char] % 2 == 0:
                pairs += 1
            # print(str(i) + ", " + str(i + span) + ": ", end="")
            # print(buckets)
            metadata[(i, i + span)] = Metadata(pairs, buckets[:])
    print_metadata()

def answerQuery(L, R):
    # Return the answer for this query modulo 1000000007.
    global answers
    global metadata
    global string
    if L < 0 or L > len(string) or R < 0 or R > len(string) or L >= R:
        return None
    if (L, R) in answers:
        return answers[(L, R)]
    data = metadata[(L, R)]
    if data.pairs == 0:
        return 1
    permutations = factorial(data.pairs)
    num_odds = 0
    for count in data.buckets:
        if count != 0:
            permutations //= factorial(count // 2)
        if count % 2 != 0:
            num_odds += 1
    answer = (permutations + max(0, num_odds - 1)) % 1000000007
    answers[(L, R)] = answer
    return answer


if __name__ == "__main__":
    #s = input().strip()
    s = "abaaba"
    initialize(s)
    #q = int(input().strip())
    #for a0 in range(q):
    result = answerQuery(1, 5)
    print(result)
