from fonctions import (calculate_ascii_sum, convert_sequence_text_to_bit, 
                       convert_integer, xor_bit_strings, 
                       convert_bit_to_hex, shift_string)
from search_sequence import get_next_32_numbers
from compres import xor_columns

# Get input from the user
text = input("   : ")
# Convert the input to bits
text_in_bit = convert_sequence_text_to_bit(text)
# Calculate the ASCII sum
sum_ascii = calculate_ascii_sum(text)
# Convert 
serie_ascii = convert_integer(sum_ascii)
# Get the next 32 numbers
les_32 = get_next_32_numbers(serie_ascii)
# Convert the next 32 numbers to bits
les_32_en_bits = convert_sequence_text_to_bit(les_32)

# Check if the length of the input text is greater than 32
if len(text) > 32:
    # Perform XOR between the columns of the input text
    text_in_bit = xor_columns(text_in_bit)
    xor_rslt = xor_bit_strings(text_in_bit, les_32_en_bits)
else:
# Perform XOR between the input text and the next 32 numbers
    xor_rslt = xor_bit_strings(text_in_bit, les_32_en_bits)

# convert the result to hex
hash = convert_bit_to_hex(xor_rslt)

shift = shift_string(text, 10)

#print("The ASCII sum of the input text is:", sum_ascii)
#print("The text in bit of the input text is:", text_in_bit )
#print("The next 32 are:", les_32 )
#print("The next 32 in bits are:", les_32_en_bits )
#print("The xor rsult :", xor_rslt )
print("The shift is:", shift)
print("The hash is:", hash)
