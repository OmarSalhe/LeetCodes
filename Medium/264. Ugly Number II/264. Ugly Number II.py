import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        factors = [2, 3, 5]
        seen = set()
        heapq.heapify(heap)
        i, cur = 0, 0
        while heap and i < n:
            cur = heapq.heappop(heap)
            for f in factors:
                num = cur * f
                if num not in seen:
                    heapq.heappush(heap, num)
                    seen.add(num)
            i += 1
        return cur
                
