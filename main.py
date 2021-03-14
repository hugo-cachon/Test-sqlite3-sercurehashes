import database


def main():

    options = int(input("1: Add User\n2: Delete User\n3: Check password\n4: Display Db"))

    if options == 1:
        try:
            database.new_user()
        except Exception as e:
            print("ERROR:", e)
        finally:
            database.display_db()

    if options == 2:
        try:
            database.delete_user()
        except Exception as e:
            print("ERROR:", e)
        finally:
            database.display_db()

    if options == 3:
        print("TODO")

    if options == 4:
        database.display_db()
        main()


if __name__ == "__main__":
    main()
