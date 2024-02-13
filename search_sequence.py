def search_sequence_in_file(pi, search_sequence):
    with open(pi.txt, 'r') as big_file:
        big_sequence = big_file.read().split()
        big_sequence = [int(num) for num in big_sequence]

    # Convert the search sequence string to a list of integers
    search_sequence = [int(num) for num in search_sequence.split()]

    # Iterate through the big sequence with a sliding window
    for i in range(len(big_sequence) - len(search_sequence) + 1):
        window = big_sequence[i:i + len(search_sequence)]
        if window == search_sequence:
            print("Sequence found starting at index:", i)
            return

    print("Sequence not found in the big sequence.")

# Example usage:
big_sequence_filename = 'big_sequence.txt'
search_sequence = input("Enter the sequence of numbers you want to search for (space-separated): ")
search_sequence_in_file(big_sequence_filename, search_sequence)
