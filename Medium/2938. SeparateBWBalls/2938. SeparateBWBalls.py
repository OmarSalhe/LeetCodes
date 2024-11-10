class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        swaps = 0
        # all white balls belong on the left side -> start of str
        w = 0
        # ensure you start where you can perform swaps
        while w < n and s[w] == '0' :
            w += 1

        # if already separated, no swapping needed
        if w == n:
            return swaps
        
        # swaps = dist to closest white ball
        for i in range(w, n):
            if s[i] == '0':
                swaps += i - w
                w += 1
        return swaps

        """
        Time Comlpexity = going through n letters and arithmetic = O(n+1) ~ O(n)
        Space Complexity = variables = O(1)
        """
