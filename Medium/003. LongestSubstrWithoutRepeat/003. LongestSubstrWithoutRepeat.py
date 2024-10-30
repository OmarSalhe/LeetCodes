from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        # letters in window
        w_letter = defaultdict(int)
        w_letter[s[0]] += 1

        # window length
        w_len = -1
        

        # add and remove letters in window as it shifts down the str
        # if any repeats remove up until dup, shift left bound, and continue
        i = 0
        for j in range(1, len(s)): # started at 1 for prior idea, now I don't feel like changing
            if w_letter[s[j]] > 0:
                w_len = max(w_len, j - i)
                while s[i] != s[j]:
                    w_letter[s[i]] = 0
                    i += 1
                i += 1
            
            w_letter[s[j]] = 1

        return max(w_len, j - i + 1)

# TC = O(n^2), b/c of the inner loop (damn)
# SC = O(26) (worst-case), 26 letters in the alphabet


