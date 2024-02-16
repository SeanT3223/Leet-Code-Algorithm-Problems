
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