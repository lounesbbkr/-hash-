def xor_bits(char1, char2):
    # Convertir les caractères en bits
    bits1 = bin(ord(char1))[2:]
    bits2 = bin(ord(char2))[2:]

    # Remplir les bits avec des zéros à gauche pour avoir la même longueur
    max_length = max(len(bits1), len(bits2))
    bits1 = bits1.zfill(max_length)
    bits2 = bits2.zfill(max_length)

    # Effectuer le XOR entre les bits
    xor_result = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(bits1, bits2))

    return xor_result

# Tester le XOR entre '0' et les lettres de l'alphabet
for letter in range(ord('a'), ord('z')+1):
    result = xor_bits('1', chr(letter))
    decimal_result = int(result, 2)
    final_result = decimal_result % 36
    print(f"Résultat du XOR des bits entre '1' et '{chr(letter)}' en décimal (modulo 36) : {final_result}")
