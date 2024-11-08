class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # marker for last letter
        j = -1

        for i in range(len(s)-1, -1, -1):
            if j == -1 and s[i] != ' ':
                j = i

            elif j != -1 and s[i] == ' ':
                return j - i

        return j+1