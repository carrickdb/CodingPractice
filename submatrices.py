class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        sums = {}
        """
        base case: size of matrix is 1x1
            return target == element in matrix
        totalTargets = 0
        for each of x1+1, y1+1, x2-1, y2-1:
            sum, numTargets = numSubmatrixSumTargetRec(smaller matrix)
            totalTargets += numTargets
            just once:
                sum + sum of the row or column that was left out to get total of original matrix
                totalTargets += large matrix total == target
        return sum of original matrix, totalTargets
        """
        def numSubmatrixSumTargetRec(i1, j1, i2, j2):
            tupCoords = tuple([i1, j1, i2, j2])
            if tupCoords in sums:
                return sums[tupCoords], 0
            if i2 == i1 and j2 == j1:
                currSum = matrix[i1][j1]
                sums[tupCoords] = currSum
                return currSum, int(currSum == target)
            origSum = None
            totalMatches = 0
            if i1 < i2:
                smallerSum, numMatches = numSubmatrixSumTargetRec(i1+1, j1, i2, j2)
                rowtup = tuple(i1, j1, i1, j2)
                origSum = smallerSum
                if rowtup in sums:
                    origSum += sums[rowtup]
                else:
                    rowsum = sum(matrix[i1][j1:j2+1])
                    origSum += rowsum
                    sums[rowtup] = rowsum
                    totalMatches += rowsum == target
                totalMatches += numMatches
                smallerSum, numMatches = numSubmatrixSumTargetRec(i1, j1, i2-1, j2)
                totalMatches += numMatches
            if j1 < j2:
                smallerSum, numMatches = numSubmatrixSumTargetRec(i1, j1+1, i2, j2)
                if not origSum:
                    origSum = smallerSum
                    for i in range(i2-i1+1):
                        origSum += matrix[i+i1][j1]
                totalMatches += numMatches
                smallerSum, numMatches = numSubmatrixSumTargetRec(i1, j1, i2, j2-1)
                totalMatches += numMatches

            sums[tupCoords] = origSum

            return origSum, totalMatches + (origSum == target)

        _, matches = numSubmatrixSumTargetRec(0, 0, len(matrix)-1, len(matrix[0])-1)
        return matches
