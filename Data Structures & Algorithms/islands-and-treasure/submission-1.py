class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def addSpace(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] == -1:
                return
            q.append([r,c])
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addSpace(r+1,c)
                addSpace(r,c+1)
                addSpace(r-1,c)
                addSpace(r,c-1)
            dist+=1


        