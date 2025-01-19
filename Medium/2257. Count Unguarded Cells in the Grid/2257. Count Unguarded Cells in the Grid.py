from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [['U' for _ in range(n)] for _ in range(m)]

        for r, c in guards:
            matrix[r][c] = 'G'

        for r, c in walls:
            matrix[r][c] = 'W'


        for r, c in guards:
            i = r - 1
            while i > -1 and matrix[i][c] != 'W' and matrix[i][c] != 'G':
                matrix[i][c] = 'X'
                i -= 1

            i = r + 1
            while i < m and matrix[i][c] != 'W' and matrix[i][c] != 'G':
                matrix[i][c] = 'X'
                i += 1
            
            i = c - 1
            while i > -1 and matrix[r][i] != 'W' and matrix[r][i] != 'G':
                matrix[r][i] = 'X'
                i -= 1
            
            i = c + 1
            while i < n and matrix[r][i] != 'W' and matrix[r][i] != 'G':
                matrix[r][i] = 'X'
                i += 1

        unguarded = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 'U':
                    unguarded += 1
        return unguarded

        """
        approach #2 (brute-force):
            mark all cells visible to guards as 'guarded'
            stop if wall or bounds
        """

        # seen = set((r, c) for r, c in guards)
        # walls = set((r, c) for r, c in walls)

        # DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)] # down, right, up, left
        # q = collections.deque([(r, c, False, False, False, False) for r, c in guards])
        # while q:
        #     for _ in range(len(q)):
        #         cur_r, cur_c, up, down, left, right = q.popleft()
        #         if (cur_r, cur_c) in walls:
        #             continue

        #         seen.add((cur_r, cur_c)) 

        #         if not up and not down and not left and not right: # if a guard
        #             for dr, dc in DIR:
        #                 r, c = cur_r + dr, cur_c + dc
        #                 if (r < m and r > -1) and (c < n and c > -1): # if in bound
        #                     if dc < 0: # left
        #                         q.append((r, c, False, False, True, False))
        #                     elif dc > 0: # right
        #                         q.append((r, c, False, False, False, True))
        #                     elif dr < 0: # up
        #                         q.append((r, c, True, False, False, False))
        #                     elif dr > 0: # down
        #                         q.append((r, c, False, True, False, False))
        #         else: # else (checking what a guard sees)
        #             if left and cur_c - 1 > -1:
        #                 q.append((cur_r, cur_c - 1, False, False, True, False))
        #             elif right and cur_c + 1 < n:
        #                 q.append((cur_r, cur_c + 1, False, False, False, True))
        #             elif up and cur_r - 1 > -1:
        #                 q.append((cur_r - 1, cur_c, True, False, False, False))
        #             elif down and cur_r + 1 < m:
        #                 q.append((cur_r + 1, cur_c, False, True, False, False))

        # return m * n - len(seen) - len(walls)

        """
        notes: guards see in 4 direction infinite distance
               walls can obstruct view
               count how many squares not in view (blocked or diags?)
               can't see past bounds
               can overlap
        
        approach (bfs type):
            for each guard in graph;
                store into queue


            for each saved guard:
                for each direction
                    go until a wall or OOB
                    save every cell on the way
            
            unguarded cells = total cells - guarded - walls, total cells = area of graph
        """
