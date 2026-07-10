from typing import List
from bisect import bisect_left
import sys

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i, num in enumerate(nums):
            pos = bisect_left(nums, target - num)
            if pos > i + 1:
                res += (pos - i - 1)
        return res

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        print("Error: expected list of numbers followed by target")
    else:
        nums = list(map(int, data[:-1]))
        target = int(data[-1])
        sol = Solution()
        print(sol.countPairs(nums, target))
