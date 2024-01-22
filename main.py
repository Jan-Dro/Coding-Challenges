def reverseBits(n):
    rev = 0
    for _ in range(32):
        rev = (rev << 1) | (n & 1)
        n >>= 1
    return rev

print(reverseBits(00000010100101000001111010011100))