class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        check = str(num)
        if int(check[-1]) in [2,3,7,8]:
            return False
        if num == 1:
            return True
        left = 0
        right = num

        while left <= right:
            mid = (left+right)//2
            if (mid * mid) == num:
                return True
                break
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid-1
        return False
