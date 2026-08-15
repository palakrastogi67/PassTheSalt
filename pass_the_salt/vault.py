import json
from pathlib import Path
try:
  from . import crypto
except ImportError:
  import crypto

VAULT_MAGIC= b"PTS1"

class Vault:
  def __init__(self,path,key,entries):
    self.path=Path(path)
    self.key=key
    self.entries=entries
  @classmethod
  def create(cls,path,master_password):
    salt=crypto.new_salt()
    key=crypto.derive_key(master_password,salt)
    entries={}
    vault=cls(path,key,entries)
    vault._write(salt)
    return vault
  def _write(self,salt):
    plaintext=json.dumps(self.entries).encode("utf-8")
    blob=crypto.encrypt(plaintext,self.key)
    self.path.write_bytes(VAULT_MAGIC + salt + blob)
  @classmethod
  def unlock(cls,path,mymasterpassword):
    path=Path(path)
    raw=path.read_bytes()
    salt=raw[4:4+crypto.SALT_SIZE]
    blob=raw[4+ crypto.SALT_SIZE:]
    key=crypto.derive_key(mymasterpassword,salt)
    plaintext=crypto.decrypt(blob,key)
    entries=json.loads(plaintext.decode("utf-8"))
    return cls(path,key,entries)
  def add_entry(self,service,username,password,notes=""):
    entry_id= service.lower()
    self.entries[entry_id]={
      "service":service,
      "username": username,
      "password":password,
      "notes":notes,
    }
    self.save()
  def save(self):
    raw=self.path.read_bytes()
    salt=raw[4:4+ crypto.SALT_SIZE]
    self._write(salt)

  def search(self,query):
    results={}
    for entry_id in self.entries:
      entry=self.entries[entry_id]
      if query.lower() in entry_id or query.lower() in entry["username"].lower():
        results[entry_id]=entry
      return results
  def delete_entry(self, entry_id):
    del self.entries[entry_id]
    self.save()


v= Vault("myfile.txt", b"somekey", {})
print(v.path)
print(v.key)
print(v.entries) 

v=Vault.create("test_vault.pts","mymasterpassword")
print("Vault created at:",v.path)
print("Entries:", v.entries)

v2=Vault.unlock("test_vault.pts","mymasterpassword")
print("Unlocked entries:",v2.entries)

try:
  v3=Vault.unlock("test_vault.pts","wrongpassword")
  print("Unlocked entries:",v3.entries)
except Exception as e:
  print("Error:",e)

v4=Vault.unlock("test_vault.pts","mymasterpassword")
v4.add_entry("Gmail", "me@gmail.com", "mypassword123")
print("After adding:", v4.entries)
results=v4.search("gmail")
print("Search results:", results)

v4.delete_entry("gmail")
print("After delete:", v4.entries)

