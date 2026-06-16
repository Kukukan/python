from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(r, c):
            queue = deque([(r, c)])
            image[r][c] = color
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < rows and 0 <= new_y < cols and image[new_x][new_y] == original_color:
                        image[new_x][new_y] = color
                        queue.append((new_x, new_y))
        
        bfs(sr, sc)
        return image

# Example usage
if __name__ == "__main__":
    # image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    import sys
    input = sys.stdin.read().strip()
    lines = input.splitlines()
    image = [list(map(int, line.split())) for line in lines[:-1]]
    sr, sc, color = map(int, lines[-1].split())
    solution = Solution()
    print(solution.floodFill(image, sr, sc, color))