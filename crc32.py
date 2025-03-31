def generate_crc32_table():
    """Generate the CRC-32 lookup table."""
    poly = 0xEDB88320  # Reversed polynomial for CRC-32
    table = [0] * 256
    for i in range(256):
        crc = i
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
        table[i] = crc
    return table

# Precompute the CRC-32 lookup table
crc32_table = generate_crc32_table()

def crc32(data: bytes) -> int:
    """Compute the CRC-32 checksum for the input data."""
    crc = 0xFFFFFFFF  # Initial value
    for byte in data:
        # XOR the byte with the lower 8 bits of the CRC
        lookup_index = (crc ^ byte) & 0xFF
        # Shift CRC right by 8 bits and XOR with the table value
        crc = (crc >> 8) ^ crc32_table[lookup_index]
    # Apply final XOR to invert the bits
    return crc ^ 0xFFFFFFFF

# Example usage
if __name__ == "__main__":
    test_data = b"123456789"
    checksum = crc32(test_data)
    print(f"CRC-32 of '{test_data.decode()}': 0x{checksum:08x}")  # Output: 0xcbf43926
    import binascii
    assert crc32(test_data) == binascii.crc32(test_data)

