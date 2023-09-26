import pprint

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

print("=" * 50)
print('''
  Welcome to my first python cryptography project.
  Here are the passwords you have saved:      
''')
print("=" * 50)
print("\n" * 2)

with open('../python/key.bin', 'rb') as key_file:
    key = key_file.read()
  
with open('../python/encrypted.bin', 'rb') as file_in:
    iv = file_in.read(16)
    ciphered_data = file_in.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
original = unpad(cipher.decrypt(ciphered_data), AES.block_size)

original = original.decode('utf-8').replace("\n", ' ').replace("'", "")
pprint.pprint(original)
