# Test-sqlite3-secure-hashes
### A project that i made to discover sqlite3 and hashlib

The function new_user() allows you to add a row to the table.
Parameters to fill are pseudo, mail and password and hash algorithm

Example: *database*.new_user("John", "Doe", "John@Doe.com", "sha256")

Supported hash algorithm:

- SHA1 
- SHA224 
- SHA256
- SHA384
- SHA512
- MD5
- blake2b
- blake2s

To delete a user, use the function delete_user()
Parameter to fill is the row id of the user

Example: *database*.delete_user(2)

To display the database use the function:

*database*.display_db()

