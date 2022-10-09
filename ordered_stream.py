class OrderedStream:

    def __init__(self, n):
        self.buffer = [0 for i in range(n)]
        self.curr = 0

    def insert(self, idKey, value):
        """
        insert value at idKey
        if pointer is pointing at a spot that isn't 0:
            return the slice of the list from the current frame to the one before a frame containing 0
        increment pointer to space after returned portion of buffer
        """
        self.buffer[idKey-1] = value
        startSlice = self.curr
        while self.curr < len(self.buffer) and self.buffer[self.curr] != 0:
            self.curr += 1
        return self.buffer[startSlice:self.curr]

"""
          0        1        2        3  4
buffer = ["aaaaa", "bbbbb", "ccccc", 0, 0]
curr = 3
startSlice = 1

"""

inputs = [[3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]

stream = OrderedStream(5)
for idKey, val in inputs:
    print(stream.insert(idKey, val))
