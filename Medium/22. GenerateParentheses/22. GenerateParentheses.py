from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        def bum_ahh_dfs(n, s='()', visited=set()):
            visited.add(s)
            if n == 0:
                # add leaf to possible combo
                pairs.append(s)
                return
            for i in range(len(s)):
                if s[i] == ')' and (s[:i] + '()' + s[i:]) not in visited:
                    bum_ahh_dfs(n-1, s[:i] + '()' + s[i:] )
            bum_ahh_dfs(n-1, s + '()')
            
            # backtrack
            return
        bum_ahh_dfs(n-1) 
        return pairs