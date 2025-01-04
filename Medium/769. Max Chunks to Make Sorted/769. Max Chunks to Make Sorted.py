class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        x = 0
        for i in range(len(arr)):
            x += arr[i]
            if x == (i * (i + 1)) / 2:
                chunks += 1
        return chunks
