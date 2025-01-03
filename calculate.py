Enter_first_number = input("Enter first number : ")

if (Enter_first_number.isdigit()):
    Enter_first_number = int(Enter_first_number)

    Enter_second_number = input("Enter second number : ")

    if (Enter_second_number.isdigit()):
        Enter_second_number = int(Enter_second_number)

        type = input("Enter your type :")

        if type == "+":
             print(Enter_first_number+Enter_second_number)

        elif type == "-":
            print(Enter_first_number-Enter_second_number)

        elif type == "*":
            print(Enter_first_number*Enter_second_number)

        elif type == "/":
            print(Enter_first_number/Enter_second_number)

    else:
        print("check the number")

else:
    print("check the number")
