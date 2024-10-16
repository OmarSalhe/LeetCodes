class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # can i assume the wordDict contains words related to the given string?
        n = len(s)
        # marks start of word as true
        dp = [False] * (n + 1)
        dp[0] = True

        # for each letter
        for i in range(n):
            # if a word starts there
            if dp[i]:
                # check if a word can be formed from there
                for j in range(i+1, n+1):
                    if s[i:j] in wordDict:
                        # mark potential start to new word
                        dp[j] = True

        # if end of string reached successfully i.e. all prior letters formed words
        return dp[j]