import hashlib
username_trial = b"PRITCHARD"



print(hashlib.sha256(username_trial).hexdigest()[4]  , end="")
print(hashlib.sha256(username_trial).hexdigest()[5]  , end="")
print(hashlib.sha256(username_trial).hexdigest()[3]  , end="")
print(hashlib.sha256(username_trial).hexdigest()[6]  , end="")
print(hashlib.sha256(username_trial).hexdigest()[2]  , end="")
print(hashlib.sha256(username_trial).hexdigest()[7]  , end="")
print(hashlib.sha256(username_trial).hexdigest()[1]  , end="")
print(hashlib.sha256(username_trial).hexdigest()[8]  , end="")
    