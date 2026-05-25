class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        res = []

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            flag = [0,0]
            visited = set()
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                
                if (row == 0 or col == 0):
                    flag[0] = 1
                if (row==rows-1 or col == cols-1):
                    flag[1] = 1
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and heights[r][c] <= heights[row][col] and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
                        if (r == 0 or c == 0):
                            flag[0] = 1
                        if (r==rows-1 or c == cols-1):
                            flag[1] = 1
            if flag[0] == 1 and flag[1] == 1:
                return True
            else:
                return False

        for r in range(rows):
            for c in range(cols):
                if bfs(r,c):
                    res.append([r,c])

        return res


        