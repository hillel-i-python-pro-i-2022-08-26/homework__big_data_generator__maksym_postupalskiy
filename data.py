import secrets
import string
import random
from random import randint

from faker import Faker

fake = Faker()


def password_generator() -> str:
    letters = string.ascii_letters + string.digits
    while True:
        password = "".join(secrets.choice(letters) for i in range(randint(8, 15)))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    return password


def login_generator() -> str:
    name = fake.name().split()
    unique_name = [secrets.randbelow(1000), random.randint(1970, 2022), f"{secrets.choice(string.ascii_letters)}",
                   f'{secrets.choice(string.ascii_letters)}{secrets.choice(string.ascii_letters)}']
    fake_name1 = [name[0], name[1]]
    fake_name2 = [name[0], name[1], ""]
    username = fake.profile()['username']
    separator = [".", "_", "__", ""]
    login = [username, f"{secrets.choice(fake_name1)}{secrets.choice(separator)}{secrets.choice(fake_name2)}"]
    return f"{secrets.choice(unique_name)}{secrets.choice(separator)}{secrets.choice(login)}"

