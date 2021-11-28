def password_check(password):
    Special_Symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '`', '~', ',', '.', '/',
                       '[', ']', '<', '>', '?', '{']
    val = True

    if len(password) < 5:
        val = False

    if len(password) > 15:
        val = False

    if not any(char.isupper() for char in password):
        val = False

    if not any(char.islower() for char in password):
        val = False

    if not any(char.isdigit() for char in password):
        val = False

    if not any(char in Special_Symbols for char in password):
        val = False

    if val:
        return val


def main():
    password = input("Password: ")
    length = len(password)
    if (password_check(password)):
        print(f"Your {length} character password is valid: {password}")
    else:
        print("Invalid Password!")


main()