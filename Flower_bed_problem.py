# program returns whether or not n flowers can be placed in a flower bed where no two flowers can be placed next to one other
#flowerbed is a list representation of 1's and 0's where a 1 represents a flower and 0 represents empty 
def canPlaceFlowers(flowerbed, n):
    numA = 0 
    for i in range(len(flowerbed)):
        print(i)
        #beginning case 
        if i == 0 :
            if flowerbed[i+1] == 0 and flowerbed[0] == 0:
                numA += 1
                flowerbed[i] = 1 
                print(numA)
                print(flowerbed)
        #end case
        elif i == len(flowerbed)-1:
            if flowerbed[i-1] == 0 and flowerbed[i]== 0: 
                numA += 1
                flowerbed[i] = 1 
                print(numA)
                print(flowerbed)
        #Everything else
        elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0 :
                numA += 1
                flowerbed[i] = 1  
    print(i)
    if numA >= n:
        return True
    else:
        return False