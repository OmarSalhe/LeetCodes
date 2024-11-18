from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        # window sum
        win_sum = 0
        if k == 0:
            for i in range(n):
                code[i] = 0
            return code

        elif k > 0:
            for i in range(1, k + 1):
                win_sum += code[(i + n) % n]
            
            res[0] = win_sum
            for i in range(1, n):
                # shift window forward
                win_sum -= code[i]
                win_sum += code[(k + i) % n]

                res[i] = win_sum
        
        else:
            for i in range(n-1, n + k - 1, -1):
                win_sum += code[i % n]

            res[0] = win_sum
            for i in range(1, n):
                # shift window forward
                win_sum -= code[(n + k - 1 + i) % n]
                win_sum += code[(n - 1 + i) % n]

                res[i] = win_sum
        return res
        

