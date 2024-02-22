#You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.


def maxOperations(nums, k):
    nums.sort()
    b = 0 
    e = len(nums)-1
    output = 0
    while b < e:
        ksum = nums[b] + nums[e] 
        if ksum == k:
            b += 1
            e -= 1
            output += 1
        elif ksum < k:
            b+=1
        else:
            e -= 1
    return output