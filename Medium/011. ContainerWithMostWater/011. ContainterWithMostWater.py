from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        two pointers
        if end > start
            check area
            update max area
        else
            shift end back one
        """

        start, end =  0, len(height) - 1
        out = 0
        while start != end:
            a = (end - start) * min(height[end], height[start])
            out = max(out, a)
            if height[start] < height[end]: start += 1
            else: end -= 1

        return out