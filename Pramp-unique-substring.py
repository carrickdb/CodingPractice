def get_shortest_unique_substring(arr, s):
  start = 0
  counts = {}
  minStart = -1
  minEnd = -1
  for char in arr:
    counts[char] = 0
  numUnique = 0
  for i in range(len(s)):
    curr = s[i]
    if curr in arr:
      counts[curr] += 1
      if counts[curr] == 1:
        numUnique += 1
      if numUnique == len(arr):
        if minEnd == -1 or minEnd - minStart > i-start:
          minStart = start
          minEnd = i
        while start < i:
          curr = s[start]
          if curr in arr:
            counts[curr] -= 1
            if counts[curr] == 0:
              numUnique -= 1
              if minEnd == -1 or minEnd - minStart > i-start:
                minStart = start
                minEnd = i
              break
          start += 1
  return s[minStart:minEnd+1]

print(get_shortest_unique_substring(['x','y','z'], "xjhffmdmz"))

"""
set = {x: 1, y: 1, z: 1}
minCount = 4
xyyyzzyyx
['x','y','z'], "xyyzyzyx"
"""
