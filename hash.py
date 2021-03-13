import hashlib


# Function to hash the password and where put as parameter
# one of the available algorithm from the default hashlib module
def hash_password(password, algorithm):
    hash_algorithm = hashlib.new(algorithm)
    hash_algorithm.update(password.encode())
    return hash_algorithm.hexdigest()
