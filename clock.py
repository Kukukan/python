# Cong Earthquake has a 24-hour clock that shows the time in the format "HH:MM" (00 ≤ HH ≤ 23, 00 ≤ MM ≤ 59). Cong want to check clock every X minutes after current time S and he want to calculate how many different palindrome time he will see.

# For example, if Cong start looking at the clock at 06:12 and repeat every 180 minutes (i.e. every 3 hours), then he will see the times 06:12, 09:12, 12:12, 15:12, 18:12, 21:12, 00:12, 03:12, and the times will continue to repeat. Here the time 21:12 is the only palindrome he will ever see, so the answer is 1

# A palindrome is a string that reads the same backward as forward. For example, the times 12:21, 05:50, 11:11 are palindromes but 13:13, 22:10, 02:22 are not.

# Help him to calculate it.

# Input Format

# First line T number of testcase

# Each test case string S and number X

# Constraints

# 1 <= T <= 100

# 1 <= X <= 1440

# Output Format

# Each test case output 1 line total number of palindrome time he see

import sys
import math

def solve() -> None:
    # Precompute palindrome times in a day (0..1439 minutes)
    is_pal = [False] * 1440
    for m in range(1440):
        hh = m // 60
        mm = m % 60
        hh_str = f"{hh:02d}"
        mm_str = f"{mm:02d}"
        if hh_str == mm_str[::-1]:
            is_pal[m] = True

    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        S = next(it)
        X = int(next(it))
        hh = int(S[0:2])
        mm = int(S[3:5])
        start = hh * 60 + mm

        g = math.gcd(X, 1440)
        steps = 1440 // g

        cnt = 0
        for k in range(steps):
            t = (start + k * X) % 1440
            if is_pal[t]:
                cnt += 1
        out_lines.append(str(cnt))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()