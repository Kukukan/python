from typing import List
import sys

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        i = 1
        # Iterate through the positive multiples of k
        while True:
            if i*k not in nums:
                return i*k

            i += 1


if __name__ == "__main__":
    data = sys.stdin.readline().split(",")
    nums = list(map(int, data))
    k = int(data[1])
    sol = Solution()
    print(sol.missingMultiple(nums, k))