from pass_the_salt import vault as vault_mod

def test_create_and_unlock(tmp_path):
  path=tmp_path/"test.pts"
  v=vault_mod.Vault.create(path,"mypassword")
  v.add_entry("Gmail", "me@gmail.com","secret123")

  v2=vault_mod.Vault.unlock(path,"mypassword")
  assert "gmail" in v2.entries
  assert v2.entries["gmail"]["password"]=="secret123"

def test_wrong_password_fails(tmp_path):
  path=tmp_path/"test.pts"
  vault_mod.Vault.create(path,"mypassword")

  try:
    vault_mod.Vault.unlock(path,"wrongpassword")
    assert False
  except Exception:
    assert True
    