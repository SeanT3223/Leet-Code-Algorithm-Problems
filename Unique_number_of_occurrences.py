#Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

#USING HASHMAP


def uniqueOccurrences(arr):
    hashmap = dict()
    count = 0 
    for item in arr: 
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1
    print(hashmap)

    occurrences = []
    for key, value in hashmap.items():
        occurrences.append(value)
    print(occurrences)

    counter = 0
    for i in occurrences:
        
        if occurrences.count(i)>1:
            return False
    return True