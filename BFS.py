class Graph():
    def __init__(self, n):
        self.numNodes = n
        self.edges = {}
        self.distances = [-1 for i in range(n)]
        self.added = [0 for i in range(n)]

    def addEdge(self, fr, to):
        if fr not in self.edges:
            self.edges[fr] = [to]
        else:
            self.edges[fr].append(to)

    def connect(self, node1, node2):
        self.addEdge(node1, node2)
        self.addEdge(node2, node1)

    def find_all_distances(self, start):
        queue = [start]
        self.distances[start] = 0
        self.added[start] = 1
        while queue:
            curr = queue[0]
            del queue[0]
            if curr not in self.edges:
                break
            currNeighbors = self.edges[curr]
            for neighbor in currNeighbors:
                if not self.added[neighbor]:
                    queue.append(neighbor)
                    self.distances[neighbor] = self.distances[curr] + 6
                    self.added[neighbor] = 1
        for i in range(self.numNodes):
            if i != start:
                print(self.distances[i], end=' ')
        print()


with open('BFS testcase.txt', 'r') as f:
    t = int(f.readline())
    for i in range(t):
        n, m = [int(value) for value in f.readline().split()]
        graph = Graph(n)
        for i in range(m):
            x, y = [int(x) for x in f.readline().split()]
            graph.connect(x - 1, y - 1)
        s = int(f.readline())
        graph.find_all_distances(s - 1)

