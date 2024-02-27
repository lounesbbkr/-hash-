from fonctions import calculate_ascii_sum
from fonctions import convert_sequence_text_to_bit
from fonctions import convert_integer
from fonctions import xor_bit_strings
from fonctions import convert_bit_to_base36
from search_sequence import get_next_32_numbers

# Get input from the user
text = input("Enter a text or a series of characters: ")
# Convert the input to bits
text_in_bit = convert_sequence_text_to_bit(text)
# Calculate the ASCII sum
sum_ascii = calculate_ascii_sum(text)
# Convert the
serie_ascii = convert_integer(sum_ascii)

les_32 = get_next_32_numbers(serie_ascii)

les_32_en_bits = convert_sequence_text_to_bit(les_32)

xor_rslt = xor_bit_strings(text_in_bit, les_32_en_bits)

hash = convert_bit_to_base36(xor_rslt)

print("The ASCII sum of the input text is:", sum_ascii)
print("The text in bit of the input text is:", text_in_bit )
print("The next 32 are:", les_32 )
print("The next 32 in bits are:", les_32_en_bits )
print("The xor rsult :", xor_rslt )
print("The hash is:", hash)
