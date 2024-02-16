#Program returns either True of False based on whether the specified condition is met
#Condition: There exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
def increasingTriplet(nums):
    i=j=float('inf')
    for item in nums:
        if item <= i:
            i=item
            print(i)
        elif item <= j:
            j =item
            print(j)
        else:
            return True
    return False
        
    