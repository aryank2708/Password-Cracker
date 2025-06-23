import hashlib
import itertools
import string
import time

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def dictionary_attack(target_hash, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            for word in file:
                word = word.strip()
                if md5_hash(word) == target_hash:
                    return word
        return None
    except FileNotFoundError:
        print("Wordlist file not found.")
        return None

def brute_force_attack(target_hash, max_length=4):
    chars = string.ascii_lowercase + string.digits
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            word = ''.join(guess)
            if md5_hash(word) == target_hash:
                return word
    return None

def main():
    print("=== Password Hash Cracker ===")
    target_hash = input("Enter the MD5 hash: ")
    mode = input("Choose mode (dictionary/brute): ").strip().lower()

    start_time = time.time()

    if mode == 'dictionary':
        wordlist_file = input("Enter path to wordlist file (e.g., wordlist.txt): ")
        result = dictionary_attack(target_hash, wordlist_file)
    elif mode == 'brute':
        max_len = int(input("Enter maximum password length (recommended ≤ 4): "))
        result = brute_force_attack(target_hash, max_len)
    else:
        print("Invalid mode selected.")
        return

    end_time = time.time()

    if result:
        print(f"[✓] Password found: {result}")
    else:
        print("[✗] Password not found.")

    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    main()
