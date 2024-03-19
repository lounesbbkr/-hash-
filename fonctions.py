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
 
def convert_bit_to_hex(bit_string):
    decimal_sequence = []
    for i in range(0, len(bit_string), 8):
        binary_char = bit_string[i:i+8]
        decimal_number = int(binary_char, 2)
        decimal_sequence.append(decimal_number)
    
    hex_sequence = ""
    for decimal_number in decimal_sequence:
        hex_char = hex(decimal_number)[2:].zfill(2)
        hex_sequence += hex_char
    
    return hex_sequence[:64]  

def shift_string(chaine, decalage):
    decalage = decalage % len(chaine)
    return chaine[-decalage:] + chaine[:-decalage]