import heapq
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix_heap = []
        cur_sum = 0
        min_sub = float('inf')

        for i in range(n):
            cur_sum += nums[i]

            if cur_sum >= k:
                min_sub = min(min_sub, i + 1)
            
            while prefix_heap and cur_sum - prefix_heap[0][0] >= k:
                min_sub = min(min_sub, i - heapq.heappop(prefix_heap)[1])
        
            heapq.heappush(prefix_heap, (cur_sum, i))

        return min_sub if min_sub < float('inf') else -1
