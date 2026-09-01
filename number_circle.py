import sys
from collections import deque

def solve() -> None:
    input = sys.stdin.read().strip().split()
    it = iter(input)
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]

    # duplicate a
    b = a + a
    # build prefix sum array
    p = [0] * (2 * n + 1)
    for i in range(2*n):
        p[i + 1] = p[i] + b[i]

    # deque to store indices of the prefix sum array
    maxsum = -float('inf')
    dq = deque()
    for i in range(len(p)):
        # remove indices that are out of the window
        while dq and dq[0] < i - k:
            dq.popleft()
        # update maxsum
        if dq:
            maxsum = max(maxsum, p[i] - p[dq[0]])
        # maintain deque in increasing order of prefix sums
        while dq and p[dq[-1]] >= p[i]:
            dq.pop()
        dq.append(i)
    print(maxsum)

if __name__ == "__main__":
    solve()