

accountnumber = input("Enter your account number : ")
balance = 20000
if(accountnumber.isdigit()):
    if(len(accountnumber) == 7):
        transcation = input("Do you want to withdraw or deposit")
        if (transcation=="withdraw"): #IndentationError: expected an indented block after 'if' statement
            withdraw = input("How much do you want to withdow")
            if withdraw.isdigit():
               balance = balance - int(withdraw)
               print(balance)
            else:
                print("Invalid  input")

        elif (transcation == "deposit"):
              deposit = input("How much do you wont to deposit")
              if deposit.isdigit():
                 balance = balance + int(deposit)
                 print(balance)
              else:
                  print("Invalid  input")

else:
    print("Invalid input")









