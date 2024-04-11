# Louis Li

def encode(password):
    returnString = ""
    for char in password:
        returnString += str((int(char) + 3) % 10)
    return returnString


def main():
    print("Menu")
    print("------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = 0
    password = ""
    while choice != 3:
        choice = int(input("Please enter an option: "))
        if choice == 1:
            passToEncode = input("Please enter your password to encode: ")
            password = encode(passToEncode)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            decodedPassword = ""
            print("The encoded password is ", password, ", and the original password is ", decodedPassword, ".")

if __name__ == "__main__":
    main()
