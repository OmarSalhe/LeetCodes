class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        count = [0]
        def dfs(root, parent):
            cur_val = values[root]
            for node in adj[root]:
                if node != parent:
                    cur_val += dfs(node, root)
                
            if cur_val % k == 0:
                print(f'valid tree rooted at {root}')
                count[0] += 1

            return cur_val

        
        dfs(0, -1)
        return count[0]
