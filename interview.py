import unittest
from random import shuffle, randint


# n = 20000
# nums = [i for i in range(n)]
# random_num = randint(0, n - 1)
# print(random_num)
# nums.append(random_num)
# shuffle(nums)

def findDuplicates(L):
    hashmap = {}
    for num in L:
        if num in hashmap:
            return num
        else:
            hashmap[num] = 1
    return -1


def findDuplicates2(L):
    pass


class TestFindDuplicates(unittest.TestCase):
    def test_smallArray(self):
        L = [1, 4, 3, 2, 7, 9, 2, 8, 6, 5, 0]
        self.assertEqual(findDuplicates(L), 2)

    def test_mediumList(self):
        L = [7, 121, 11, 114, 130, 135, 109, 158, 88, 194, 80, 49, 26, 24, 132, 19, 179, 127, 66, 190, 195, 140, 59,
             164, 141, 173, 21, 75, 99, 176, 169, 160, 167, 142, 185, 193, 81, 15, 54, 58, 104, 183, 65, 107, 168, 10,
             86, 36, 192, 100, 166, 25, 53, 147, 39, 46, 100, 180, 48, 134, 125, 111, 27, 89, 124, 33, 139, 0, 83, 29,
             199, 170, 31, 91, 123, 22, 119, 51, 110, 63, 74, 182, 163, 118, 187, 198, 197, 92, 32, 43, 129, 191, 136,
             4, 116, 152, 126, 5, 17, 2, 77, 138, 103, 28, 8, 153, 151, 82, 40, 72, 34, 87, 96, 175, 122, 9, 93, 171,
             188, 67, 1, 131, 55, 145, 41, 79, 57, 78, 128, 13, 120, 38, 60, 76, 184, 23, 50, 12, 61, 181, 35, 14, 115,
             155, 156, 56, 105, 189, 146, 20, 45, 62, 112, 113, 97, 148, 117, 30, 186, 18, 16, 154, 37, 3, 69, 159, 178,
             47, 6, 84, 102, 68, 161, 90, 52, 98, 42, 106, 172, 73, 157, 108, 177, 165, 85, 162, 133, 196, 101, 137, 95,
             149, 174, 71, 143, 150, 44, 94, 70, 144, 64]
        self.assertEqual(findDuplicates(L), 100)


unittest.main(exit=False)


def bunnyTrain(n, t):
    if n % t == 0:
        return t
    return t - 1


def bunnyTrain2(n, t):
    pass


class TestBunnyTrain(unittest.TestCase):
    def test_bunnyTrain9(self):
        self.assertEqual(bunnyTrain2(9, 3), 3)

    def test_bunnyTrain10(self):
        self.assertEqual(bunnyTrain2(10, 3), 2)

    def test_bunnyTrainLarge(self):
        self.assertEqual(bunnyTrain2(234972938, 120), 119)

    def test_bunnyTrain1(self):
        self.assertEqual(bunnyTrain2(2321, 1), 1)

    def test_bunnyTrain1(self):
        self.assertEqual(bunnyTrain2(355992, 104), 104)

    def test_bunnyTrain1(self):
        self.assertEqual(bunnyTrain2(355922, 104), 103)

# print(bunnyTrain(355992, 104))
# unittest.main(exit=False)

