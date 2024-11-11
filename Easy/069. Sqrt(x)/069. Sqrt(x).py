class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        start, end = 1, x
        while start <= end:
            mid = (start + end) // 2
            check = x // mid
            if check == mid:
                return mid
            elif check < mid:
                end = mid - 1
            else:
                start = mid + 1
        return end        