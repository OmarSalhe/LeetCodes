class Solution:
    def maximumLength(self, s: str) -> int:
        intervals = collections.defaultdict(list)
        start, end = 0, 0
        while end < len(s):
            start = end
            while end < len(s) and s[start] == s[end]:
                end += 1
            intervals[s[start]].append((start, end))

        matrix = [[0 for _ in range(len(s) + 1)] for _ in range(26)]
        for ltr in intervals:
            print(intervals[ltr])
            for start, end in intervals[ltr]:
                size = end - start
                for i in range(1, size + 1):
                    matrix[ord(ltr) - ord('a')][i] += size - i + 1
        
        candidet = -1
        for ltr in intervals:
            row = matrix[ord(ltr) - ord('a')]
            for i in range(len(row)):
                if row[i] >= 3:
                    candidet = max(candidet, i)

        return candidet
