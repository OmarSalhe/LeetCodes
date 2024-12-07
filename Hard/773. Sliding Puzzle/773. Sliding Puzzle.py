from typing import List
import collections

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        zero = -1
        for r in range(2):
            for c in range(3):
                if board[r][c] == 0:
                    zero = (r, c)
                    break

        ans = [[1,2,3],[4,5,0]]
        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        q = collections.deque()
        q.append((zero, board, 0))

        visited = set()
        while q:
            for _ in range(len(q)):
                zero, cur_board, depth = q.popleft()

                state = tuple(val for row in cur_board for val in row) 
                if state in visited:
                    continue
                visited.add(state)

                if cur_board == ans:
                    return depth

                for dr, dc in direction:
                    r, c = zero[0] + dr, zero[1] + dc
                    if (r < 2 and r > -1) and (c < 3 and c > -1): # if move is legal
                        cur_board[zero[0]][zero[1]], cur_board[r][c] = cur_board[r][c], cur_board[zero[0]][zero[1]] # play move
                        q.append(((r,c), [row[:] for row in cur_board], depth + 1)) # save game state
                        cur_board[zero[0]][zero[1]], cur_board[r][c] = cur_board[r][c], cur_board[zero[0]][zero[1]] # reset board
                    
        return -1
