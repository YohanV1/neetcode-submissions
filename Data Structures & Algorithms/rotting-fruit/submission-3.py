class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addFruit(r,c):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] == 0:
                return
            q.append([r,c])
            visited.add((r,c))
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))

        if not q:
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        return -1
            return 0

        time = -1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                addFruit(r+1, c)
                addFruit(r-1, c)
                addFruit(r, c+1)
                addFruit(r, c-1)
                if grid[r][c] == 1:
                    grid[r][c] = 2
            time += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return time


        