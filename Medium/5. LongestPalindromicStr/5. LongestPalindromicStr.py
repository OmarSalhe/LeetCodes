class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ml = 0
        start = 0
        for i in range(n):
            # for odd length
            a = b = i
            while a >= 0 and b < n and s[a] == s[b]:
                a -= 1
                b += 1
            l = b-a-1
            if l > ml:
                ml = l
                # after a since a is the last spot before failed expansion
                start = a + 1

            # for even length
            a, b = i, i+1
            while a >= 0 and b < n and s[a] == s[b]:
                a -= 1
                b += 1
            l = b-a-1
            if l > ml:
                ml = l
                start = a + 1

        return s[start: start + ml]

            
            
