# Louis Li

def encode(password):
    returnString = ""
    for char in password:
        returnString += str((int(char) + 3) % 10)
    return returnString

def decode(password):
    string = ""
    for char in password:
        string += f"{int(char) - 3}"
    return string 

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
            decodedPassword = decode(password)
            print("The encoded password is ", password, ", and the original password is ", decodedPassword, ".")

if __name__ == "__main__":
    main()
