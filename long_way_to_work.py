# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

def solve() -> None:
    data = iter(sys.stdin.read().split())
    N = int(next(data))
    G = int(next(data))
    B = int(next(data))
    D = int(next(data))
    
    stations = []
    for _ in range(N):
        x = int(next(data))
        y = int(next(data))
        stations.append((x, y))
    # sort stations by the distance
    stations.sort()
    
    stations.append((D, 0))
    
    pos = 0
    cost = 0
    q = deque([(B, 0)])
    
    for x, p in stations:
        dist = x - pos
        
        while dist > 0:
            if not q:
                print(-1)
                return
            cap, price = q.popleft()
            if cap <= dist:
                dist -= cap
                cost += cap*price
            else:
                cap -= dist
                cost += dist*price
                dist = 0
                q.appendleft([cap, price])
        pos = x
        if pos == D:
            break
        
        while q and q[-1][1] > p:
            q.pop()
            
        current_fuel = sum(fuel for fuel, price in q)
        
        fill_amount = G - current_fuel
        if fill_amount > 0:
            q.append([fill_amount, p])
    print(cost)
    
if __name__ == "__main__":
    solve()