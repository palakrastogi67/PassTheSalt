# 🔐 PassTheSalt

**Your passwords, properly salted.**
*Because "password123" deserves better.*

A privacy-first, local-only password manager built from scratch in Python. No cloud sync, no third-party servers — your credentials are encrypted and stored entirely on your own machine.

---

## Why PassTheSalt?

Most people reuse weak passwords because remembering strong, unique ones for every account is hard. PassTheSalt solves this by:
- Generating strong, random passwords for you
- Encrypting everything with industry-standard cryptography
- Keeping your data local — nothing ever leaves your device

---

## Features

| Feature | Description |
|---|---|
| 🔑 Master password | One password to unlock the entire vault |
| 🧂 Argon2id key derivation | Memory-hard hashing, resistant to brute-force and GPU attacks |
| 🔒 AES-256-GCM encryption | Authenticated encryption — tampering or wrong passwords are detected, not silently accepted |
| ➕ Full CRUD | Add, search, edit, and delete saved credentials |
| 🎲 Password generator | Cryptographically secure random passwords |
| 📊 Strength checker | Scores password strength on length, digits, and case variety |
| 🚫 Zero plaintext storage | Passwords are never written to disk unencrypted |
| 🧪 Unit tested | Core crypto and vault logic covered with `pytest` |

---

## How It Works


1. You enter your master password.
2. Argon2id derives a secure 256-bit key from it (using a random salt, so no two vaults share a key even with the same password).
3. That key encrypts/decrypts your vault using AES-256-GCM.
4. The vault file on disk is just ciphertext — unreadable without the master password.

---

## Installation

```bash
git clone https://github.com/palakrastogi67/pass-the-salt.git
cd pass-the-salt

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

pip install -e ".[dev]"

## Author
Built by **Palak Rastogi**- A personal project to learn applied cryptography, secure software design and Python from the group up. 
