class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i: [] for i in range(n)}
        for node1, node2 in edges:
            preMap[node1].append(node2)
            preMap[node2].append(node1)

        visited = set()
        output = 0

        def dfs(node, parent):
            visited.add(node)
            for nei in preMap[node]:
                if nei == parent:
                    continue
                if nei not in visited:
                    dfs(nei, node)

        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                output += 1

        return output
