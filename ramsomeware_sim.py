from cryptography.fernet import Fernet
import os

# Generate encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load existing encryption key
def load_key():
    return open("key.key", "rb").read()

# Encrypt all files in a directory
def encrypt_files(directory, key):
    fernet = Fernet(key)
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            continue  # Skip directories
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted_data = fernet.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted_data)
    print("[🔒] Files encrypted successfully!")

# Decrypt all files in a directory
def decrypt_files(directory, key):
    fernet = Fernet(key)
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            continue  # Skip directories
        with open(file_path, "rb") as f:
            encrypted_data = f.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path, "wb") as f:
            f.write(decrypted_data)
    print("[🔓] Files decrypted successfully!")

# Main function
if __name__ == "__main__":
    choice = input("Type 'encrypt' to lock files or 'decrypt' to unlock: ").strip().lower()
    directory = input("Enter directory path to target: ").strip()

    if not os.path.exists(directory):
        print("[❌] Invalid directory!")
        exit()

    if choice == "encrypt":
        generate_key()  # Generate key only during encryption
        key = load_key()
        encrypt_files(directory, key)
    elif choice == "decrypt":
        key = load_key()
        decrypt_files(directory, key)
    else:
        print("[❌] Invalid option! Use 'encrypt' or 'decrypt'.")
