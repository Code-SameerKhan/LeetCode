class Solution:
    def binarySearch(self,arr):
        left = 0
        right = len(arr)-1
        count = 0
        
        while left <= right:
            mid = (left+right)//2
            
            if arr[mid] == 1:
                count = len(arr[:mid+1])
                left = mid + 1
            else:
                right = mid - 1
        return count
    
    
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[]
        finalAns=[]

        for i in range(len(mat)):
            ans.append((i, self.binarySearch(mat[i])))

        ans = sorted(ans, key=lambda value: value[1])

        for i in range (0, k):
            finalAns.append(ans[i][0])

        return finalAns
        
