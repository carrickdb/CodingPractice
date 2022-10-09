class Solution:

  def sortArray(nums):
      if len(nums) < 2:
          return nums
      left = self.sortArray(nums[:len(nums)//2])
      right = self.sortArray(nums[len(nums)//2:])
      currL = 0
      currR = len(nums)//2
      newNums = [0 for i in range(len(nums))]
      for i in range(len(nums)):
          if currR < len(right) and (currL >= len(left) or right[currR] < left[currL]):
              newNums[i] = right[currR]
              currR += 1
          else:
              newNums[i] = left[currL]
              currL += 1
      return nums


print(sortArray([5, 6]))
