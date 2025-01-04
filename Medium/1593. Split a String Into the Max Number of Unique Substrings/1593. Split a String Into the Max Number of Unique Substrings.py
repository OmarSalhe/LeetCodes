class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def countUnique(unique, i, j):
            # if end of string reached
            if i == len(s):
                return 0

            count = 0
            while j < len(s):
                if s[i:j+1] not in unique:
                    cur = s[i:j+1]
                    unique.add(cur)
                    count = max(count, 1 + countUnique(unique, j+1, j+1))
                    unique.remove(cur)
                j += 1
            
            return count

        # i = left bound (inclusive)
        # j = right bound (exclusive)
        return countUnique(set(), 0, 0)
"""
Time Complexity = O(n^2) (maybe, kinda, idk) -> 1 node with n-1 children, each with n-2 children ...
so like 1 + n-1(n-2) + n-2(n-3) + ... + n-n-1(n-n), which is a big polynomial that rounds 
to n^2 (don't quote me)

Space Complexity = each call has a substr/node to process? so the # of nodes? = O(n^2)
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def countUnique(unique, i, j):
            # if end of string reached
            if i == len(s):
                return 0
            count = 0
            while j < len(s):
                if s[i:j+1] not in unique:
                    cur = s[i:j+1]
                    unique.add(cur)
                    count = max(count, 1 + countUnique(unique, j+1, j+1))
                    unique.remove(cur)
                j += 1
            return count
        # i = left bound (inclusive)
        # j = right bound (exclusive)
        return countUnique(set(), 0, 0)
"""
Time Complexity = O(n^2) (maybe, kinda, idk) -> 1 node with n-1 children, each with n-2 children ...
so like 1 + n-1(n-2) + n-2(n-3) + ... + n-n-1(n-n), which is a big polynomial that rounds 
to n^2 (don't quote me)
Space Complexity = each call has a substr/node to process? so the # of nodes? = O(n^2)
"""
