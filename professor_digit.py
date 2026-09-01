# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

MAX_N = 10

def solve() -> None:
    data = iter(sys.stdin.read().split())
    
    N = int(next(data))
    
    grid = [next(data) for _ in range(N)]
    # print(grid)
    
    pos = [[] for _ in range(MAX_N)]
    
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            d = int(ch)
            if d != 0:
                pos[d].append((i, j))
    bbox = [None] * MAX_N
    for d in range(1, MAX_N):
        if pos[d]:
            rs = [p[0] for p in pos[d]]
            cs = [p[1] for p in pos[d]]
            bbox[d] = (min(rs), max(rs), min(cs), max(cs))
            
    res = 0
    for a in range(1, MAX_N):
        if not pos[a]:
            continue
        annexed = False
        for r, c in pos[a]:
            for b in range(1, MAX_N):
                if b == a or  not pos[b]:
                    continue
                minr, maxr, minc, maxc = bbox[b]
                if minr <= r <= maxr and minc <= c <= maxc:
                    annexed = True
                    break
                if annexed:
                    break
        if not annexed:
            res += 1
    sys.stdout.write(''.join(str(res)))
if __name__ == "__main__":
    solve()