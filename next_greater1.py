from typing import List
import sys
from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        return [next_greater.get(num, -1) for num in nums1]

if __name__ == "__main__":
    sol = Solution()
    nums1 = list(map(int, sys.stdin.readline().strip().split()))
    nums2 = list(map(int, sys.stdin.readline().strip().split()))
    result = sol.nextGreaterElement(nums1, nums2)
    print(result)