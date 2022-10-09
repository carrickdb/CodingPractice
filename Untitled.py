import json


class Node:
    def __init__(self, index, val):
        self.val = val
        self.index = index
        self.next = None
        self.setSize = 1

class Solution:

    def find(self, v):
        while v.next:
            v = v.next
        return v

    def fixPointers(self, a, bSet):
        while a.next != bSet:
            nextNode = a.next
            a.next = bSet
            a = nextNode

    def union(self, u, v):
        uSet = self.find(u)
        vSet = self.find(v)
        if uSet != vSet:
            if uSet.setSize > vSet.setSize:
                vSet.next = uSet
                uSet.setSize += vSet.setSize
                self.fixPointers(v, uSet)
            else:
                uSet.next = vSet
                vSet.setSize += uSet.setSize
                self.fixPointers(u, vSet)

    def gcdSort(self, nums):
        maxNum = max(nums)
        sieve = [-1 for _ in range(maxNum+1)]
        for i in range(2, len(sieve)//2):
            curr = i
            while curr <= maxNum:
                if sieve[curr] == -1:
                    sieve[curr] = i
                else:
                    break
                curr += i

        print("done with sieve")

        def getFactors(a):
            primes = set()
            while a > 1:
                primes.add(sieve[a])
                a //= sieve[a]
            return primes

        nodes = []
        for i in range(len(nums)):
            nodes.append(Node(i, nums[i]))
        for i in range(len(nums)):
            curr = nums[i]
            currprimes = getFactors(curr)
            self.union(nodes[i], nodes[j])

        print("done with sets")

        return True


with open("bullshit") as f:
    nums = json.load(f)
    sol = Solution()
    print(sol.gcdSort(nums))
