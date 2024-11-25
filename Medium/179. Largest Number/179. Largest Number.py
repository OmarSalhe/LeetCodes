from typing import List

class LargerNumKey(str):
    def __lt__(a,b):
        return a+b > b+a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        nums.sort(key=LargerNumKey)
        out = ''.join(nums)

        return '0' if out[0] == '0' else out
