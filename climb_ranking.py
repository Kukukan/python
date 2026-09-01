import sys
from bisect import bisect_right
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = sorted(set(ranked), reverse=True)
    res = []
    # for score in player:
    #     l, r = 0, len(ranked)-1
    #     while l <= r:
    #         m = l + (r-l)//2
    #         if ranked[m] == score:
    #             l = m
    #             break
    #         elif ranked[m] < score:
    #             r = m -1
    #         else:
    #             l = m + 1
    #     res.append(l+1)
    for score in player:
        idx = bisect_right(ranked[::-1], score)
        res.append(len(ranked) - idx + 1)
    return res
    

if __name__ == '__main__':
    data = sys.stdin.read().splitlines()
    it = iter(data)
    ranked_count = int(next(it).strip())
    ranked = list(map(int, next(it).rstrip().split()))
    player_count = int(next(it).strip())
    player = list(map(int, next(it).rstrip().split()))
    sys.stdout.write('\n'.join(map(str, climbingLeaderboard(ranked, player))) + '\n')