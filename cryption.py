"""
encrypt.py

This module provides functions for encrypting my messages with pgp

My key ID is stored in `dpipes public credentials/dpipes_key_id.txt`
My public key is stored in `dpipes public credentials/dpipes_public.asc`
My private key is stored in `dpipes private credentials/dpipes_private.asc`
"""

import gnupg

def encrypt_message(message, key_id):
    gpg = gnupg.GPG()
    encrypted_data = gpg.encrypt(message, key_id)
    return str(encrypted_data)

def decrypt_message(encrypted_message, passphrase):
    gpg = gnupg.GPG()
    decrypted_data = gpg.decrypt(encrypted_message, passphrase=passphrase)
    return str(decrypted_data)

if __name__ == "__main__":
    key_id = open("dpipes public credentials/dpipes_key_id.txt").read()
    message = input("Enter the message you want to encrypt: ")
    encrypted_message = encrypt_message(message, key_id)
    print(f"Encrypted message: {encrypted_message}")

    passphrase = input("Enter the passphrase for your private key: ")
    decrypted_message = decrypt_message(encrypted_message, passphrase)
    print(f"Decrypted message: {decrypted_message}")