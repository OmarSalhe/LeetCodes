from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # min-heap to store value, list index -> row, element index -> col
        pq = []
        max_val = float("-inf")
        # where the interval starts
        a = 0
        # where the interval ends
        b = float("inf")

        # number of lists
        k = len(nums)

        # add the first elements from each list into the min-heap
        for i in range(k):
            heapq.heappush(pq, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])

        # continue until can't proceed further
        while len(pq) == k: # -> checks all lists have remaining elements
            min_val, row, col = heapq.heappop(pq)

            # update the smallest range
            if max_val - min_val < b - a:
                a = min_val
                b = max_val

            # if possible, add the next element from the same row to the heap
            if col + 1 < len(nums[row]):
                next_val = nums[row][col + 1]
                heapq.heappush(pq, (next_val, row, col + 1))
                # update max to include elements from all k lists
                max_val = max(max_val, next_val)

        return [a, b]
