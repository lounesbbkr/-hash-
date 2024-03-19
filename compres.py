def xor_columns(bits):
    # Calculate the number of padding zeros needed
    padding_zeros = (256 - len(bits) % 256) % 256

    # Add padding zeros to the bits string
    bits += '0' * padding_zeros

    # Divide the bits string into lines of 256 bits
    lines = [bits[i:i+256] for i in range(0, len(bits), 256)]

    # Perform XOR between the elements of each column
    result = ""
    for i in range(256):
        column_bits = [line[i] for line in lines]
        column_xor = str(int(column_bits[0]))
        for j in range(1, len(column_bits)):
            column_xor = str(int(column_xor) ^ int(column_bits[j]))
        result += column_xor

    return result