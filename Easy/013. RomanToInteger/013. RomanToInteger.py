class Solution:
    def romanToInt(self, s: str) -> int:
        romanTranslate = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M':1000}
        num = 0
        length = len(s) - 1
        for i in range(length):       
            nextIndex = i + 1
            if romanTranslate[s[i]] >= romanTranslate[s[nextIndex]]:
                num += romanTranslate[s[i]]
            else:
                num -= romanTranslate[s[i]]
            
        return num + romanTranslate[s[length]]
