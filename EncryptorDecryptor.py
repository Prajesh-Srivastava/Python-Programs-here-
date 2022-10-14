# Encrypting & Decrypting strings in python

#First need to install cryptography package (pip install cryptography)
from cryptography.fernet import Fernet

# Generating a Key
key = Fernet.generate_key()
print("Key : ", key.decode())
f = Fernet(key)

# Encryption
encrypted_data = f.encrypt(b"Hola Open source Contributors!")
print("After encryption : ", encrypted_data)

# Decryption 
decrypted_data = f.decrypt(encrypted_data)
print(decrypted_data)
print("After decryption : ", decrypted_data.decode())
