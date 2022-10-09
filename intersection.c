#include <stdlib.h>
#include <stdio.h>



int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
	/*
		create an array of buckets of size 1001
		tally up the number of times each number occurs in the first array
		go through the second array and tally # of times it occurs in second array and buckets
		decrement # in bucket
		find out how many numbers were in common, instantiate array with that size
		fill array with the numbers
	*/
	int buckets[1001] = {0};
	for (int i = 0; i < nums1Size; i++) {
		buckets[nums1[i]]++;
	}
	int intersection[1001] = {0};
	for (int i = 0; i < nums2Size; i++) {
		int currNum = nums2[i];
		if (buckets[currNum] > 0) {
			intersection[currNum]++;
			buckets[currNum]--;
		}
	}
	size_t intersection_size = 0;
	for (int i = 0; i < 1001; i++) {
		intersection_size += intersection[i];
	}
	*returnSize = intersection_size;
	int* output = (int*)calloc(intersection_size, sizeof(int*));
	uint32_t index = 0;
	for (int i = 0; i < 1001; i++) {
		uint32_t numRepeats = intersection[i];
		if (numRepeats > 0) {
			for (int j = 0; j < numRepeats; j++) {
				output[index] = i;
				index++;
			}
		}
	}
	return output;
}



int main() {
	int nums1[] = {4,1,1000};
	int nums2[] = {9,1,9,8,1000};
	// Output: [4,9]
	int nums1Size = 3;
	int nums2Size = 5;
	int returnSize = 0;
	int* output = intersect(nums1, nums1Size, nums2, nums2Size, &returnSize);
	for (int i = 0; i < returnSize; i++) {
		printf("%d, ", output[i]);
	}
	// Output: [2,2]
}
