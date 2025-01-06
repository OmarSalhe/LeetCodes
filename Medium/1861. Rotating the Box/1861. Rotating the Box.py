class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])

        out = [['' for _ in range(m)] for _ in range(n)]

        # first rotate
        for r in range(n):
            for c in range(m):
                out[r][c] = box[c][r]   
        for r in range(n):
            out[r].reverse()

        # then apply gravity
        for c in range(m):
            empty = n - 1
            for r in range(n-1, -1, -1): # place all stones at their lowest possible point
                if out[r][c] == '*':
                    empty = r - 1
                elif out[r][c] == '#':
                    out[r][c] = '.'
                    out[empty][c] = '#'
                    empty -= 1
                    
        return out
