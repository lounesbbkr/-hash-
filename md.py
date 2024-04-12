import hashlib
import time

def calculate_md5_hash(data):
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    return md5_hash
    

# Example usage
data = input("Enter the text to hash: ")
start_time = time.time()
hash = calculate_md5_hash(data)
end_time = time.time()
execution_time = end_time - start_time
print(f"MD5 Hash: {hash}")
print(f"Execution Time: {execution_time} seconds")