#You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 




def findMaxAverage(self, nums, k):
    max_index = len(nums) - k
    max_average = 0 
    for i in range(max_index+1):
        to_sum = nums[i:i+4]
        print(to_sum)
        x = sum(to_sum)
        x = float(x)
        print(x)
        average = x / k
        print(average)
        max_average = max(average, max_average)
    return max_average