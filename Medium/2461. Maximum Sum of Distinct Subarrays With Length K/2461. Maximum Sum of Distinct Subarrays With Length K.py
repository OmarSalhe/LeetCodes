class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_win = 0 # maximum k-length subarray sum
        win_sum = 0 # current k-length subarray sum
        win_nums = collections.defaultdict(int) # numbers in cur k-length subarray

        n = len(nums)
        left, right = 0, 0

        while right < n: # expand right bound to end of array
            win_nums[nums[right]] += 1
            win_sum += nums[right]

            # contract window if any duplicates arise
            while left <= right and win_nums[nums[right]] > 1:
                # print(f'window: {nums[left: right + 1]}')
                win_sum -= nums[left]
                win_nums[nums[left]] -= 1
                left += 1
            
            if right - left + 1 == k: # if valid k-length window formed
                max_win = max(max_win, win_sum)

                # shift left bound forward
                win_nums[nums[left]] -= 1
                win_sum -= nums[left]

                left += 1

            # shift right bound forward
            right += 1
        
        return max_win
