from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


# ==========================
# GENERATE KEY
# ==========================

def generate_key():

    key = Fernet.generate_key()

    with open(
        KEY_FILE,
        "wb"
    ) as key_file:

        key_file.write(key)


# ==========================
# LOAD KEY
# ==========================

def load_key():

    if not os.path.exists(
            KEY_FILE
    ):

        generate_key()

    with open(
            KEY_FILE,
            "rb"
    ) as key_file:

        return key_file.read()


# ==========================
# ENCRYPT PASSWORD
# ==========================

def encrypt_password(
        password
):

    key = load_key()

    fernet = Fernet(
        key
    )

    encrypted_password = (
        fernet.encrypt(
            password.encode()
        )
    )

    return encrypted_password.decode()


# ==========================
# DECRYPT PASSWORD
# ==========================

def decrypt_password(
        encrypted_password
):

    key = load_key()

    fernet = Fernet(
        key
    )

    decrypted_password = (
        fernet.decrypt(
            encrypted_password.encode()
        )
    )

    return decrypted_password.decode()