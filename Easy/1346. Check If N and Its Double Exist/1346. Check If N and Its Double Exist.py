from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hm = {}

        for i in range(len(arr)):
            if hm.get(arr[i]/2) or hm.get(arr[i]*2):
                return True
            hm[arr[i]] = i + 1 # since i = 0 would be considered false
        
        return False
