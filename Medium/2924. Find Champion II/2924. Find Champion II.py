class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers = [False] * n

        for a, b in edges:
            losers[b] = True

        winner = -1
        num_win = 0
        for team in range(n):
            if not losers[team]:
                winner = team
                num_win += 1

        if num_win == 1:
            return winner
            
        return -1 


        # TC = O(E), there may or may not be more edges than nodes (depends on the graph)
        # SC = O(n), losers set contains between 0 to n teams
