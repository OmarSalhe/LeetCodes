from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = [False] * max(nums)

        for i in range(len(nums)):
            if num[nums[i]-1]:
                return nums[i]
            num[nums[i]-1] = True

        return -1






