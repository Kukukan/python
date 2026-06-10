from ast import List
import sys

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        # two pointers approach
        while l < r:
            # width = r - l
            # height = min(heights[l], heights[r])

            # calculate the area and update the result
            cur_area = (r - l) * min(heights[l], heights[r])
            res = max(res, cur_area)

            # move the pointer that has the smaller height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

# Example usage
if __name__ == "__main__":
    rl = sys.stdin.readline
    heights = list(map(int, rl().strip().split()))
    # print("Heights:", heights)
    solution = Solution()
    result = solution.maxArea(heights)
    print(result)