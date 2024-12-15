from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        prefix = [0] * (n + 1)
        prefix[0] = 0

        for i in range(n):
            prefix[i + 1] = gain[i] + prefix[i]


        return max(prefix)
