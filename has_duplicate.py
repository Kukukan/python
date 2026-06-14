from typing import List
import sys

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize a set to keep track of seen numbers
        seen = set()

        # search for duplicates in the list
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
    
# Example usage
if __name__ == "__main__":
    input = sys.stdin.read().strip()
    nums = list(map(int, input.split()))
    solution = Solution()
    print(solution.hasDuplicate(nums))