from typing import List
import sys

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    temperatures = list(map(int, sys.stdin.readline().strip().split()))
    result = sol.dailyTemperatures(temperatures)
    print(result)