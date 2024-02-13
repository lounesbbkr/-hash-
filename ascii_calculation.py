def calculate_ascii_sum(text):
    ascii_sum = 0
    for char in text:
        ascii_sum += ord(char)
    return ascii_sum
