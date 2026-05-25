class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        preMap = {i:[] for i in range(n)}

        for node1, node2 in edges:
            preMap[node1].append(node2)
            preMap[node2].append(node1)

        visited = set()

        def dfs(node):
            for nei in preMap[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        c = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                c+=1
        return c

            
        