import sys

def solve():
    data = iter(sys.stdin.read().split())
    n = int(next(data))
    heights = [int(next(data)) for _ in range(n)]

    nge = [n] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and heights[i] > heights[stack[-1]]:
            stack.pop()
        if stack:
            nge[i] = stack[-1]
        stack.append(i)

    res = 0
    for i in range(n):
        res += nge[i] - i - 1

    sys.stdout.write(str(res))

if __name__ == "__main__":
    solve()