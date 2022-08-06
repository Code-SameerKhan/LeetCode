class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x
        
        while left <= right:
            mid = (left + right)//2
            
            if x == mid*mid:
                return mid
            elif x > mid*mid:
                left = mid + 1
            else:
                right = mid - 1
        
        temp = []
        for i in range(x):
            if i*i < x:
                temp.append(i)
            else:
                break
        return temp[-1]
