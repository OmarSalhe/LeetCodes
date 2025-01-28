class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, 0
        n = len(nums)

        window_len = -1
        while right < n:
            right += 1
            window_len = max(window_len, right - left)
            while right < n and left < right and nums[left] + k < nums[right] - k:
                left += 1
            
        return max(window_len, right - left)

        # TC = O(nlogn) -> sorting
        # SC = O(n) -> sorting
