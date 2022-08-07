class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()
        
        if len(nums) < nums[0]:
            return len(nums)
        
        left = 0
        right = len(nums)
        
        while left <= right:
            mid = (left+right)//2
            
            count = 0
            for i in range(len(nums)):
                if nums[i] >= mid:
                    count += 1
            
            if count == mid:
                return count
            
            elif mid > count:
                right = mid - 1
            else:
                left = mid + 1
        return - 1
                
