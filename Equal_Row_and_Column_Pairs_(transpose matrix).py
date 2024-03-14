def equalPairs(grid):
    temp_list1 = []
    for i in range(len(grid)):
        temp_list2 = []
        for j in range(len(grid[i])):
            temp_list2.append(grid[j][i])
        temp_list1.append(temp_list2)
    print(temp_list1) 
    count = 0 
    for k in range(len(grid)):
        if grid[k] in temp_list1:
            count += 1 
    return count 
            