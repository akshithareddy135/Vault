import sqlite3

DB_NAME = "vault.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_password(website, username, password):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO passwords
        (website, username, password)
        VALUES (?, ?, ?)
        """,
        (website, username, password)
    )

    conn.commit()
    conn.close()


def get_password(website):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT website, username, password
        FROM passwords
        WHERE website = ?
        """,
        (website,)
    )

    result = cursor.fetchone()

    conn.close()

    return result


def delete_password(website):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM passwords
        WHERE website = ?
        """,
        (website,)
    )

    conn.commit()
    conn.close()


def list_passwords():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT website, username
        FROM passwords
        """
    )

    results = cursor.fetchall()

    conn.close()

    return results