#Md5
import hashlib
from pprint import pprint
import binascii

# AES
from cryptography.fernet import Fernet
# RSA
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

secret = "This is the Secret Password"
bsecret = secret.encode(
)  # turn it into a binary string by using the encode method.
m = hashlib.md5()
m.update(bsecret)
hash = m.digest()
pprint(hash)

hash = binascii.b2a_hex(hash)
pprint(hash)

# Fernet AES
key = Fernet.generate_key()
print(key)

# create the Fernet object
f = Fernet(key)
message_to_send = b'This is the Super Secret'

encrypted = f.encrypt(message_to_send)
print(encrypted)

# No send encrypted to someone you want here
# You can decrypt the data using a Fernet object created with the same key:
f = Fernet(key)
message_received = f.decrypt(encrypted)
print(message_received)

# RSA
private_key = rsa.generate_private_key(public_exponent=65537,
                                       key_size=4096,
                                       backend=default_backend())
pprint(private_key)
public_key = private_key.public_key()
pprint(public_key)

more_message_to_send = b"More secrets to Tell"

encrypted = public_key.encrypt(
    more_message_to_send,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=None))


# send encrypted
pprint(encrypted)

decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=None))

pprint(decrypted)
