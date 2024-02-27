def calculate_ascii_sum(text):
    ascii_sum = 0
    for char in text:
        ascii_sum += ord(char)
    return ascii_sum

def convert_sequence_text_to_bit(sequence):
    binary_sequence = ""
    for char in sequence:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_sequence += binary_char
    return ''.join([binary_sequence[i:i+8] for i in range(0, len(binary_sequence), 8)])

def convert_integer(integer): 
    character_sequence = str(integer) 
    return ''.join(character_sequence)

def xor_bit_strings(bit_string1, bit_string2): 
    if len(bit_string1) < len(bit_string2):
        bit_string1 = bit_string1.zfill(len(bit_string2))
    elif len(bit_string2) < len(bit_string1):
        bit_string2 = bit_string2.zfill(len(bit_string1))
    
    result = "" 
    for bit1, bit2 in zip(bit_string1, bit_string2): 
        if bit1 == bit2:
            result += "0" 
        else: 
            result += "1" 
    return result
 
def convert_bit_to_base36(bit_string):
    decimal_sequence = []
    for i in range(0, len(bit_string), 8):
        binary_char = bit_string[i:i+8]
        decimal_number = int(binary_char, 2)
        decimal_sequence.append(decimal_number)
    
    base36_sequence = ""
    for decimal_number in decimal_sequence:
        base36_char = ""
        while decimal_number > 0:
            remainder = decimal_number % 36
            if remainder < 10:
                base36_char = str(remainder) + base36_char
            else:
                base36_char = chr(ord('A') + remainder - 10) + base36_char
            decimal_number //= 36
        base36_sequence += base36_char.zfill(1)  # Update zfill to 1 instead of 2
    
    return base36_sequence[:32]  # Return only the first 32 characters
