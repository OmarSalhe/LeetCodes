from typing import List
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        marked = set()
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        while heap:
            cur, index = heapq.heappop(heap)
            if index in marked:
                continue
            
            score += cur
            marked.add(index + 1)
            marked.add(index - 1)

        return score
