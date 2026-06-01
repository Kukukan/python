import random
import string

# prefix = input()

# def generate_codes(quantity):
#     codes = []
#     for _ in range(quantity):
#         letters = ''.join(random.choices(string.ascii_uppercase, k=1))
#         numbers = ''.join(random.choices(string.digits, k=3))
#         codes.append(prefix + letters + numbers)
#     return codes

# lucky_codes = generate_codes(100)
# print(lucky_codes)

def reverse_strings(s) :
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str

test_string = input()
reversed_string = reverse_strings(test_string)
print(reversed_string)