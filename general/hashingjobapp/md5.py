import hashlib
string = 'Hawaii'
hashed = hashlib.md5(string.encode())
print(hashed.hexdigest())
