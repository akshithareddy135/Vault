import customtkinter as ctk
from tkinter import messagebox

from database import (
    create_database,
    add_password,
    get_password,
    delete_password,
    list_passwords
)

# -----------------------------
# INITIAL SETUP
# -----------------------------

create_database()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Vault Password Manager")
app.geometry("700x650")

# -----------------------------
# CONTROLLER FUNCTIONS
# -----------------------------

def add_credential():

    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not username or not password:
        messagebox.showerror(
            "Error",
            "Please fill all fields"
        )
        return

    add_password(
        website,
        username,
        password
    )

    messagebox.showinfo(
        "Success",
        "Credential Saved"
    )

    clear_fields()


def view_credential():

    website = website_entry.get().strip()

    if not website:
        messagebox.showerror(
            "Error",
            "Enter website name"
        )
        return

    result = get_password(website)

    if result:

        messagebox.showinfo(
            "Credential Found",
            f"Website: {result[0]}\n"
            f"Username: {result[1]}\n"
            f"Password: {result[2]}"
        )

    else:

        messagebox.showerror(
            "Not Found",
            "Credential does not exist"
        )


def delete_credential():

    website = website_entry.get().strip()

    if not website:
        messagebox.showerror(
            "Error",
            "Enter website name"
        )
        return

    delete_password(website)

    messagebox.showinfo(
        "Deleted",
        f"{website} removed"
    )

    clear_fields()


def show_credentials():

    records = list_passwords()

    output_box.delete(
        "1.0",
        "end"
    )

    if not records:

        output_box.insert(
            "end",
            "Vault is empty."
        )

        return

    for website, username in records:

        output_box.insert(
            "end",
            f"Website: {website}\n"
            f"Username: {username}\n"
            f"{'-'*40}\n"
        )


def clear_fields():

    website_entry.delete(0, "end")
    username_entry.delete(0, "end")
    password_entry.delete(0, "end")


# -----------------------------
# TITLE
# -----------------------------

title_label = ctk.CTkLabel(
    app,
    text="🔐 Vault Password Manager",
    font=("Arial", 28, "bold")
)

title_label.pack(pady=20)

# -----------------------------
# INPUT SECTION
# -----------------------------

website_entry = ctk.CTkEntry(
    app,
    width=400,
    placeholder_text="Website"
)

website_entry.pack(pady=10)

username_entry = ctk.CTkEntry(
    app,
    width=400,
    placeholder_text="Username"
)

username_entry.pack(pady=10)

password_entry = ctk.CTkEntry(
    app,
    width=400,
    placeholder_text="Password"
)

password_entry.pack(pady=10)

# -----------------------------
# BUTTONS
# -----------------------------

add_button = ctk.CTkButton(
    app,
    text="Add Password",
    command=add_credential
)

add_button.pack(pady=5)

view_button = ctk.CTkButton(
    app,
    text="View Password",
    command=view_credential
)

view_button.pack(pady=5)

delete_button = ctk.CTkButton(
    app,
    text="Delete Password",
    command=delete_credential
)

delete_button.pack(pady=5)

list_button = ctk.CTkButton(
    app,
    text="List Saved Websites",
    command=show_credentials
)

list_button.pack(pady=5)

# -----------------------------
# OUTPUT BOX
# -----------------------------

output_label = ctk.CTkLabel(
    app,
    text="Stored Credentials"
)

output_label.pack(pady=(20, 5))

output_box = ctk.CTkTextbox(
    app,
    width=550,
    height=220
)

output_box.pack(pady=10)

# -----------------------------
# START APP
# -----------------------------

app.mainloop()