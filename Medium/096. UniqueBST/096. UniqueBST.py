class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        res = 0
        # Finds Catalan Seq
        for i in range(1, n):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]

        # Calculates Cn
        for i in range(n):
            res += dp[i] * dp[n-i-1]

        return res