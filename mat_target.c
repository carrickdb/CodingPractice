#include <stdlib.h>
#include <stdio.h>

int* runningSum(int* nums, int numsSize, int* returnSize) {
	*returnSize = numsSize;
	int* sums = (int*)malloc(numsSize*sizeof(int));
	int runningTotal = 0;
	for (int i = 0; i < numsSize; i++) {
		runningTotal += nums[i];
		sums[i] = runningTotal;
	}
	return sums;
}

int main() {
	int nums[] = {1, 7, 22, -1, -55};
	int numsSize = 5;
	int returnSize = 0;
	int* sums = runningSum(nums, numsSize, &returnSize);
	for (int i = 0; i < returnSize; i++) {
		printf("%d ", sums[i]);
	}
	printf("\n");
	free(sums);
	return 0;
}
