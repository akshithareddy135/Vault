import sqlite3

DB_NAME = "vault.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credentials(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,

            website TEXT NOT NULL,

            login_username TEXT NOT NULL,

            encrypted_password TEXT NOT NULL,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
        )
    """)

    conn.commit()

    conn.close()


# ==========================
# USER FUNCTIONS
# ==========================

def create_user(
        username,
        password_hash
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (
            username,
            password_hash
        )
        VALUES (?, ?)
        """,
        (
            username,
            password_hash
        )
    )

    conn.commit()

    conn.close()


def get_user(username):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ==========================
# CREDENTIAL FUNCTIONS
# ==========================

def add_credential(
        user_id,
        website,
        login_username,
        encrypted_password
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO credentials
        (
            user_id,
            website,
            login_username,
            encrypted_password
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            user_id,
            website,
            login_username,
            encrypted_password
        )
    )

    conn.commit()

    conn.close()


def get_credential(
        user_id,
        website
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM credentials
        WHERE user_id = ?
        AND website = ?
        """,
        (
            user_id,
            website
        )
    )

    credential = cursor.fetchone()

    conn.close()

    return credential


def get_all_credentials(
        user_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            website,
            login_username
        FROM credentials
        WHERE user_id = ?
        """,
        (user_id,)
    )

    records = cursor.fetchall()

    conn.close()

    return records


def delete_credential(
        user_id,
        website
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM credentials
        WHERE user_id = ?
        AND website = ?
        """,
        (
            user_id,
            website
        )
    )

    conn.commit()

    conn.close()