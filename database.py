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
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    algorithm = input("Algorithm: ")
    # Connection to the database
    connection = sqlite3.connect('database.db')
    # Cursor to navigate and execute in the database
    cursor = connection.cursor()
    # Hashing the password and choosing the algorithm
    password = hash.hash_password(password, algorithm)

    # Adding user to the db and closing connection
    cursor.execute("INSERT INTO users VALUES (?,?,?)", (name, email, password))
    connection.commit()
    connection.close()


# Function to delete a user taking as parameter the rowid
def delete_user():
    rowid = int(input("ID to delete in the DB: "))
    # Connection to the database
    connection = sqlite3.connect('database.db')
    # Cursor to navigate and execute in the database
    cursor = connection.cursor()
    cursor.execute("DELETE from users WHERE rowid = (?)", (rowid,))
    connection.commit()
    connection.close()


# Function to check if the user exist in the db
def check_user():
    user = str(input())
    # Connection to the database
    connection = sqlite3.connect('database.db')
    # Cursor to navigate and execute in the database
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, * FROM users WHERE pseudo = (?) ", (user,))
    users = cursor.fetchall()
    print("ID" + "\tNAME" + "\t\tMAIL " + "\t\t\t\t\tPASSWORD")
    print("---" + "\t-------" + "\t\t--------- " + "\t\t\t\t---------")

    for names in users:
        print(names[0],  "| ",  names[1], "\t| ", names[2], "\t| ", names[3])

    print(len(users), user, "found in the database\n")
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
    print("ID" + "\tNAME" + "\t\tMAIL " + "\t\t\t\t\tPASSWORD")
    print("---" + "\t-------" + "\t\t--------- " + "\t\t\t\t---------")
    for user in users:
        print(user[0],  "| ",  user[1], "\t| ", user[2], "\t| ", user[3])
    connection.commit()
    connection.close()
