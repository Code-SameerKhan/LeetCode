class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        def coins(n):
            return (1+n)*n//2
        
        left = 1
        right = n
        
        
        while left <= right:
            mid = (left+right)//2
            n_coin = coins(mid)
            
            if n >= n_coin:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return right
