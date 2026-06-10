from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
    
    def isAnagram(self, s: str, t: str) -> bool:
        # check if they are not same length
        if len(s) != len(t):
            return False
        c_t, c_s = {}, {}
        # count the characters in both strings and compare the counts
        for i in range(len(s)):
            c_s[s[i]] = 1 + c_s.get(s[i], 0)
            c_t[t[i]] = 1 + c_t.get(t[i], 0)
        return c_s == c_t
# Example usage
if __name__ == "__main__":
    solution = Solution()
    # random test case for twoSum
    test_case = [2, 11, 0, 15, 7, 7]
    target = 9
    result = solution.twoSum(test_case, target)
    print(result)  # Output: [0, 3]

    test_case = [("listen", "silent"), ("jam", "jar"), ("anagram", "nagaram")]
    for s, t in test_case:
        print(solution.isAnagram(s, t))