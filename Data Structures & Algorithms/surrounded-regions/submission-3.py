class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            q = []
            q.append((r,c))
            while q:
                row, col = q.pop()
                board[row][col] = "#"

                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and board[r][c] == "O":
                        board[r][c] = "#"
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if (r==0 or c==0 or r==rows-1 or c==cols-1) and board[r][c]=="O":
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"