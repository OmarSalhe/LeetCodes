class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adj1 = collections.defaultdict(list)
        for a, b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)
        
        adj2 = collections.defaultdict(list)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        
        cur_max_depths = [-1, -1]
        roots = [0, 0]
        def find_root(tree: int, root: int, parent: int, depth: int, edges: dict) -> None:
            if len(edges[root]) == 1 and depth > cur_max_depths[tree]:
                cur_max_depths[tree] = depth
                roots[tree] = root
            
            for node in edges[root]:
                if node != parent:
                    find_root(tree, node, root, depth + 1, edges)
                

        def dfs(root: int, parent: int, edges: dict) -> int:
            path_len = 0
            for node in edges[root]:
                if node != parent:
                    path_len = max(path_len, dfs(node, root, edges))
            
            return path_len + 1    
        
        find_root(0, 0, -1, 0, adj1)
        find_root(1, 0, -1, 0, adj2)

        a, b = dfs(roots[0], -1, adj1) - 1, dfs(roots[1], -1, adj2) - 1

        return max(a, b, ((a + 1) // 2) + ((b + 1) // 2) + 1)
