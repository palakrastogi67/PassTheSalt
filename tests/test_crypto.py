from pass_the_salt import crypto

def test_encrypt_decrypt():
  salt= crypto.new_salt()
  key= crypto.derive_key("mypassword",salt)
  encrypted=crypto.encrypt(b"hello world",key)
  decrypted=crypto.decrypt(encrypted,key)
  assert decrypted==b"hello world"
  