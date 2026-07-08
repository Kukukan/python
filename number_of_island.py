import sys
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = [[False] * cols for _ in range(rows)]
        # vis = set()
        def bfs(i, j):
            q = deque([(i,j)])
            vis[i][j] = True
            while q:
                r, c = q.popleft()
                for dr, dc in direc:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and not vis[nr][nc]:
                        vis[nr][nc] = True
                        q.append((nr,nc))
    
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not vis[i][j]:
                    res += 1
                    bfs(i, j)
        return res

# grid=[["0","1","1","1","0"],["0","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# -> convert to
# 0 1 1 1 0
# 0 1 0 1 0
# 1 1 0 0 0
# 0 0 0 0 0

if __name__ == "__main__":
    sol = Solution()
    input = sys.stdin.read().strip().splitlines()
    grid = [list(line.strip().split()) for line in input]
    result = sol.numIslands(grid)
    print(result)