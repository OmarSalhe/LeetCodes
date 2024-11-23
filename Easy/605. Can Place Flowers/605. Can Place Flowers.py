from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        m = len(flowerbed)
        while i < m:
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == m - 1) or (flowerbed[i + 1] == 0)
                
                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True

            i += 1
                    
        return n <= 0
