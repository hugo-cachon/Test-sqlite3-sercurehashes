import sqlite3
import hash

# Connection to the database
conn = sqlite3.connect('database.db')
# Cursor to navigate and execute in the database
cursor = conn.cursor()

# Creation of the table "users"
# cursor.execute("""CREATE TABLE users (
#       pseudo BLOB,
#       email TEXT,
#       password BLOB
#       )""")


# Function to add a new user
def new_user():

    pseudo = str(input("Pseudo: ")),
    email = str(input("Email: ")),
    password = str(input("Password: ")),
    algorithm = str(input("Algorithm: "))

    # Connection to the database
    connection = sqlite3.connect('database.db')
    # Cursor to navigate and execute in the database
    cursor = connection.cursor()
    # Hashing the password and choosing the algorithm
    password = hash.hash_password(password, algorithm)

    # Adding user to the db and closing connection
    cursor.execute("INSERT INTO users VALUES (?,?,?)", (pseudo, email, password))
    connection.commit()
    connection.close()


# Function to delete a user taking as parameter the rowid
def delete_user():

    rowid = int(input("ID to delete of the DB"))

    # Connection to the database
    connection = sqlite3.connect('database.db')
    # Cursor to navigate and execute in the database
    cursor = connection.cursor()
    cursor.execute("DELETE from users WHERE rowid = (?)", str(rowid))
    connection.commit()
    connection.close()


# Function to display the db
def display_db():
    # Connection to the database
    connection = sqlite3.connect('database.db')
    # Cursor to navigate and execute in the database
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, * FROM users")
    users = cursor.fetchall()
    print("ID" + "\tPSEUDO" + "\t\tMAIL " + "\t\t\t\t\tPASSWORD")
    print("---" + "\t-------" + "\t\t--------- " + "\t\t\t\t---------")
    for user in users:
        print(user[0],  "| ",  user[1], "\t| ", user[2], "\t| ", user[3])
    connection.commit()
    connection.close()
