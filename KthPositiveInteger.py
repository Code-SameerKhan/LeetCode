class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left+right)//2
            
            # Number of missing numbers that should ideally be in list
            missing =  arr[mid] - mid - 1 
            
            if k > missing: # we require to check more missing number
                left = mid + 1
            else:
                right = mid - 1 # we require less missing number
                
        return right + k + 1 # 
        
