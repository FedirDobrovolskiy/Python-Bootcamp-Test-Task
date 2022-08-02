import hashlib

s = b"Python Bootcamp"


def toHash(var):
    hash_object = hashlib.sha512(var)
    hex_dig = hash_object.hexdigest()
    return hex_dig


print(toHash(s))
