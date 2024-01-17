email = input("Enter your email: ")

if len(email) >= 6:
    if email[0].isalpha():
        if email.count("@") == 1:
            if (email[-4] == ".") ^ (email[-3] == "."):
                flag = False

                for i in email:
                    if i == " ":
                        flag = 1
                        break

                    elif i.isalpha() and i.isupper():
                        flag = 1
                        break

                    elif i.isdigit() or i.isalpha() or i == "_" or i == "." or i == "@":
                        continue

                    else:
                        flag = True

                if flag:
                    print("Invalid: email must not contain spaces, special characters or uppercase alphabets")

                else:
                    print("Entered email is valid")

            else:
                print("Invalid: dot must be at the correct position")
        else:
            print("Invalid: email must contain exactly one @")
    else:
        print("Invalid: email can only start with an alphabet")
else:
    print("Invalid: email length too short")
