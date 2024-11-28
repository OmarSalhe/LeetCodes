from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return

        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0 and j < i: # if non-zero num found
                 nums[j] = nums[i]
                 nums[i] = 0
                 j += 1
            if nums[j] != 0: # shift j onto a non-zero element
                j += 1
            i += 1
            
        
