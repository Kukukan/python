from ast import List
import heapq
import sys

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])

        # Dijkstra's algorithm to find the minimum health cost to reach each cell
        min_health_cost = [[float('inf')] * cols for _ in range(rows)]
        min_health_cost[0][0] = grid[0][0]

        # Min-heap priority queue
        pq = [(grid[0][0], 0, 0)]  # (health_cost, row, col)

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # down, right, up, left

        while pq:
            current_cost, r, c = heapq.heappop(pq)

            # If we reached the bottom-right corner
            if r == rows - 1 and c == cols - 1:
                return current_cost < health

            # Explore neighbors (down, right, up, left)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_cost = current_cost + grid[nr][nc]
                    if new_cost < min_health_cost[nr][nc]:
                        min_health_cost[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))
        
        return min_health_cost[rows - 1][cols - 1] < health

if __name__ == "__main__":
    input =  sys.stdin.buffer.read().splitlines()
    grid = [list(map(int, line.split())) for line in input[:-1]]
    health = int(input[-1])
    solution = Solution()
    result = solution.findSafeWalk(grid, health)

    print(result)  # Output True if a safe walk exists, otherwise False