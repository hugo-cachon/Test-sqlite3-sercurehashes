import database


def main():
    options = int(input("1: Add User\n2: Delete User\n3: Check User\n4: Display Db\n"))

    if options == 1:
        try:
            database.new_user()
        except Exception as e:
            print("ERROR:", e)
        finally:
            print("\n")
            main()
    if options == 2:
        try:
            database.delete_user()
        except Exception as e:
            print("ERROR:", e)
        finally:
            print("\n")
            main()
    if options == 3:
        try:
            database.check_user()
        except Exception as e:
            print("ERROR:", e)
        finally:
            print("\n")
            main()
    if options == 4:
        database.display_db()
        print("\n")
        main()


if __name__ == "__main__":
    main()
