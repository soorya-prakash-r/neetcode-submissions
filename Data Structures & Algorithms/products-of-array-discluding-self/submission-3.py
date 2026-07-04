class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        def divide(x,y):
            # x/y
            if x == 0:
                return 0
            if y == 0:
                return x

            count = 0
            neg = (x < 0) ^ (y < 0)
            x = abs(x)
            y = abs(y)

            if x >= y:
                count = 1
            temp = y
            while (temp << 1) <= x:
                temp = temp << 1
                count  = count << 1
            
            x = x - temp
            
            if neg:
                return -(count + divide(x,y))
            else:
                return (count + divide(x,y))

        result = []
        z = 0
        multiply = 1
        for i in nums:
            if i != 0:
                multiply *= i
            else: 
                z += 1 

        for i in nums:
            if z!=0 and i!=0:
                result.append(divide(0,i))
            elif z >= 2 and i == 0:
                result.append(divide(0,i))
            else:
                result.append(divide(multiply,i))

        return result


            