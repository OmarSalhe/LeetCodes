class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        left = [0] * h
        right = [0] * h

        # Preproccessing 
        left[0] = height[0]
        for i in range(1,h):
            left[i] = max(height[i], left[i-1])
            
        right[h-1] = height[h-1]
        for i in range(h-2, -1, -1):
            right[i] = max(height[i], right[i+1])

        # Finding water
        w = 0
        for i in range(h):
            x = min(right[i], left[i])
            if height[i] < x:
                w += max(x - height[i], 0)
        return w