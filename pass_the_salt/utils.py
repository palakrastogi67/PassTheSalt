import secrets
import string

def generate_password(length):
  characters= string.ascii_letters + string.digits + "!@#$%&*"

  password=""
  for i in range(length):
    password= password + secrets.choice(characters)
  return password
print(generate_password(12))

def password_strength(password):
  score=0
  if len(password)>=8:
    score=score+1
  if len(password)>=12:
    score=score+1
  if any(c.isdigit() for c in password):
    score=score+1
  if any(c.isupper() for c in password):
      score=score+1
  return score
print(password_strength("hello123"))