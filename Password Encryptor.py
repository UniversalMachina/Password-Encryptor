def generate_key(master_password):
    password_chars = list(set(master_password))
    key = {}
    for i, char in enumerate(password_chars):
        key[char] = chr((ord(char) + i) % 256)
    return key

def generate_reverse_key(key):
    reverse_key = {}
    for k, v in key.items():
        reverse_key[v] = k
    return reverse_key

def encrypt_data(data, key):
    encrypted_data = ''
    for char in data:
        encrypted_data += key.get(char, char)
    return encrypted_data

def decrypt_data(encrypted_data, key):
    decrypted_data = ''
    for char in encrypted_data:
        decrypted_data += key.get(char, char)
    return decrypted_data

def main():
    master_password = input("Enter master password: ")
    data = "This is a sample text."

    key = generate_key(master_password)
    reverse_key = generate_reverse_key(key)

    encrypted_data = encrypt_data(data, key)
    print(f"Encrypted data: {encrypted_data}")

    decrypted_data = decrypt_data(encrypted_data, reverse_key)
    print(f"Decrypted data: {decrypted_data}")

if __name__ == "__main__":
    main()