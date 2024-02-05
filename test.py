import gnupg

def encrypt_message(message, recipient_key_id):
    gpg = gnupg.GPG()
    encrypted_data = gpg.encrypt(message, recipient_key_id)
    return str(encrypted_data)

def decrypt_message(encrypted_message, passphrase):
    gpg = gnupg.GPG()
    decrypted_data = gpg.decrypt(encrypted_message, passphrase=passphrase)
    return str(decrypted_data)

if __name__ == "__main__":
    recipient_key_id = input("Enter the recipient's key ID: ")
    passphrase = input("Enter your passphrase for the private key: ")
    message = input("Enter the message you want to encrypt: ")

    encrypted_message = encrypt_message(message, recipient_key_id)
    print("Message encrypted successfully.")
    print("Encrypted message:")
    print(encrypted_message)

    decrypted_message = decrypt_message(encrypted_message, passphrase)
    print("\nDecrypting message...")
    print("Decrypted message:")
    print(decrypted_message)
