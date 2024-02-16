#Program takes in a list nums and returns a list where each position is associated with the product of every numver in the original array besides that position multiplied together

def productExceptSelf(nums):
    output = []
    for i in range(len(nums)):
        x = nums[i]
        del nums[i]
        product = 1
        for item in nums:
            product *= item
        output.append(product)
        nums.insert(i, x)
    return output