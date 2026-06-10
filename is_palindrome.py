import sys

def is_palindrome(s):
    # Remove spaces, numbers, special characters and convert to lowercase
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())

    left, right = 0, len(cleaned_s) - 1
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1
    return True

# main function to test the is_palindrome function
if __name__ == "__main__":
    str = sys.stdin.read().strip()
    if is_palindrome(str):
        print("YES")
    else:
        print("NO")