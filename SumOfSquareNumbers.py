class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(c**0.5)
        left = 0
        right = n

        while left <= right:
            target = (left**2)+(right**2)
            if target == c:
                return True
            elif c > target:
                left += 1
            else:
                right -= 1
        return False
