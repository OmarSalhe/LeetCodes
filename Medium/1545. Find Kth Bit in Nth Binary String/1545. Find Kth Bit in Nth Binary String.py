class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return '0'
        # on the basis the S_n is mirrored around the middle, asides from being inverted.
        def binary_search(n, k):
            if n == 1:
                return '0'

            left = (1 << (n-1)) - 1 # == (2^n-1)-1 == (2^n / 2) - 1 = half of S_n to the left
            mid = left + 1

            if k == mid:
                return '1'
            
            elif k <= left:
                bit = binary_search(n - 1, k)
                return bit
            
            else:
                # k is on the inversed reversed side
                pos_on_right = 2 * (left + 1) - k
                bit = binary_search(n - 1, pos_on_right)
                # inverse bit
                return '1' if bit == '0' else '0'

        return binary_search(n, k)
        """
        TC = O(logn) = binary search
        SC = O(logn) = call stack
        """

        
