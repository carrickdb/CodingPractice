def partition_array(nums):
    greatest_left = nums[0]
    greatest_right = -1
    left_size = -1
    for i in range(1, len(nums)):
        if greatest_left <= nums[i]:
            if left_size < 0:
                left_size = i
            if greatest_right <= nums[i]:
                greatest_right = nums[i]
        elif left_size > 0:
            left_size = -1
            greatest_left = greatest_right
    return left_size

"""

806166225460393


[1,1,1,0,6,12]

greatest_left = 2
greatest_right = 6
left_size = 5
nums = [7, 6, 8, 4, 2, 9, 12, 11]
nums = [7, 6, 7, 9, 12, 11]
iterate through array
    if largest_left is less than current number at i:
        if partition has been set:
            set greatest_right to this number
        else:
            partition = i
    else:
        if partition has been set:
            partition = -1
            greatest_left = greatest_right
        else:
            pass

hold on to greatest number x seen so far
when you see an even greater number at i, hold on to i
if you see a number less than x, set x to the even greater number
return i

naive: n^2
sort: out of order

sliding window?
"""
# nums = [7, 6, 8, 4, 2, 9, 9] # 5
nums = [7, 6, 7, 9, 12, 11] # 2
nums = [7, 6, 9, 12, 7, 15] # 2
nums = [1,1,1,0,6,12] # 4
nums = [5,0,3,8,6] # 3
nums = [1, 2]
nums = [1, 1]
print(partition_array(nums))
