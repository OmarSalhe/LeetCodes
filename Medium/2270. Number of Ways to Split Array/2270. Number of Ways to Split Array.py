'''
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
    - n - i - 1 = (n - 1) - i = remaining elements
    - i + 1 -> shifting to 1-index -> includes ith element
    - the sum of the first x elements must be >= to the sum of the last x - 1 elements
There is at least one element to the right of i. That is, 0 <= i < n - 1.
    - part cannot be made at the end of arr or at the start -> splits are non-empty

Return the number of valid splits in nums.

return the number of times the sum of the first i + 1 elements >= the remaining elements

*only one split per iteration -> only splitting into two*

i = 0, len(nums) - 1 always fails
len(nums) = big -> O(n) needed

slowest part = finding sum for every range -> need to find sum at every index first (prefix sum)

nums = [10,4,-8,7]
Decision:
    x = 1
    left = 10, right = 4 - 8 + 7 = 5 -> valid
    x = 2
    left = 10 + 4 = right = -8 + 7 = -1 -> valid
    x = 3
    left = 10 + 4 - 8 = 6, right = 7 -> invalid

Generalized:
    for x in [1, len(nums) - 2]:
        if prefix[x] >= prefix[n - 1] - prefix[x]:
            valid part formed
'''
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] += prefix[i - 1] + nums[i - 1]
        
        valid_part = 0
        for i in range(1, n):
            if prefix[i] >= prefix[n] - prefix[i]:
                valid_part += 1
        
        return valid_part
