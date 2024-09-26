# Initialize the memory with 35 'x' characters
memory = ['x'] * 35

# Set the first line to "Acectf"
memory[0] = 'A'
memory[1] = 'C'
memory[2] = 'E'
memory[3] = 'C'
memory[4] = 'T'
memory[5] = 'F'

# Continue with the rest of the operations
memory[6] = chr(123)
memory[20] = 'l'
memory[19] = chr(0x34)
memory[18] = chr(ord(memory[19]) - 1)
memory[17] = 'r'
memory[7] = 'y'
memory[8] = chr(48)
memory[9] = 'u'
memory[10] = '_'
memory[11] = chr(52)
memory[12] = 'r'
memory[13] = chr(51)
memory[14] = '_'
memory[15] = chr(52)
memory[16] = '_'

# XOR operations
memory[21] = chr(ord("'") ^ ord('x'))
memory[22] = chr(ord('L') ^ ord('x'))
memory[23] = chr(11 ^ ord('x'))
memory[24] = chr(ord('M') ^ ord('x'))
memory[25] = chr(ord('K') ^ ord('x'))
memory[26] = chr(0x15 ^ ord('x'))
memory[27] = chr(0x1A ^ ord('x'))
memory[28] = chr(0x14 ^ ord('x'))
memory[29] = chr(0x01 ^ ord('x'))
memory[30] = chr(0x27 ^ ord('x'))
memory[31] = chr(ord('L') ^ ord('x'))
memory[32] = chr(0x1B ^ ord('x'))
memory[33] = chr(0x4B ^ ord('x'))
memory[34] = chr(5 ^ ord('x'))

# Print the final memory state
print(''.join(memory))