import os

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

keys = get_random_bytes(16)
salt = b'%s' % keys
password = os.environ.get('MY_PASSWORD')

key = PBKDF2(password, salt, dkLen=32)

# bring content from file and encrypt it
with open('my_passwords.json', 'rb') as file_in:
    message = file_in.read()

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('encrypted.bin', 'wb') as file_out:
    file_out.write(cipher.iv)
    file_out.write(ciphered_data)

with open('encrypted.bin', 'rb') as file_in:
    iv = file_in.read(16)
    ciphered_data = file_in.read()

with open('key.bin', 'wb') as file_out:
    file_out.write(key)


