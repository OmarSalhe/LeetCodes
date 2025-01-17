class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        val = [[False, 0] for _ in range(len(s) + 1)]
        for i in range(len(shifts)):
            start, end, direction = shifts[i]
            sign = 1 if direction else -1
            val[start][0], val[start][1] = True, val[start][1] + sign
            val[end + 1][0], val[end + 1][1] = True, val[end + 1][1] - sign
        
        shift = 0
        res = []
        for i in range(len(s)):
            if val[i][0]:
                shift += val[i][1]
            
            res.append(chr((ord(s[i]) + shift - ord('a')) % 26 + ord('a')))
        
        return ''.join(res)
