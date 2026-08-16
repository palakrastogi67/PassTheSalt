from pathlib import Path
from getpass import getpass

from.import vault as vault_mod
from.import utils

DEFAULT_VAULT_PATH= "myvault.pts"

print("Welcome to PassTheSalt!")
master_password=getpass("Enter your Master Password:")

if Path(DEFAULT_VAULT_PATH).exists():
  v=vault_mod.Vault.unlock(DEFAULT_VAULT_PATH,master_password)
  print("Vault unlocked.")
else:
  label, score= utils.password_strength(master_password)
  print ("Master password strength:",label, "("+ str(score)+ "/4)")
  if score<2:
    confirm=input("This is a weak password. Continue anyway? (y/n):")
    if confirm !="y":
      exit()

  v=vault_mod.Vault.create(DEFAULT_VAULT_PATH,master_password)
  print("New Vault created.")

while True:
  command=input("\nCommand (add/search/delete/list/exit/edit):")

  if command=="exit":
      print ("Goodbye!")
      break

  elif command=="add":
    service=input("Service name:")
    username=input("Enter your Username:")
    user_generated= input("Generate a strong password? (y/n):")
    if user_generated=="y":
      password=utils.generate_password(16)
      print("Generated Password:", password)
    else:
      password=input("Enter your Password:") 
    v.add_entry(service,username,password)
    print("Entry added.")

  elif command=="search":
    query=input("Search for:")
    results=v.search(query)
    print("Results:", results)

  elif command=="delete":
    entry_id=input("Entry ID to delete:")
    v.delete_entry(entry_id)
    print("Entry deleted.")
  
  elif command=="edit":
    entry_id=input("Enter ID to edit:")
    if entry_id not in v.entries:
      print("Entry not found.")
    else:
      new_username= input("New username (leave blank to keep same):")
      new_password= input("New password (leave blank to keep same):")
      if new_username!="":
        v.entries[entry_id]["username"]= new_username
      if new_password!= "":
        v.entries[entry_id]["password"]=new_password
      v.save()
      print("Entry updated.")

  elif command=="list":
       print("All entries:", v.entries)

  else:
    print("Unknown command. Try: add/search/delete/list/exit")
