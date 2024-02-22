#Takes in a list nums and returns the list with all the 0's moved to the end 
def moveZeroes( nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))
    return nums
            