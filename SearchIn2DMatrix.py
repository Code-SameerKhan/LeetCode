class Solution:
    
    def binarySearch(self,arr,target):
        left = 0
        right = len(arr)-1
        
        while left <= right:
            mid = (left+right)//2
            
            if arr[mid] == target:
                return 1
            
            elif target > arr[mid]:
                left = mid + 1
            
            else:
                right = mid - 1
        return 0
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        counter = []
        for li in matrix:
            counter.append(self.binarySearch(li,target))
        
        return max(counter)
