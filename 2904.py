import sys

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        ones_count = 0
        min_length = float('inf')
        result = ""

        for right in range(n):
            if s[right] == '1':
                ones_count += 1
            while ones_count == k:
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    result = s[left:right + 1]
                elif current_length == min_length and s[left:right + 1] < result:
                    result = s[left:right + 1]
                if s[left] == '1':
                    ones_count -= 1
                left += 1

        return result if result else ""
if __name__ == "__main__":
    data = iter(sys.stdin.read().split())
    s = next(data)
    k = int(next(data))
    sol = Solution()
    print(sol.shortestBeautifulSubstring(s, k))


