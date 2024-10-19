class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # max-heap containing (number of letter, letter)
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(heap)
        cooldown = None

        happy = [''] * (a + b + c)
        i = 0

        while heap and i < (a + b + c):
            num, ltr = heapq.heappop(heap)
            if num == 0:
                continue

            happy[i] = ltr
            num += 1

            # if a letter is already in a cooldown state
            if cooldown:
                heapq.heappush(heap, cooldown)
                cooldown = None

            # if a letter was already added twice
            if happy[i] == happy[i-1] and num < 0:
                cooldown = (num, ltr)

            # if more letters remain
            elif num < 0:
                heapq.heappush(heap, (num, ltr))
        
            i += 1
        return ''.join(happy)

        """
        Time Complexity = n heap operations = O(nlogn), where n = a + b + c (worst-case)
        Space Comlpexity = heap = O(n), where n = a + b + c (worst-case)
        """