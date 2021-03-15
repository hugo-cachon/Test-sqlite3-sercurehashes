import sqlite3
import datetime
import hash


# Creation of the table "users"
def create_db():
    # Connection to the database
    conn = sqlite3.connect('database.db')
    # Cursor to navigate and execute in the database
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users (
            name TEXT,
            email TEXT,
            password BLOB,
            creation_date TEXT
            )""")


# Function to add a new user
def new_user():
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    algorithm = input("Algorithm: ")
    date = datetime.datetime.now()

    # Connection to the database
    connection = sqlite3.connect('database.db')
    # Cursor to navigate and execute in the database
    cursor = connection.cursor()

    # Hashing the password and choosing the algorithm
    password = hash.hash_password(password, algorithm)

    # Adding user to the db and closing connection
    cursor.execute("INSERT INTO users VALUES (?,?,?,?)", (name, email, date.strftime("%Y-%m-%d"), password ))

    connection.commit()
    connection.close()


# Function to delete a user taking as parameter the rowid
def delete_user():
    rowid = int(input("ID to delete in the DB: "))
    # Connection to the database
    connection = sqlite3.connect('database.db')
    # Cursor to navigate and execute in the database
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE rowid = (?)", (rowid,))

    connection.commit()
    connection.close()


# Function to check if the user exist in the db
def check_user():
    user = str(input("Name to check: "))
    # Connection to the database
    connection = sqlite3.connect('database.db')
    # Cursor to navigate and execute in the database
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, * FROM users WHERE name = (?) ", (user,))
    users = cursor.fetchall()

    print("ID" + "\tNAME" + "\tMAIL" + " \t\t\t\tCREATION DATE" + "\tPASSWORD")
    print("---" + "\t-------" + "\t----------" + "\t\t\t-----------" + "\t\t---------")

    for names in users:
        print(names[0],  "| ",  names[1], "\t| ", names[2], "\t| ", names[3], "\t| ", names[4])
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

    print("ID" + "\tNAME" + "\tMAIL" + " \t\t\t\tCREATION DATE" + "\tPASSWORD")
    print("---" + "\t-------" + "\t----------" + "\t\t\t-----------" + "\t\t---------")

    for user in users:
        print(user[0],  "| ",  user[1], "\t| ", user[2], "\t| ", user[3], "\t| ", user[4])

    connection.commit()
    connection.close()
