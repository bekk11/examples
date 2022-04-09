import hashlib, binascii, os


def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    password_hash = binascii.hexlify(password_hash)
    return (salt+password_hash).decode('ascii')


eski = hash_password("4451122")
print(eski)


def check_password(stored_password, user_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    password_hash = hashlib.pbkdf2_hmac('sha512', user_password.encode('utf-8'), salt.encode('ascii'), 100000)
    password_hash = binascii.hexlify(password_hash).decode('ascii')
    return password_hash == stored_password


hash_password = hash_password("Mypassword")


print(check_password(eski, 'kalijscenfgb'))
