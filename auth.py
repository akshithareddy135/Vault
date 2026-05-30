import bcrypt

from database import (
    create_user,
    get_user
)


# ==========================
# HASH PASSWORD
# ==========================

def hash_password(password):

    password_bytes = password.encode()

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(
        password_bytes,
        salt
    )

    return hashed_password.decode()


# ==========================
# VERIFY PASSWORD
# ==========================

def verify_password(
        password,
        password_hash
):

    return bcrypt.checkpw(
        password.encode(),
        password_hash.encode()
    )


# ==========================
# REGISTER USER
# ==========================

def register_user(
        username,
        password
):

    existing_user = get_user(
        username
    )

    if existing_user:

        return False

    password_hash = hash_password(
        password
    )

    create_user(
        username,
        password_hash
    )

    return True


# ==========================
# LOGIN USER
# ==========================

def login_user(
        username,
        password
):

    user = get_user(
        username
    )

    if not user:

        return None

    user_id = user[0]

    stored_hash = user[2]

    if verify_password(
            password,
            stored_hash
    ):

        return user_id

    return None