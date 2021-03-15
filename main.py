import database


def main():
    options = int(input("1: Add User"
                        "\n2: Delete User"
                        "\n3: Check User"
                        "\n4: Display Db"
                        "\n5: Create Db\n"))

    if options == 1:
        try:
            database.new_user()
        except Exception as error:
            print("ERROR:", error)
        finally:
            print("\n")
            main()
    if options == 2:
        try:
            database.delete_user()
        except Exception as error:
            print("ERROR:", error)
        finally:
            print("\n")
            main()
    if options == 3:
        try:
            database.check_user()
        except Exception as error:
            print("ERROR:", error)
        finally:
            print("\n")
            main()
    if options == 4:
        database.display_db()
        print("\n")
        main()
    if options == 5:
        try:
            database.create_db()
            print("Database created\n")
        except Exception as error:
            print("Error", error)
        finally:
            main()


if __name__ == "__main__":
    main()

