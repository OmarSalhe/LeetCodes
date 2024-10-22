class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        i_i__i__i_i__i____i_____i
        """
        if stones[0] != 0 or stones[1] != 1:
            return False

        # keep track of accessible rocks
        rocks = {pos: False for pos in stones}
        # keep track of visited paths
        memo = {}
        def helper(dist, k):
            # if position was reached prior
            if (dist, k) in memo:
                return memo[(dist, k)]
            # if end reached
            if dist == stones[-1]:
                rocks[dist] = True
            # make all possible jumps
            for i in range(-1, 2):
                jump = k+i
                next_dist = dist+jump
                # only make legal jumps to existing rocks
                if jump > 0 and next_dist in rocks:
                    if helper(next_dist, jump):
                        memo[(dist, k)] = True
                        return True
            memo[(dist, k)] = False
            return False
        helper(stones[1], 1)
        return rocks[stones[-1]]
            