class Solution:
    def climbStairs(self, n: int) -> int:
        # only two ways to get to two: 1 + 1 or just 2
        if n <= 2:
            return n

        a, b = 1, 2
        # fibonnaci seq
        for i in range(1, n):
            a, b = b, a + b
        return a
