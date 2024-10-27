from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hm = {num: num for num in nums}
        rank = {num: 0 for num in nums}

        def find(x):
            if hm[x] != x:
                hm[x] = find(hm[x])
            return hm[x]

        def union(x, y):
            rootX, rootY = find(hm[x]), find(hm[y])
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    hm[rootY] = rootX
                elif rank[rootY] < rank[rootX]:
                    hm[rootX] = rootY
                else:
                    hm[rootY] = rootX
                    rank[rootX] += 1

        for num in nums:
            if num - 1 in hm:
                union(num, num - 1)

        size = collections.Counter([find(num) for num in hm])
        return max(size.values())

        """
        if an immediate number is found
        make the immediate number's parent the cur number's parent
        
        parent = [1, 2, 3] num = [1, 2, 3]
        parent = [1, 1, 3]
        parent = [1, 1, 1]

        3 -> 4, but when 2 -> 3 4 doesnt update its connection to 3
        instead of linking to base just link to next value?

        1 -> 2 -> 3 -> 4 -> 5
        iterate through chain formed
        """
