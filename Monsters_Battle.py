import sys

def check(H, a, b, m):
    k = 0
    for h in H:
        if h > m * b:
            dmg = h - m * b
            k += (dmg + (a -b ) - 1) // (a - b)
    return k <= m

def solve():
    input = iter(sys.stdin.read().split())
    N = int(next(input))
    A = int(next(input))
    B = int(next(input))
    H = [int(next(input)) for _ in range(N)]

    # print(N, A, B)
    # print(H)
    lo = 1
    hi = max(H) // B + 1
    res = hi
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if check(H, A, B, mid):
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1

    sys.stdout.write(str(res))

if __name__ == "__main__":
    solve()