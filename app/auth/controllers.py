import app.db.db as db
from argon2 import PasswordHasher
"""
auth module
"""
ph = PasswordHasher()

__author__ = "Elliot Steffensen"
__version__ = "0.1.0"
__license__ = "MIT"

def generateAccessToken():
    pass

def generateRefreshToken():
    pass

def login():
    pass

def register(email, password, username, firstname, lastname):
    if db.verifyEmail(email):
        db.createUser(email, ph.hash(password), username, firstname, lastname)
        return True
    else:
        return False


def main():
    print("hello world")


if __name__ == "__main__":
    main()