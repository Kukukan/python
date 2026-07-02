from typing import List
import sys

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for p in patterns:
            if p in word:
                cnt += 1
        return cnt

#Example usage:
if __name__ == "__main__":
    patterns = sys.stdin.readline().strip().split()
    word = sys.stdin.readline().strip()
    solution = Solution()
    result = solution.numOfStrings(patterns, word)
    print(result)