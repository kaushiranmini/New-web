# Card Values
Q = 12
K = 13
J = 11
A = 1

# Player 1
player_1 = input("Enter player 1 name: ")
value = input("Enter card value (2-10, Q, K, J, A): ")
total1 = 0


# Player 1
if value.isdigit() and 2 <= int(value) <= 10:
    total1 = int(value)
elif value == 'Q' or value == 'q':  # Enter card value (2-10, Q, K, J, A): q : my total is: 0
    total1 = Q
elif value == 'K' or value == 'k':
    total1 = K
elif value == 'J' or value == 'j':
    total1 = J
elif value == 'A' or value == 'a':
    total1 = A
else:
 print(player_1, "total is:", total1)
chance = input("Do you want another chance (yes/no): ")

if chance == "yes":
    value = input("Enter your next card value (2-10, Q, K, J, A): ")

    if value.isdigit() and 2 <= int(value) <= 10:
        total1 += int(value)
    elif value == 'Q' or value == 'q':
        total1 += Q
    elif value == 'K' or value == 'k':
        total1 += K
    elif value == 'J' or value == 'j':
        total1 += J
    elif value == 'A' or value == 'a':
        total1 += A
else:
    print(player_1, "total is:", total1)

    if total1 <= 31:
        chance = input("Do you want another chance (yes/no): ")

        if chance == "yes":
            value = input("Enter your next card value (2-10, Q, K, J, A): ")

            if value.isdigit() and 2 <= int(value) <= 10:
                total1 += int(value)
            elif value == 'Q' or value == 'q':
                total1 += Q
            elif value == 'K' or value == 'k':
                total1 += K
            elif value == 'J' or value == 'j':
                total1 += J
            elif value == 'A' or value == 'a':
                total1 += A

                print(player_1, "total is:", total1)

                if total1 > 31:
                    print(f'{player_1},{total1}')
        else:
            print(player_1, "total is:", total1)
    else:
        print("invalid")

# Player 2
player_2 = input("Enter player 2 name: ")
value = input("Enter card value (2-10, Q, K, J, A): ")
total2 = 0


# Player 2
if value.isdigit() and 2 <= int(value) <= 10:
    total2 = int(value)
elif value == 'Q' or value == 'q':
    total2 = Q
elif value == 'K' or value == 'k':
    total2 = K
elif value == 'J' or value == 'j':
    total2 = J
elif value == 'A' or value == 'a':
    total2 = A
else:
    print("Invalid input for card value.")
print(player_2, "total is:", total2)

chance = input("Do you want another chance (yes/no): ")

if chance == "yes":
    value = input("Enter your next card value (2-10, Q, K, J, A): ")

    if value.isdigit() and 2 <= int(value) <= 10:
        total2 += int(value)
    elif value == 'Q' or value == 'q':
        total2 += Q
    elif value == 'K' or value == 'k':
        total2 += K
    elif value == 'J' or value == 'j':
        total2 += J
    elif value == 'A' or value == 'a':
        total2 += A
else:
    print("Invalid input for card value.")
print(player_2, "total is:", total2)

if total2 <= 31:
    chance = input("Do you want another chance (yes/no): ")

    if chance == "yes":
        value = input("Enter your next card value (2-10, Q, K, J, A): ")

        if value.isdigit() and 2 <= int(value) <= 10:
            total2 += int(value)
        elif value == 'Q' or value == 'q':
            total2 += Q
        elif value == 'K' or value == 'k':
            total2 += K
        elif value == 'J' or value == 'j':
            total2 += J
        elif value == 'A' or value == 'a':
            total2 += A
        else:
            print("Invalid input for card value.")

        print(player_2, "total is:", total2)

        if total2 > 31:
            print(f'{player_2}, your total is {total2}, which is over 31. You lost the game.')
else:
    print(player_2, "total is:", total2)
#winner
if total2 > 31:
    print(f'{player_2} wins because {player_1} total 31.')
elif total2 > 31:
    print(f'{player_1} wins because {player_2} total 31.')
elif total2 > total2:
    print(f'{player_1} wins with a total card total of {total2}.')
elif total2 > total2:
    print(f'{player_2} wins with a total card total of {total2}.')
else:
    print("Try!")