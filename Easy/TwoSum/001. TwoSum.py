class Solution(object): 
    def twoSum(self, nums, target):
        hm = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if hm.get(complement) != None:
                return i, hm[complement]
            hm[nums[i]] = i