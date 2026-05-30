import secrets
import string


# ==========================
# GENERATE PASSWORD
# ==========================

def generate_password(
        length=16
):

    lowercase = (
        string.ascii_lowercase
    )

    uppercase = (
        string.ascii_uppercase
    )

    digits = (
        string.digits
    )

    symbols = (
        "!@#$%^&*()_+-=[]{}"
    )

    all_characters = (
        lowercase +
        uppercase +
        digits +
        symbols
    )

    password = "".join(

        secrets.choice(
            all_characters
        )

        for _ in range(length)
    )

    return password


# ==========================
# CHECK PASSWORD STRENGTH
# ==========================

def check_strength(
        password
):

    score = 0

    if len(password) >= 12:
        score += 1

    if any(
            c.isupper()
            for c in password
    ):
        score += 1

    if any(
            c.islower()
            for c in password
    ):
        score += 1

    if any(
            c.isdigit()
            for c in password
    ):
        score += 1

    if any(
            c in "!@#$%^&*()_+-=[]{}"
            for c in password
    ):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"