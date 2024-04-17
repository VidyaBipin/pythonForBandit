from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_des(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), DES.block_size)
    encrypted_data = cipher.encrypt(padded_plaintext)
    return encrypted_data

# Example usage
key = b'01234567'  # DES key must be 8 bytes long
plaintext = "Hello, DES!"

encrypted_data = encrypt_des(key, plaintext)
print("Encrypted:", encrypted_data.hex())
