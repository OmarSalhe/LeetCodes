class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        have two pointers: one to keep track of non-val values and one to go through list
        for each num in list
            shift all non-val's to start of list

            if non-val:
                set first pointer val to non-val
                shift pointer

        TC = O(N) -> iterate through
        SC = O(1) -> only uses two pointer variables
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i