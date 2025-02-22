class Solution:
    def canDistribute(self, amount: int, n: int, qty: List[int]) -> bool:
        i, j = 0, 0
        distr = 0
        while i < n and j < len(qty):
            distr += amount
            if distr >= qty[j]:
                distr = 0
                j += 1
            i += 1
        return j == len(qty)

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low, high = 0, max(quantities)
        while low <= high:
            mid = low + (high - low) // 2
            if self.canDistribute(mid, n, quantities):
                high = mid - 1
            else:
                low = mid + 1

        return low

        # TC = O(nlog(m)), where m = the max quantity
        # SC = O(1), no use of auxiliary memory, asides from pointers
