from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual = sum(nums)
        expected = len(nums)*(len(nums) + 1)//2

        return expected - actual
