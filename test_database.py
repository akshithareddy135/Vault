from database import *

create_database()

add_password(
    "amazon.com",
    "karunya@gmail.com",
    "Amazon123"
)

print(get_password("amazon.com"))

print(list_passwords())