from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s, b = min(strs), max(strs) # min and max gives outlying strings (i.e. diff letters or just really short/long)
        for i in range(len(s)):
            if s[i] != b[i]: # check to see where the outlying stings differ
                return s[:i]
        return s

