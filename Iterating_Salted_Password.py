import hashlib
import os

password = "Cybersecurity".encode()
print(password)

salt = os.urandom(16)
salted_password = hashlib.pbkdf2_hmac("sha256",password, salt, 100)
salted_password02 = hashlib.pbkdf2_hmac("sha256",password, salt, 1000)

#iterating the password for 2 times
print(salted_password*2)
#iterating the password for 14 times
print(salted_password02*14)