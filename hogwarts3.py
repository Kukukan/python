import sys

def solve() -> None:
    data = iter(sys.stdin.read().split())
    N = int(next(data))
    Q = int(next(data))
    S = next(data)

    prefix = [0]
    stack = []
    cnt = 0
    for c in S:
        while stack and stack[-1] > c:
            stack.pop()
        if not stack or stack[-1] < c:
            stack.append(c)
            cnt += 1
        prefix.append(cnt)
    suffix = [0]
    stack = []
    cnt = 0
    for c in S[::-1]:
        while stack and stack[-1] > c:
            stack.pop()
        if not stack or stack[-1] < c:
            stack.append(c)
            cnt += 1
        suffix.append(cnt)
    
    out = []
    for _ in range(Q):
        a = int(next(data))
        b = int(next(data))
        ans = prefix[a-1] + suffix[N-b]
        out.append(str(ans) + "\n")
    sys.stdout.write("".join(out))

if __name__ == "__main__":
    solve()