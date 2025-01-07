from cryptography.fernet import Fernet
import os

# Fungsi untuk membuat kunci enkripsi
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Kunci berhasil dibuat dan disimpan ke 'key.key'.")

# Fungsi untuk memuat kunci
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Kunci tidak ditemukan. Buat kunci baru terlebih dahulu.")
        return None

# Fungsi untuk mengenkripsi file
def encrypt_file(file_path):
    key = load_key()
    if key is None:
        return
    
    fernet = Fernet(key)
    
    with open(file_path, "rb") as file:
        original_data = file.read()
    
    encrypted_data = fernet.encrypt(original_data)
    encrypted_path = file_path.replace("original", "encrypted")
    
    os.makedirs(os.path.dirname(encrypted_path), exist_ok=True)
    with open(encrypted_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    print(f"File '{file_path}' berhasil dienkripsi ke '{encrypted_path}'.")

# Fungsi untuk mendekripsi file
def decrypt_file(file_path):
    key = load_key()
    if key is None:
        return
    
    fernet = Fernet(key)
    
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        decrypted_path = file_path.replace("encrypted", "decrypted")
        
        os.makedirs(os.path.dirname(decrypted_path), exist_ok=True)
        with open(decrypted_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
        
        print(f"File '{file_path}' berhasil didekripsi ke '{decrypted_path}'.")
    except Exception as e:
        print(f"Error saat mendekripsi file: {e}")

# Menu interaktif
if __name__ == "__main__":
    print("Pilih opsi:")
    print("1. Buat Kunci")
    print("2. Enkripsi File")
    print("3. Dekripsi File")
    
    choice = input("Masukkan pilihan (1/2/3): ")
    
    if choice == "1":
        generate_key()
    elif choice == "2":
        file_path = input("Masukkan path file yang akan dienkripsi: ")
        encrypt_file(file_path)
    elif choice == "3":
        file_path = input("Masukkan path file yang akan didekripsi: ")
        decrypt_file(file_path)
    else:
        print("Pilihan tidak valid.")
