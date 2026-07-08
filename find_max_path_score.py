from typing import List
import heapq, sys

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        # build graph
        graph = [[] for _ in range(n)]

        max_cost = -float('inf')

        for u,v, c in edges:
            graph[u].append((v, c))
            max_cost = max(max_cost, c)
        
        # check path from 0 to n-1 with at most k online nodes
        def dijkstra(mid):
            dist = [float('inf')] * n
            dist[0] = 0
            # create a min-heap priority queue with current cost and node
            pq = [(0, 0)]  # (cost, node)

            # dijkstra's algorithm
            while pq:
                d, u = heapq.heappop(pq)

                if d > dist[u]:
                    continue
                if u == n - 1:
                    return d <= k
                
                # if node is offline, we cannot use it
                if u != 0 and u != n-1 and not online[u]:
                    continue
                
                for v, c in graph[u]:
                    if c < mid:
                        continue
                    if v != n -1 and not online[v]:
                        continue
                    new_d = d + c
                    if new_d < dist[v]:
                        dist[v] = new_d
                        heapq.heappush(pq, (new_d, v))
            return False
        if not dijkstra(0):
            return -1
        l, r = 0, max_cost
        res = -1
        while l <= r:
            mid = l + (r-l) // 2
            if dijkstra(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
    
if __name__ == "__main__":
    input = sys.stdin.buffer.read().splitlines()
    edges = []
    for line in input[:-2]:
        u, v, c = map(int, line.split())
        edges.append([u, v, c])
    online = list(map(int, input[-2].split()))
    k = int(input[-1])
    solution = Solution()
    result = solution.findMaxPathScore(edges, online, k)
    print(result)  # Output the maximum path score