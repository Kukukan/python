import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        edges = []
        max_w = 0
        for __ in range(m):
            u = int(next(it)); v = int(next(it)); w = int(next(it))
            edges.append((u, v, w))
            if w > max_w: max_w = w
        src = int(next(it)); dst = int(next(it)); k = int(next(it))
        
        if src == dst:
            out_lines.append("0")
            continue
        
        # binary search on threshold
        lo, hi = 0, max_w
        ans = -1
        
        def feasible(T: int) -> bool:
            # 0-1 BFS: cost 0 for light edges (w <= T), cost 1 for heavy (w > T)
            dist = [10**9] * n
            dist[src] = 0
            dq = deque()
            dq.append(src)
            while dq:
                u = dq.popleft()
                for uu, vv, w in edges:
                    if uu == u:
                        v = vv
                    elif vv == u:
                        v = uu
                    else:
                        continue
                    cost = 1 if w > T else 0
                    if dist[u] + cost < dist[v]:
                        dist[v] = dist[u] + cost
                        if cost == 0:
                            dq.appendleft(v)
                        else:
                            dq.append(v)
            return dist[dst] <= k
        
        # binary search
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        # if no feasible threshold, ans remains -1
        out_lines.append(str(ans))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()