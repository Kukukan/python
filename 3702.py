import sys
from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        totalxor = 0
        haszero = False

        for num in nums:
            totalxor ^= num
            if num != 0:
                haszero = True
        
        if not haszero:
            return 0
        if totalxor != 0:
            return len(nums)
        return len(nums) - 1

if __name__ == "__main__":
    data = sys.stdin.readline().split(",")
    nums = list(map(int, data))
    sol = Solution()
    print(sol.longestSubsequence(nums))