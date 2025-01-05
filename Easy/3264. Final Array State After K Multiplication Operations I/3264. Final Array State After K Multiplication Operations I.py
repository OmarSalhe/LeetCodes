from typing import List
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if len(nums) <= 1:
            nums[0] *= multiplier ** k
            return nums

        for _ in range(k):
            i = 1
            min_index = 0
            while i < len(nums):
                if nums[i] < nums[min_index]:
                    min_index = i

                i += 1
            nums[min_index] *= multiplier
        
        return nums
