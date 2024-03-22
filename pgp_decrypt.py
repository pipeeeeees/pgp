"""
pgp_decrypt.py

This script demonstrates how to decrypt a PGP-encrypted message using the gnupg library in Python.
"""

import gnupg

def decrypt_message(encrypted_message, passphrase):
    gpg = gnupg.GPG()
    decrypted_data = gpg.decrypt(encrypted_message, passphrase=passphrase)
    return str(decrypted_data)

if __name__ == "__main__":
    encrypted_message_file = "encrypted_message.asc"
    passphrase = "oscarandpepper"
    with open(encrypted_message_file, 'r') as f:
        encrypted_message = f.read()
    
    decrypted_message = decrypt_message(encrypted_message, passphrase)
    print("Decrypting message...")
    print("Decrypted message:")
    print(decrypted_message)