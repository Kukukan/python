import sys
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        st = []
        for i in range(n*2 - 1, -1, -1):
            idx = i % n
            while st and st[-1] <= nums[idx]:
                st.pop()
            if i < n and st:
                res[i] = st[-1]
            st.append(nums[idx])
        return res

if __name__ == "__main__":
    input = sys.stdin.read().split()
    sol = Solution()
    print(sol.nextGreaterElements(list(map(int, input))))