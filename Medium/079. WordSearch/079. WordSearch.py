from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #     right     left    up     down
        DIR = [(0,1), (0,-1), (1,0), (-1, 0)]
        r_max, c_max = len(board), len(board[0])
        def dfs(row, col, letter):

            if letter == len(word)-1 and board[row][col] == word[letter]: return True
            if board[row][col] != word[letter]: return False

            board[row][col] = '#' # -> mark cell as visited
            for dr, dc in DIR:
                r = row + dr
                c = col + dc

                if (r > -1 and r < r_max) and (c > -1 and c < c_max):
                    if dfs(r, c, letter + 1): return True
            
            board[row][col] = word[letter] # -> reset back to og so it can be revisited
            return False

        for r in range(r_max):
            for c in range(c_max):
                if dfs(r, c, 0):
                    return True
        return False

