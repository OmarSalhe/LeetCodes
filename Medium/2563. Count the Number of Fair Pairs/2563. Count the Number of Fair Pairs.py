class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # upper bound
        def find_right(left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        # lower bound
        def find_left(left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            
            return left
    
        nums.sort()
        n = len(nums)
        pairs = 0

        for i in range(n - 1):
            # binary search min nums that stay within range
            left = find_left(i + 1, n, lower - nums[i])
            right = find_right(i + 1, n, upper - nums[i])

            pairs += right - left
        
        return pairs
        

    # TC = O(nlogn), both sorting and searching
    # SC = O(1), glorified two pointer problem
