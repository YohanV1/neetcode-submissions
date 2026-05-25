class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        maxArea = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            count = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == 1):
                        q.append((r,c))
                        visited.add((r,c))
                        count += 1
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    maxArea = max(area, maxArea)
        return maxArea

