from fonctions import (calculate_ascii_sum, 
                       convert_integer, get_next_32_numbers , next_generation ,
                       convert_bit_to_hex  , md_compres)
import time

def calculate_hash(text):
    sum_ascii = calculate_ascii_sum(text)
    print("sum_ascii : ", sum_ascii)
    serie_ascii = convert_integer(sum_ascii)
    les_32 = get_next_32_numbers(serie_ascii )
    print("les_32 de π : ", les_32)
    hash_beta = md_compres(text , les_32) 
    hash_beta  = convert_bit_to_hex(hash_beta)
    print("hash_beta : ", hash_beta)
    print("Re-hashing ")
    sum_ascii = calculate_ascii_sum(hash_beta ) + sum_ascii
    serie_ascii = convert_integer(sum_ascii)
    print("sum_ascii : ", sum_ascii)
    les_32 = get_next_32_numbers(serie_ascii )
    print("les_32 de π : ", les_32)
    hash = md_compres (hash_beta , les_32 )
    hash_3 = convert_bit_to_hex(hash )
    print("hash with out  next_generation : ", hash_3)
    hash = next_generation(hash)
    hash  = convert_bit_to_hex(hash )
    return hash

text = input (":")
start_time = time.time()
hash = calculate_hash(text)
end_time = time.time()
execution_time = end_time - start_time
print("Real Hash:", hash)
print("Execution Time:", execution_time, "seconds")