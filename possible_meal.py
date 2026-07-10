import sys
from bisect import bisect_left

def solve() -> None:
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    p = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    B = [int(next(it)) for _ in range(m)]

    B.sort()
    prefix = [0]
    for bi in B:
        prefix.append(prefix[-1] + bi)
    res = 0
    for ai in A:
        pos = bisect_left(B, p - ai)

        tsmall = pos
        tlarge = m - pos
        res += tsmall*ai + prefix[pos]
        res += tlarge*p
    
    print(res)

if __name__ == "__main__":
    solve()