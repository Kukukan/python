import sys

def helper(arr, t, p):
    ok = 1
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        if total > t:
            ok += 1
            total = arr[i]
    return ok <= p

def solve():
    readl = sys.stdin.readline
    n, k = map(int, readl().split())
    s_bag = list(map(int, readl().split()))

    for i in range(n):
        if s_bag[i] == -1:
            s_bag[i] = 0

    right = sum(s_bag)
    left = max(s_bag)

    ans = right

    while left < right:
        m = left + (right - left) // 2
        if helper(s_bag, m, k):
            ans = m
            right = m
        else:
            left = m + 1

    print(ans)

if __name__ == "__main__":
    solve()
