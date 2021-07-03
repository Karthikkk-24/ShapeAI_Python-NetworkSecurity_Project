import hashlib

#Python code for SHA256 algorithm

string01 ="Cybersecurity"
SHA256algorithm = hashlib.sha512(string01.encode())

print("The hexidecimal value : ",SHA256algorithm.hexdigest())