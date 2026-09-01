import sys
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        mp = {}
        for idx, el in enumerate(temp):
            if el not in mp:
                mp[el] = idx + 1
        res = []
        for num in arr:
            res.append(mp[num])
        return res

if __name__ == "__main__":
    input = sys.stdin.read().split()
    arr = list(map(int, input))
    sol = Solution()
    print(sol.arrayRankTransform(arr))