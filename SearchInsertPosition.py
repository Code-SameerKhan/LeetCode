class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[-1]:
                return 0
            elif target > nums[-1]:
                return 1
            else:
                return 0
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid - 1
            
        if target < nums[-1]:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
        else:
            return len(nums)
