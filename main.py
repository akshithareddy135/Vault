import customtkinter as ctk

from tkinter import (
    messagebox,
    simpledialog
)

from database import (
    create_database,
    add_credential,
    get_credential,
    get_all_credentials,
    delete_credential
)

from auth import (
    register_user,
    login_user
)

from crypto import (
    encrypt_password,
    decrypt_password
)

from password_generator import (
    generate_password
)

# ==========================================
# INITIAL SETUP
# ==========================================

create_database()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

current_user_id = None


# ==========================================
# DASHBOARD FUNCTIONS
# ==========================================

def refresh_credentials():

    credential_box.delete(
        "1.0",
        "end"
    )

    records = get_all_credentials(
        current_user_id
    )

    for website, username in records:

        credential_box.insert(
            "end",
            f"{website} | {username}\n"
        )


def add_new_credential():

    website = website_entry.get().strip()

    username = username_entry.get().strip()

    password = password_entry.get().strip()

    if not website or not username or not password:

        messagebox.showerror(
            "Error",
            "Fill all fields"
        )

        return

    encrypted_password = (
        encrypt_password(password)
    )

    add_credential(
        current_user_id,
        website,
        username,
        encrypted_password
    )

    messagebox.showinfo(
        "Success",
        "Credential Saved"
    )

    website_entry.delete(0, "end")
    username_entry.delete(0, "end")
    password_entry.delete(0, "end")

    refresh_credentials()


def view_credential_gui():

    website = simpledialog.askstring(
        "View Credential",
        "Enter Website"
    )

    if not website:
        return

    record = get_credential(
        current_user_id,
        website
    )

    if not record:

        messagebox.showerror(
            "Error",
            "Credential Not Found"
        )

        return

    decrypted_password = (
        decrypt_password(
            record[4]
        )
    )

    messagebox.showinfo(
        "Credential Found",
        f"Website: {record[2]}\n\n"
        f"Username: {record[3]}\n\n"
        f"Password: {decrypted_password}"
    )


def delete_credential_gui():

    website = simpledialog.askstring(
        "Delete Credential",
        "Enter Website"
    )

    if not website:
        return

    delete_credential(
        current_user_id,
        website
    )

    refresh_credentials()

    messagebox.showinfo(
        "Deleted",
        "Credential Removed"
    )


def generate_new_password():

    generated = generate_password()

    password_entry.delete(
        0,
        "end"
    )

    password_entry.insert(
        0,
        generated
    )


# ==========================================
# DASHBOARD WINDOW
# ==========================================

def open_dashboard():

    global website_entry
    global username_entry
    global password_entry
    global credential_box

    login_window.destroy()

    dashboard = ctk.CTk()

    dashboard.title(
        "Vault Password Manager"
    )

    dashboard.geometry(
        "800x700"
    )

    title = ctk.CTkLabel(
        dashboard,
        text="🔐 Vault Password Manager",
        font=("Arial", 28, "bold")
    )

    title.pack(
        pady=20
    )

    website_entry = ctk.CTkEntry(
        dashboard,
        width=500,
        placeholder_text="Website"
    )

    website_entry.pack(
        pady=10
    )

    username_entry = ctk.CTkEntry(
        dashboard,
        width=500,
        placeholder_text="Username"
    )

    username_entry.pack(
        pady=10
    )

    password_entry = ctk.CTkEntry(
        dashboard,
        width=500,
        placeholder_text="Password"
    )

    password_entry.pack(
        pady=10
    )

    ctk.CTkButton(
        dashboard,
        text="Generate Password",
        command=generate_new_password).pack(
        pady=5
    )

    ctk.CTkButton(
        dashboard,
        text="Add Credential",
        command=add_new_credential
    ).pack(
        pady=5
    )

    ctk.CTkButton(
        dashboard,
        text="View Credential",
        command=view_credential_gui
    ).pack(
        pady=5
    )

    ctk.CTkButton(
        dashboard,
        text="Delete Credential",
        command=delete_credential_gui
    ).pack(
        pady=5
    )

    credential_box = ctk.CTkTextbox(
        dashboard,
        width=600,
        height=250
    )

    credential_box.pack(
        pady=20
    )

    refresh_credentials()

    dashboard.mainloop()


# ==========================================
# LOGIN
# ==========================================

def login():

    global current_user_id

    username = login_username.get().strip()

    password = login_password.get().strip()

    if not username or not password:

        messagebox.showerror(
            "Error",
            "Fill all fields"
        )

        return

    user_id = login_user(
        username,
        password
    )

    if not user_id:

        messagebox.showerror(
            "Login Failed",
            "Invalid Credentials"
        )

        return

    current_user_id = user_id

    open_dashboard()


# ==========================================
# REGISTER
# ==========================================

def register():

    username = login_username.get().strip()

    password = login_password.get().strip()

    if not username or not password:

        messagebox.showerror(
            "Error",
            "Fill all fields"
        )

        return

    success = register_user(
        username,
        password
    )

    if success:

        messagebox.showinfo(
            "Success",
            "User Registered"
        )

    else:

        messagebox.showerror(
            "Error",
            "Username Already Exists"
        )


# ==========================================
# LOGIN WINDOW
# ==========================================

login_window = ctk.CTk()

login_window.title(
    "Vault Login"
)

login_window.geometry(
    "450x350"
)

title = ctk.CTkLabel(
    login_window,
    text="Vault Login",
    font=("Arial", 28, "bold")
)

title.pack(
    pady=30
)

login_username = ctk.CTkEntry(
    login_window,
    width=300,
    placeholder_text="Username"
)

login_username.pack(
    pady=10
)

login_password = ctk.CTkEntry(
    login_window,
    width=300,
    placeholder_text="Password",
    show="*"
)

login_password.pack(
    pady=10
)

ctk.CTkButton(
    login_window,
    text="Login",
    command=login
).pack(
    pady=10
)

ctk.CTkButton(
    login_window,
    text="Register",
    command=register
).pack(
    pady=10
)

login_window.mainloop()