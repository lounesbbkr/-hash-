def get_next_32_numbers(sequence):
    def read_sequence_from_file(filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError:
            print("File not found.")
            yield ""

    def find_sequence_in_file(user_sequence, filename):
        user_sequence = ''.join(user_sequence)  # Convert list to string
        for file_sequence in read_sequence_from_file(filename):
            if not file_sequence:
                return None
            if user_sequence in file_sequence:
                index = file_sequence.index(user_sequence)
                sequence_end = index + len(user_sequence)
                next_32_numbers = file_sequence[sequence_end:sequence_end + 32]
                return next_32_numbers
        return None

    filename = "base_pi.txt"
    next_32_numbers = find_sequence_in_file(sequence, filename)
    return next_32_numbers