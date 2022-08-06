class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0 or target > nums[-1]:
             return [-1,-1]
        
        def leftRangeStart(nums,target):
            
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def rightRangeEnd(nums,target):
            
            left = 0
            right = len(nums)-1
            
            while left <= right:
                mid = (left+right)//2
                if target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left, right = leftRangeStart(nums, target), rightRangeEnd(nums, target)
        return (left, right) if left <= right else [-1, -1]
                
