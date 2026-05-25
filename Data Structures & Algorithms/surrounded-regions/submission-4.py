class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                row, col = stack.pop()
                board[row][col] = "#"
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        stack.append((nr, nc))

        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == "O":
                    dfs(r, c)
        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == "O":
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
