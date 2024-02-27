from fonctions import calculate_ascii_sum
from fonctions import convert_sequence
from fonctions import convert_integer
from search_sequence import get_next_32_numbers

# Get input from the user
text = input("Enter a text or a series of characters: ")
# Convert the input to bits
text_in_bit = convert_sequence(text)
# Calculate the ASCII sum
sum_ascii = calculate_ascii_sum(text)
# Convert the
serie_ascii = convert_integer(sum_ascii)
les_32 = get_next_32_numbers(serie_ascii)

print("The ASCII sum of the input text is:", sum_ascii)
print("The text in bit of the input text is:", text_in_bit )
print("The next 32 are:", les_32 )
print(get_next_32_numbers(serie_ascii))