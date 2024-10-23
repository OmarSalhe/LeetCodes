from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, sub=[]):
            if i == len(nums):
                res.append(sub[:])
                return
            # add
            sub.append(nums[i])
            helper(i+1, sub)
            # remove
            sub.pop()
            helper(i+1, sub)
        helper(0)
        return res
"""
            [1,2,3]
           /   |   \
      [2,3]  [1,3]  [1,2]
      /  \    / \     / \
    [2]  [3] [1] [3] [1] [2]
               |
               |
               v
               []

makes more sense, if you go from bottom-up, but becomes more intuitive if you recognize tree struct              
"""