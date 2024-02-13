def read_sequence_from_file(filename):
    try:
        with open(filename, 'r') as file:
            sequence = file.read().strip()  # Reading the entire file as a single string
            return sequence
    except FileNotFoundError:
        print("File not found.")
        return ""

def sequence_exists_in_file(user_sequence, filename):
    file_sequence = read_sequence_from_file(filename)
    if not file_sequence:
        return False
    if user_sequence in file_sequence:  # Checking if user_sequence is a substring of file_sequence
        index = file_sequence.index(user_sequence)
        next_32_numbers = file_sequence[index + len(user_sequence):index + len(user_sequence) + 32]
        return next_32_numbers
    else:
        return ""

if __name__ == "__main__":
    filename = "pi_file.txt"  # Using fixed filename 'pi_file.txt'
    user_sequence = input("Enter the sequence to verify: ").strip()
    
    next_32_numbers = sequence_exists_in_file(user_sequence, filename)
    if next_32_numbers:
        print("The provided sequence exists in the file.")
        print("The next 32 numbers are:", next_32_numbers)
    else:
        print("The provided sequence does not exist in the file.")
