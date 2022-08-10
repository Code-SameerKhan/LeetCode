class Solution:
    def binarySearch(self,arr,target):
        
        left = 0
        right = len(arr)-1
        
        while left<= right:
            mid = (left+right)//2
            
            if arr[mid] == target:
                return [arr[mid],mid]
            elif target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        output = []
        for i in nums1:
            result = self.binarySearch(nums2,i)
            
            if not result == -1:
                output.append(result[0])
                nums2.pop(result[1])
        
        return output
