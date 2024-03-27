import hashlib


def hashage(password: str):
    str2hash = password
    result = hashlib.md5(str2hash.encode())
    return result.hexdigest()
