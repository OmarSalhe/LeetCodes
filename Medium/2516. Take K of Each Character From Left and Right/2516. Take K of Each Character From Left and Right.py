class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        n = len(s)
        count = [0] * 3
        for i in range(n):
            count[ord(s[i]) - ord('a')] += 1

        if count[0] < k or count[1] < k or count[2] < k:
            return -1


        left, right = 0, 0
        max_win = -1
        while right < n:
            count[ord(s[right]) - ord('a')] -= 1

            while left <= right and (count[0] < k or
                                    count[1] < k or 
                                    count[2] < k):
                count[ord(s[left]) - ord('a')] += 1
                left += 1
            
            max_win = max(max_win, right - left + 1)

            right += 1


        return n - max_win
