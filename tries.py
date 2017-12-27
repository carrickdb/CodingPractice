class Trie:

    def __init__(self):
        self.root = Node("")

    def addContact(self, contact):
        curr = self.root
        nodes = [self.root]
        for i in range(len(contact)):
            next = curr.inChildren(contact[i])
            if next:
                curr = next
            else:
                newChild = curr.addChild(contact[i])
                curr = newChild
            nodes.append(curr)
        for n in nodes:
            n.numPrefix += 1

    def count(self, prefix):
        curr = self.root
        numPrefix = self.root.numPrefix
        for i in len(prefix):
            child = curr.inChildren(prefix[i])
            if child:
                numPrefix = child.numPrefix
            else:
                return 0
            curr = child

    def print(self):
        print("Total number of contacts: ", self.root.numPrefix)
        stack = []
        for child in self.root.children:
            stack.append(child)
        while stack:
            curr = stack.pop()
            print(curr.val, curr.numPrefix)
            for child in curr.children:
                stack.append(child)


class Node:

    def __init__(self, val):
        self.children = []
        self.val = val
        self.numPrefix = 0

    def addChild(self, child):
        newChild = Node(child)
        self.children.append(newChild)
        return newChild

    def inChildren(self, val):
        for child in self.children:
            if child.val == val:
                return child
        return None

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    trie = Trie()
    if op == "add":
        trie.addWord(contact)
    elif op == "find":
        trie.count(contact)