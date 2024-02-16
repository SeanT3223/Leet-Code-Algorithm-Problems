class Solution(object):
    def findGCD(self, nums):
        greatest = 0
        least = 1000
        for num in nums: 
            if num > greatest:
                greatest = num
            if num < least:
                least = num
        if greatest % least == 0:
            GCD = least
            return  GCD
        else:
            prod = greatest*least
            mleast = []
            mgreatest = []
            
            for count1 in range(1, 10000):
                mleast.append(count1*least)

            for count2 in range(1, 10000):
                mgreatest.append(count2*greatest)
                
            for i in range(len(mgreatest)):
                if mgreatest[i] in mleast:
                    LCM = mgreatest[i]
                    break

            GCD = prod/LCM
            return GCD

            

                

            
            


               
        
            
        


            GCD = prod/LCM