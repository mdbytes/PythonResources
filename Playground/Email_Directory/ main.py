import pickle


def main_menu(email_dict):
    still_choosing = True
    print("\nHere are your options:\n\n\t1. List all emails in the directory\n\t2. Look up an email by name\n\t3. Enter more email addresses\n\t4. Remove an email address\n\t5. Exit Directory")
    while still_choosing:

        choice = int(input("\n\tEnter choice: "))

        if choice == 1:
            still_choosing = False
            list_all(email_dict)

        elif choice == 2:
            still_choosing = False
            look_up(email_dict)

        elif choice == 3:
            still_choosing = False
            enter_addresses(email_dict)

        elif choice == 4:
            still_choosing = False
            remove_address(email_dict)

        elif choice == 5:
            still_choosing = False
            close_shop(email_dict)

        else:
            print("Sorry.  I did not recognize that choice.  Try again")


def list_all(email_dict):
    print("\n")
    print("Name", "\tEmail Address")
    for name in email_dict:
        print(name, "\t", email_dict[name])
    main_menu(email_dict)


def look_up(email_dict):
    name = input("Name?  ")
    print("\n")
    if email_dict[name] is not None:
        print(email_dict[name])
    else:
        print("Sorry that name is not on record")
    main_menu(email_dict)


def enter_addresses(email_dict):
    keep_entering = 'y'

    while keep_entering == 'y':
        name = input("Name: ")
        email = input("Email: ")
        email_dict[name] = email

        keep_entering = input('Enter "y" to continue entering items')

    main_menu(email_dict)


def remove_address(email_dict):
    name = input("Name?  ")
    print("\n")
    if email_dict[name] is not None:
        del email_dict[name]
        print('Entry Deleted')
    else:
        print("Sorry that name is not on record")
    main_menu(email_dict)


def close_shop(email_dict):
    file_name = 'Playground/Email_Directory/email.dat'
    file = open(file_name, 'wb')
    pickle.dump(email_dict, file)
    file.close()
    print("Thanks for visiting!  Come back soon!")


def open_shop():
    email_dict = {}
    file_name = 'Playground/Email_Directory/email.dat'
    input_file = open(file_name, 'rb')
    email_dict = pickle.load(input_file)
    input_file.close()

    return email_dict


def main():
    print("\nWelcome to the email address directory!\n")
    email_dict = {}
    email_dict = open_shop()
    main_menu(email_dict)


main()
