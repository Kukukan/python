from typing import List
import sys, collections
from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # bfs invert approach
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            queue = deque([(r, c)])
            visited[r][c] = True
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and grid[new_x][new_y] == 1:
                        visited[new_x][new_y] = True
                        queue.append((new_x, new_y))
        
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and grid[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)
        enclave_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    enclave_count += 1
        return enclave_count

# Example usage
# input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
if __name__ == "__main__":
    # read input from stdin like above example
    input = sys.stdin.read().strip()
    grid = [list(map(int, row.split())) for row in input.splitlines()]
    solution = Solution()
    print(solution.numEnclaves(grid))