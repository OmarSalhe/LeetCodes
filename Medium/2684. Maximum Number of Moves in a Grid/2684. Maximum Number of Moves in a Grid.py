class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # possible moves given
        possible_moves = [(-1, 1), (0, 1), (1, 1)]

        # used to save moves from a specific point
        memo = {}

        def dfs(row, col):
            # if square was already visited -> return max moves from that point on
            if (row, col) in memo:
                return memo[(row, col)]
            
            max_moves = -1
            for r, c in possible_moves:
                dr, dc = row + r, col + c
                # if next move is in the grid
                if (dr > -1 and dr < len(grid)) and (dc > -1 and dc < len(grid[0])):
                    if grid[dr][dc] > grid[row][col]:
                        max_moves = max(max_moves, dfs(dr, dc))
            
            # save max moves found at that point
            memo[(row, col)] = max_moves + 1
            return 1 + max_moves

        max_moves = -1
        # check down the first column 
        for i in range(len(grid)):
            max_moves = max(max_moves, dfs(i, 0))
        
        return max_moves

        # Time Complexity = O(m*n), since (worst-case) I visit every single cell/square
        # Space Complexity = O(m*n), since (worst-case) I cache every single cell/sqaure
