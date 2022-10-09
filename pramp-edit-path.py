from collections import deque

def shortestWordEditPath(source, target, words):
  queue = deque([source])
  pathlen = -1
  visited = set([source])
  wordMap = {}
  for word in [source] + words:
    for i in range(len(word)):
      newString = word[:i] + "*" + word[i+1:]
      wordMap[newString] = []
  for word in words:
    for i in range(len(word)):
      newString = word[:i] + "*" + word[i+1:]
      if newString in wordMap:
        wordMap[newString].append(word)
  # print(wordMap)
  while queue:
    pathlen += 1
    for i in range(len(queue)):
      curr = queue.popleft()
      if curr == target:
        return pathlen
      for j in range(len(curr)):
        newString = curr[:j] + "*" + curr[j+1:]
        if newString not in wordMap:
          continue
        edges = wordMap[newString]
        for edge in edges:
          if edge not in visited:
            queue.append(edge)
            visited.add(edge)
  return -1


# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.visited = False
#         self.edges = []
#
# def shortestWordEditPath(source, target, words):
#     if target not in words:
#         return -1
#     if source not in words:
#         allWords = words + [source]
#     else:
#         allWords = words
#     graph = {}
#     for word in allWords:
#         graph[word] = Node(word)
#     for word in allWords:
#         for word2 in allWords:
#             if len(word) != len(word2):
#                 continue
#             numDiffs = 0
#             for i in range(len(word)):
#                 if word[i] != word2[i]:
#                     numDiffs += 1
#                     if numDiffs > 1:
#                         break
#             if numDiffs == 1:
#                 graph[word].edges.append(graph[word2])
#     for _, node in graph.items():
#         print(node.val, end=': ')
#         for edge in node.edges:
#             print(edge.val, end=' ')
#         print()
#     queue = deque([graph[source]])
#     pathlen = -1
#     while queue:
#         pathlen += 1
#         for i in range(len(queue)):
#             curr = queue.popleft()
#             if curr.val == target:
#                 return pathlen
#             if not curr.visited:
#                 for edge in curr.edges:
#                     if not edge.visited:
#                         queue.append(edge)
#                 curr.visited = True
#     return -1
#
# print(shortestWordEditPath("abc", "ab", ["abc","ab"]))


# from collections import deque
#
# class Node:
#
#   def __init__(self, val, edges):
#     self.val = val
#     self.edges = edges
#
# def shortestWordEditPath(source, target, words):
#   graph = {}
#   allWords = words + [source] + [target]
#   for word1 in allWords:
#     edges = []
#     for word2 in allWords:
#       if len(word1) != len(word2):
#         continue
#       numDifferent = 0
#       for i in range(len(word1)):
#         if word1[i] != word2[i]:
#           numDifferent += 1
#       if numDifferent == 1:
#         if word2 in graph:
#           otherNode = graph[word1]
#         else:
#           otherNode = Node(word2, [])
#         edges.append(otherNode)
#         graph[word2] = otherNode
#       if word1 in graph:
#         graph[word1].edges.append(edges)
#       else:
#         graph[word1] = Node(word1, edges)
#   print(graph)
# #  visited = set()
# #  queue = deque()
# #  queue.append(graph[source])
# #  while queue:
# #    curr = queue.popleft()
# #    if curr in visited:
#
#
#
# # ["bit", "but", "put"]
# # "bit", ["but"]
# # "but",
# shortestWordEditPath("bit", "dog", ["but", "put"])
#
#
#
# # *ut
# # b*t: [bit, but]    ,
# # bu*: []
# #
# # def shortestWordEditPath(source, target, words):
# #   steps = 0
# #   trans_dict = {}
# #   #bit *it
# #   for w in words:
# #     for i in range(len(w)):
# #       _w = w[:i]+'*'+w[i+1:]
# #       #print(_w)
# #       if _w not in trans_dict:
# #         trans_dict[_w]=[]
# #       trans_dict[_w].append(w)
# #   #print(trans_dict)
# #
# #   q = []
# #   #source
# #   q.append(source)
# #   chosen_set = set()
# #   chosen_set.add(source)
# #   while q:
# #     q_next = []
# #     for each_q in q: #bit
# #       #each_q == target
# #       if each_q == target:
# #         return steps
# #       for i in range(len(each_q)):
# #         #_w = each_q
# #         #_w[i] = '*'
# #         _w = each_q[:i]+'*'+each_q[i+1:]
# #         # b*t
# #         if _w in trans_dict:
# #           for candidate in trans_dict[_w]:
# #             if candidate not in chosen_set:
# #               q_next.append(candidate)
# #               chosen_set.add(candidate)
# #     steps += 1
# #     q = q_next
# #   #source == target
# #
# #
# #   return -1
