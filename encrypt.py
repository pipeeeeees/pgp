import cryption

if __name__ == '__main__':
    input_message = input("Enter the message you want to encrypt: ")
    passphrase = input("Enter the passphrase for your private key: ")
    encrypted_message = cryption.encrypt_message(input_message, passphrase)
    print(f"Encrypted message: {encrypted_message}")