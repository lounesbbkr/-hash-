def convert_sequence(sequence):
    binary_sequence = ""
    for char in sequence:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_sequence += binary_char
    return [binary_sequence[i:i+8] for i in range(0, len(binary_sequence), 8)]
