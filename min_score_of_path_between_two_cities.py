""" You are given a positive integer n representing n cities numbered from 1 to n. 
You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.

Constraints:

2 <= n <= 105
1 <= roads.length <= 105
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 104
There are no repeated edges.
There is at least one path between 1 and n. """

import sys
from typing import List
from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(n+1)]

        for a, b, dis in roads:
            graph[a].append((b, dis))
            graph[b].append((a, dis))

        visited = set()
        q = deque([1])
        visited.add(1)

        # Perform BFS to find the minimum score of a path between cities 1 and n
        res = float('inf')
        while q:
            cur_city = q.popleft()
            for u, cost in graph[cur_city]:
                res = min(res, cost)
                if u not in visited:
                    visited.add(u)
                    q.append(u)
        return res

if __name__ == "__main__":
    input = sys.stdin.buffer.read().splitlines()
    n = int(input[0])
    roads = [list(map(int, line.split())) for line in input[1:]]
    solution = Solution()
    result = solution.minScore(n, roads)
    print(result)  # Output the minimum possible score of a path between cities 1 and n
