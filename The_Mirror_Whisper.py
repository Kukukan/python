import sys

def transform_code(k: int, encoded_sub: str):
    # repeat the decode substring k times
    repeated = k * encoded_sub
    """ Right-rotate the resulting string by k positions. 
    (means: Take the last k characters of the string and move them to the front. The remaining characters are shifted to the right.)
    """
    n = len(repeated)
    shift = k % n
    if shift:
        rotated = repeated[-shift:] + repeated[:-shift]
    else:
        rotated = repeated
    
    # If k is odd, reverse the string.
    if k % 2:
        rotated = rotated[::-1]

    """ For every character at zero-based position index , shift it forward in the lowercase English alphabet by: (k + i) % 26
    The alphabet wraps around, so shifting z by 1 produces a.
    """
    chars = []
    for idx, ch in enumerate(rotated):
        shifted_idx = (k + idx) % 26
        old_idx = ord(ch) - ord('a')
        new_idx = (old_idx + shifted_idx) % 26
        new_ch = chr(new_idx + ord('a'))
        chars.append(new_ch)
    shift_str = ''.join(chars)

    mid = (len(shift_str) + 1) // 2
    left = shift_str[:mid]
    right = shift_str[mid:]
    
    res = []
    for i in range(len(right)):
        res.append(left[i])
        res.append(right[i])
    
    if len(left) > len(right):
        res.append(left[-1])

    return ''.join(res)

def decode_mirror_whisper(encoded_str: str) -> str:
    stack = []
    i = 0
    n = len(encoded_str)
    
    current_string = ""
    current_num = 0
    
    while i < n:
        char = encoded_str[i]
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '{':
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == '}':
            prev_string, repeat_count = stack.pop()

			# ==========================================
    		# Write your code in here
            trans = transform_code(repeat_count, current_string)
            
            current_string = prev_string + trans
       
    		# ==========================================


            pass
        else:
            current_string += char
        i += 1
        
    return current_string

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    
    if input_data:
        result = decode_mirror_whisper(input_data)
        
        print(result)