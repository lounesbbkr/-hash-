from fonctions import (calculate_ascii_sum, 
                       convert_integer, get_next_32_numbers , next_generation ,
                       convert_bit_to_hex  , md_compres)
import time

def calculate_hash(text):
    sum_ascii = calculate_ascii_sum(text)
    serie_ascii = convert_integer(sum_ascii)
    les_32 = get_next_32_numbers(serie_ascii )
    hash_beta = md_compres(text , les_32) 
    hash_beta  = convert_bit_to_hex(hash_beta)
    sum_ascii = calculate_ascii_sum(hash_beta ) + sum_ascii
    serie_ascii = convert_integer(sum_ascii)
    les_32 = get_next_32_numbers(serie_ascii )
    hash = md_compres (hash_beta , les_32 )
    hash = next_generation(hash)
    hash  = convert_bit_to_hex(hash )
    return hash

text = input (":")
start_time = time.time()
hash = calculate_hash(text)
end_time = time.time()
execution_time = end_time - start_time
print("Hash:", hash)
print("Execution Time:", execution_time, "seconds")