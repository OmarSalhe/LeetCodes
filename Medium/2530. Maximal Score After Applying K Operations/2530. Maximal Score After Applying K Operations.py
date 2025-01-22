class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        def ceil(n): # -> ceiling function
            return n // 3 if n % 3 == 0 else (n // 3) + 1
        

        # turning default min-heap to max-heap
        heap = [-num for num in nums]
        heapq.heapify(heap)

        i = 0
        score = 0
        # add highest points to score each turn until k turns
        while i < k:
            i += 1
            points = -heapq.heappop(heap)
            score += points
            heapq.heappush(heap, -ceil(points))

        return score

        """
        Approach is straight-forward: just add the biggest number in the list, divide it by 3, repeat

        Time Complexity = heappush + heappop, k times = O(2klogn) ~ O(klogn)
        Space Complexity = heap = O(n)
        """
