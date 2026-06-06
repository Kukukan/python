def encode_bit(input_str: str) -> bytearray:
    packed_bytes = bytearray()
    
    original_length = len(input_str)
    packed_bytes.append((original_length >> 0) & 0xFF)
    packed_bytes.append((original_length >> 8) & 0xFF)
    packed_bytes.append((original_length >> 16) & 0xFF)
    packed_bytes.append((original_length >> 24) & 0xFF)

    buffer = 0
    bits_in_buffer = 0

    for char in input_str:
        char_bit = ord(char) & 0x7F
        
        buffer |= (char_bit << bits_in_buffer)
        bits_in_buffer += 7

        while bits_in_buffer >= 8:
            packed_bytes.append(buffer & 0xFF)
            buffer >>= 8
            bits_in_buffer -= 8

    if bits_in_buffer > 0:
        packed_bytes.append(buffer & 0xFF)

    return packed_bytes

# Enter your code here
def decode_bit(packed_bytes: bytearray) -> str:
    if len(packed_bytes) < 4:
        return ""

    # Reconstruct the original length from the first 4 bytes
    L = (packed_bytes[0] |
         (packed_bytes[1] << 8) |
         (packed_bytes[2] << 16) |
         (packed_bytes[3] << 24))

    # The rest are the packed data bytes
    data = packed_bytes[4:]

    result = []
    bit_buffer = 0      # holds up to 8 bits or more read from the stream
    bits_in_buffer = 0  # number of valid bits currently in bit_buffer
    byte_idx = 0        # current position in data

    total_bits_needed = L * 7
    bits_extracted = 0

    while bits_extracted < total_bits_needed:
        # Fill the buffer until we have at least 7 bits, if data remains
        while bits_in_buffer < 7 and byte_idx < len(data):
            bit_buffer |= (data[byte_idx] << bits_in_buffer)
            bits_in_buffer += 8
            byte_idx += 1

        # Extract the lowest 7 bits one character
        char_code = bit_buffer & 0x7F
        result.append(chr(char_code))

        # Remove the extracted 7 bits from the buffer
        bit_buffer >>= 7
        bits_in_buffer -= 7
        bits_extracted += 7

    return ''.join(result)

if __name__ == "__main__":
    tc = int(input())
    
    for _ in range(tc):
        n = int(input())
        compressed_data = bytes(map(int, input().split()))
        
        # Encode
        # compressed_data = encode_bit(original_text)
        
        # Decode
        decompressed_text = decode_bit(compressed_data)
        
        print(decompressed_text)
        
        # if original_text == decompressed_text:
        #     print("SUCCESS")
        # else:
        #     print("FAILED")
