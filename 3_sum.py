from typing import List
import sys

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers approach
        # nums.sort()
        # res = []
        # for i in range(len(nums) - 2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue

        #     left, right = i + 1, len(nums) - 1
        #     while left < right:
        #         total = nums[i] + nums[left] + nums[right]
        #         if total < 0:
        #             left += 1
        #         elif total > 0:
        #             right -= 1
        #         else:
        #             res.append([nums[i], nums[left], nums[right]])
        #             left += 1
        #             right -= 1
        #             while left < right and nums[left] == nums[left-1]:
        #                 left += 1
        # hash map approach
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    res.append([nums[i], nums[j], complement])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])

        return res
    
# Example usage
if __name__ == "__main__":
    input = sys.stdin.read().strip()
    nums = list(map(int, input.split()))
    solution = Solution()
    print(solution.threeSum(nums))