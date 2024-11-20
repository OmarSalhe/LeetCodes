from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1: return False

        """
        Approach: save the index of all numbers encountered. If a dup 
        is found check if they're k apart from the og. If they are -> T,
        else -> update recent location
        """
        hm = {nums[0]:0}
        for i in range(1, len(nums)):
            if nums[i] in hm and abs(hm[nums[i]] - i) <= k:
                return True
            
            hm[nums[i]] = i

        return False
