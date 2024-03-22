import cryption

if __name__ == '__main__':
    input_message = input("Enter the message you want to decrypt: ")
    passphrase = input("Enter the passphrase for your private key: ")
    decrypted_message = cryption.decrypt_message(input_message, passphrase)
    print(f"Decrypted message: {decrypted_message}")