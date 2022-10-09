def productExceptSelf(nums):
	zero_count = nums.count(0)
	num_length = range(len(nums))
	if zero_count > 1:
		return [0 for i in num_length]
	if zero_count == 1:
		total = 1
		for i in num_length:
			if nums[i] != 0:
				total *= nums[i]
		output = [0 for i in num_length]
		output[nums.index(0)] = total
		return output

	return output

print(productExceptSelf([0, 5, 4]))
