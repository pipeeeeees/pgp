import gnupg

def generate_pgp_keys(email, passphrase):
    gpg = gnupg.GPG()
    input_data = gpg.gen_key_input(
        key_type="RSA",
        key_length=4096,
        name_email=email,
        passphrase=passphrase
    )
    key = gpg.gen_key(input_data)
    return key

def export_keys(key_id, output_file, passphrase):
    gpg = gnupg.GPG()
    public_key = gpg.export_keys(key_id)
    with open(output_file + "_public.asc", 'w') as f:
        f.write(public_key)
    print(f"Public key saved to {output_file}_public.asc")

    private_key = gpg.export_keys(key_id, secret=True, passphrase=passphrase)
    with open(output_file + "_private.asc", 'w') as f:
        f.write(private_key)
    print(f"Private key saved to {output_file}_private.asc")

    with open(output_file + "_key_id.txt", 'w') as f:
        f.write(key_id)
    print(f"Key ID saved to {output_file}_key_id.txt")

if __name__ == "__main__":
    email = input("Enter your email address: ")
    passphrase = input("Enter passphrase for your PGP key: ")
    output_file = input("Enter the base filename for the key files: ")

    key = generate_pgp_keys(email, passphrase)
    print("PGP keys generated successfully.")
    print(f"Filename is stored in {output_file}_key_id.txt")
    export_keys(key.fingerprint, output_file, passphrase)
