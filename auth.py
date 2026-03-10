import json
import os

USER_FILE = "users.json"


# ---------------- LOAD USERS ----------------

def load_users():

    if not os.path.exists(USER_FILE):

        with open(USER_FILE, "w") as f:
            json.dump({}, f)

    with open(USER_FILE, "r") as f:

        users = json.load(f)

    return users


# ---------------- SAVE USERS ----------------

def save_users(users):

    with open(USER_FILE, "w") as f:

        json.dump(users, f, indent=4)


# ---------------- SIGNUP ----------------

def signup(username, password):

    users = load_users()

    username = username.strip()

    if username in users:

        return False

    users[username] = password

    save_users(users)

    return True


# ---------------- LOGIN ----------------

def login(username, password):

    users = load_users()

    username = username.strip()

    if username in users and users[username] == password:

        return True
