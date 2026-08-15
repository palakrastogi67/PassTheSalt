import os
from argon2.low_level import hash_secret_raw, Type
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
SALT_SIZE=16
KEY_SIZE=32

def new_salt():
  return os.urandom(SALT_SIZE)

def derive_key(master_password, salt):
  key=hash_secret_raw(
    secret=master_password.encode("utf-8"),
    salt=salt,
    time_cost=3,
    memory_cost=65536,
    parallelism=4,
    hash_len=KEY_SIZE,
    type=Type.ID,
  )
  return key

def encrypt(plaintext,key):
  aesgcm=AESGCM(key)
  nonce= os.urandom(12)
  ciphertext= aesgcm.encrypt(nonce,plaintext, None)
  return nonce + ciphertext

def decrypt(blob,key):
  aesgcm=AESGCM(key)
  nonce=blob[:12]
  ciphertext= blob[12:]
  plaintext=aesgcm.decrypt(nonce,ciphertext,None)
  return plaintext


salt=new_salt()
key=derive_key("mypassword123",salt)
print("Key:",key)

encrypted= encrypt(b"secret data", key)
print("Encrypted:", encrypted)

decrypted= decrypt(encrypted, key)
print("Decrypted:", decrypted)
