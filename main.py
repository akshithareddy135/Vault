import customtkinter as ctk

from tkinter import messagebox

from auth import verify_password

from database import (
    create_database,
    add_password,
    get_password,
    delete_password,
    list_passwords
)

create_database()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ===================================
# LOGIN
# ===================================

def login():

    password = login_password_entry.get()

    if verify_password(password):

        login_window.destroy()

        open_vault()

    else:

        messagebox.showerror(
            "Error",
            "Invalid Master Password"
        )


# ===================================
# VAULT WINDOW
# ===================================

def open_vault():

    vault = ctk.CTk()

    vault.title("Vault Password Manager")

    vault.geometry("700x650")

    # -----------------------
    # FUNCTIONS
    # -----------------------

    def add_credential():

        website = website_entry.get()

        username = username_entry.get()

        password = password_entry.get()

        if not website or not username or not password:

            messagebox.showerror(
                "Error",
                "Fill all fields"
            )

            return

        add_password(
            website,
            username,
            password
        )

        messagebox.showinfo(
            "Success",
            "Password Saved"
        )

    def view_credential():

        website = website_entry.get()

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
                "Error",
                "Credential Not Found"
            )

    def delete_credential():

        website = website_entry.get()

        delete_password(website)

        messagebox.showinfo(
            "Deleted",
            "Credential Removed"
        )

    def show_all():

        output_box.delete(
            "1.0",
            "end"
        )

        records = list_passwords()

        for website, username in records:

            output_box.insert(
                "end",
                f"{website} | {username}\n"
            )

    # -----------------------
    # UI
    # -----------------------

    title = ctk.CTkLabel(
        vault,
        text="Vault Password Manager",
        font=("Arial", 28, "bold")
    )

    title.pack(pady=20)

    website_entry = ctk.CTkEntry(
        vault,
        width=400,
        placeholder_text="Website"
    )

    website_entry.pack(pady=10)

    username_entry = ctk.CTkEntry(
        vault,
        width=400,
        placeholder_text="Username"
    )

    username_entry.pack(pady=10)

    password_entry = ctk.CTkEntry(
        vault,
        width=400,
        placeholder_text="Password"
    )

    password_entry.pack(pady=10)

    ctk.CTkButton(
        vault,
        text="Add Password",
        command=add_credential
    ).pack(pady=5)

    ctk.CTkButton(
        vault,
        text="View Password",
        command=view_credential
    ).pack(pady=5)

    ctk.CTkButton(
        vault,
        text="Delete Password",
        command=delete_credential
    ).pack(pady=5)

    ctk.CTkButton(
        vault,
        text="List Websites",
        command=show_all
    ).pack(pady=5)

    output_box = ctk.CTkTextbox(
        vault,
        width=500,
        height=200
    )

    output_box.pack(pady=20)

    vault.mainloop()


# ===================================
# LOGIN WINDOW
# ===================================

login_window = ctk.CTk()

login_window.title("Vault Login")

login_window.geometry("400x250")

title = ctk.CTkLabel(
    login_window,
    text="Vault Login",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)

login_password_entry = ctk.CTkEntry(
    login_window,
    width=250,
    placeholder_text="Master Password",show="*"
)

login_password_entry.pack(pady=10)

ctk.CTkButton(
    login_window,
    text="Login",
    command=login
).pack(pady=20)

login_window.mainloop()