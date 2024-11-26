import bcrypt
import os


def hash_password(plain_passw):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(str(plain_passw).encode('utf-8'), salt)
    return hashed_password

def verify_password(plain_passw, hashed_passw):
    print(str(plain_passw).encode('utf-8'))
    print(str(hashed_passw).encode('utf-8'))
    return bcrypt.checkpw(str(plain_passw).encode('utf-8'), str(hashed_passw).encode('utf-8'))