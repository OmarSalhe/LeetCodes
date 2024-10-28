class Solution:
    def reverse(self, x: int) -> int:
        num, y = 0, abs(x)
        while(y > 0):
            num *= 10
            num += y % 10
            y //= 10
        if num > 2**31 - 1:
            return 0
        return num if x >= 1 else -num
