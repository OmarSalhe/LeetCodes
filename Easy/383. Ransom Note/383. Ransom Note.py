class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ltr = [0] * 26

        for i in range(len(magazine)):
            ltr[ord(magazine[i]) - ord('a')] += 1

        for i in range(len(ransomNote)):
            if ltr[ord(ransomNote[i]) - ord('a')] == 0:
                return False
            else:
                ltr[ord(ransomNote[i]) - ord('a')] -= 1
        
        return True
        # TC = O(n) -> single pass
        # SC = O(26) ~ O(1) -> alphabet arr

