class Node:

    def __init__(self, val, index=None):
        self.val = val
        self.indices = []
        if index != None:
            self.indices.append(index)
        self.children = {}

def findAncestors(changedPaths):
    root = None
    for i in range(len(changedPaths)):
        currPath = changedPaths[i]
        if currPath == '/':
            if root == None:
                root = Node('/', i)
            else:
                root.indices.append(i)
        elif root == None:
            root = Node('/')
        fileList = currPath.split('/')
        currNode = root
        for j in range(len(fileList)):
            currFile = fileList[j]
            if currFile == "":
                continue
            if currFile in currNode.children:
                currNode = currNode.children[currFile]
                if j == len(fileList) - 1:
                    currNode.indices.append(i)
            else:
                index = None
                if j == len(fileList)-1:
                    index = i
                currNode.children[currFile] = Node(currFile, index)
                currNode = currNode.children[currFile]
    ancestorDescendants = []
    for child, _ in root.children.items():
        print(child, end=' ')
    print()
    exit()
    for i in range(len(changedPaths)):
        currPath = changedPaths[i]
        if currPath == "/":
            continue
        fileList = currPath.split('/')
        currNode = root
        for j in range(len(fileList)):
            currFile = fileList[j]
            if currFile == "":
                continue
            for index in currNode.indices:
                ancestorDescendants.append((index, i))
            if currFile not in currNode.children:
                print("something went wrong")
                exit()
            currNode = currNode.children[currFile]
    return ancestorDescendants

print(findAncestors(['/foo/', '/bar', '/foo/bar/baz']))



"""
[/, [a, [[b, None], [c, None], [d, None]]], [h, None]]


first idea:

create tree of files (include numbers of duplicates)

for each file, traverse the tree and add the tuple to the list
(each level is sorted)

space: O(n)
time:
O(nlogn)


totally naive version:
for each file, traverse the entire list and check (also O(n^2))

wild idea:
sort the list (recursively for each level of files) O(nlogn)
do binary search O(nlogn)

[a, b, c, d, e, f, g]
[n, m, r]

/a/b/c/d/e/f/g => [/, a, b, c, d, e, f, g]
/a/b/c/d/e/f/g/h
/a/b/c/d/e/f/g/h
/a/b/c/d/e/f/g/h
/a/b/c/d/e/f/g/h
/a/b/c/d/e/f/g/h
/a/b/c/d/e/f/g/h
/a/b/c/d/e/f/g/h

/a/b
/a/c
/a/d
/h/

[/, [a, [[b, None], [c, None], [d, None]]], [h, None]]


"""
