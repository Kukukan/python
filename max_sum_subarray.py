from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_sum = nums[0]
        # current_sum = nums[0]
        # for i in range(1, len(nums)):
        #     current_sum = max(nums[i], current_sum + nums[i])
        #     max_sum = max(max_sum, current_sum)
        # return max_sum
        # apply dynamic programming to find the maximum subarray sum
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for idx, num in enumerate(nums[1:], start=1):
            dp[idx] = max(num, dp[idx - 1] + num)
        return max(dp)
    
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    nums = list(map(int, input_data.split()))
    solution = Solution()
    result = solution.maxSubArray(nums)
    print(result)