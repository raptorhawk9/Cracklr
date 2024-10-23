import hashlib
import os

def generate_pbkdf2_password(secret, salt=None, iterations=100000, dklen=16):
    if salt is None:
        salt = os.urandom(16)
    return hashlib.pbkdf2_hmac('sha256', secret.encode(), salt, iterations, dklen).hex()

print(generate_pbkdf2_password("user-secret"))  # Example: 4f9c2b5d... (hash output)
