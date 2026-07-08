""" Cong Earthquake is playing the Card Puzzle using cards with '+' (the plus sign), '-' (the minus sign) and N digit cards (with one of the digits '0'-'9' written on them). For convenience, let string S of length N represent the digits in an equation from left to right.

For instance, the example below with N = 3 can be described using S = "184". Cong would leave enough spacing between each pair of adjacent digit cards, and we can see that there are N - 1 spaces.

image

For each space, he can either add plus sign or minus sign or do nothing. Each equation lead to different result and can be calculated.

image

Cong believes a number is special if it follow some format with each digit appear f(i) times. If f(i) = - 1 that i digit can apear any number of times. For example if f[] = {-1, 1, 0, 1, 0, 1, 0, 0, 0, 0} mean special number is number contain 1 digit 1, 1 digit 3, 1 digit 5 and any number of 0 (1053, -1305, -13500, 153, 1503, 100350...)

Help him to check how many equations can generate special number.

Input Format

First line T number of test cases

For each test case first line contain string S

Second line 10 number frequency of

Constraints

2 <= N <= 11

f[i] >= -1

Output Format

Each test case output number of special number in 1 line

Sample Input 0

2
184
0 1 0 0 1 0 0 0 -1 0
184
-1 -1 -1 -1 -1 -1 -1 -1 -1 0
Sample Output 0

2
9
Explanation 0

First test case is example, special number is number with 1 digit 1, 1 digit 4 and any number of 8. There are 2 number satisfy 184 and 14.

Second test case special number is number without digit 9, so total 9 number equations can create special number """

import sys

def solve() -> None:
    input = sys.stdin.read().split()
    it = iter(input)
    t = int(next(it))
    res = []
    for _ in range(t):
        S = next(it)
        f = [int(next(it)) for _ in range(10)]
        n = len(S)
        ans = 0

        # check speical number
        def is_special(num):
            if num < 0:
                num = -num
            cnt = [0] * 10
            if num == 0:
                cnt[0] = 1
            else:
                while num > 0:
                    cnt[num % 10] += 1
                    num //= 10
            for i in range(10):
                if f[i] != -1 and cnt[i] != f[i]:
                    return False
            return True
        # Back tracking to generate all possible equations
        def bt(idx, cur_num, cur_sum, sign):
            nonlocal ans
            if idx == n:
                total = cur_sum + sign * cur_num
                if is_special(total):
                    ans += 1
                return
            d = int(S[idx])
            # option 1: no sign, continue the current number
            bt(idx + 1, cur_num * 10 + d, cur_sum, sign)
            # option 2: add sign, start a new number
            bt(idx + 1, d, cur_sum + sign * cur_num, 1)
            # option 3: subtract sign, start a new number
            bt(idx + 1, d, cur_sum + sign * cur_num, -1)
        bt(1, int(S[0]), 0, 1)
        res.append(str(ans))
    sys.stdout.write('\n'.join(res) + '\n')

if __name__ == "__main__":
    solve()