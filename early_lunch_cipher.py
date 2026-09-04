import sys

def sum_of_digit(n):
    return n // 10 + n % 10

def solve():
    input = sys.stdin.readline
    x = int(input())

    cnt = 0
    res = None
    for h in range(24):
        hsh = h << 2
        for m in range(60):
            msh = m << 1
            for s in range(60):
                if (hsh | msh | s) == x:
                    cnt += 1
                    # total = sum_of_digit(hsh) + sum_of_digit(msh) + sum_of_digit(s)
                    total = sum(int(c) for c in f"{h:02d}{m:02d}{s:02d}")
                    candidate = (total, h, m, s)
                    if res is None or candidate < res:
                        res = candidate
    
    if cnt == 0:
        sys.stdout.write(str(0))
    else:
        _, h, m, s = res
        sys.stdout.write(f"{cnt}\n{h:02d}:{m:02d}:{s:02d}")

if __name__ == "__main__":
    solve()
