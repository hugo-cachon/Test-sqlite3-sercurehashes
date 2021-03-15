# Test-sqlite3-secure-hashes
### A project that i made to discover sqlite3 and hashlib

The function *database*.new_user() allows you to add a row to the table.

Supported hash algorithm:

- SHA1 
- SHA224 
- SHA256
- SHA384
- SHA512
- MD5
- blake2b
- blake2s

To delete a user, use the function *database*.delete_user()

The function *database*.check_user() allows you to check if a certain name is registered in the database.
It will also tell you how many time the name have been found in the database

To display the database use the function:
*database*.display_db()

To create a database use the function
*database*.create_db()
The default columns of the DB are:
- Name
- Email
- Password
- Creation Date



