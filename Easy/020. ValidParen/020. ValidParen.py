from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # keep track of open
        q = deque()

        # possible pairings
        pairs = {'(':')', '[':']', '{':'}'}
        for c in s:
            # if new open
            if c in pairs:
                q.appendleft(c)
            elif q and c == pairs[q[0]]:
                q.popleft()
            else:
                return False

        return False if q else True

