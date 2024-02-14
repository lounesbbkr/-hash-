from ascii_calculation import calculate_ascii_sum
from text_to_bit import convert_sequence

# Get input from the user
user_input = input("Enter a text or a series of characters: ")
# Convert the input to bits
text_in_bit = convert_sequence(user_input)
# Calculate the ASCII sum
result = calculate_ascii_sum(user_input)

print("The ASCII sum of the input text is:", result)

print("The text in bit of the input text is:", text_in_bit )
