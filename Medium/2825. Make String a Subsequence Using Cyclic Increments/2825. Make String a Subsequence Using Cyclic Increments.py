class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)
        if n < m:
            return False

        i, j = 0, 0
        while i < n and j < m:
            if str1[i] == str2[j] or (ord(str1[i]) + 1 - ord('a')) % 26 == (ord(str2[j]) - ord('a')):
                j += 1
            i += 1
        
        return j == m

        # TC = O(n) -> single pass through n letters * O(1) operations
        # SC = O(1) -> constant amount of variables used
