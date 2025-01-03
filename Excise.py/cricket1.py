
total = 0
runs = input("Enter your runs:")

if runs.isdigit():
    runs = int(runs)
    if 1 <= runs <= 6:
                
        print(runs)
    else:
        print('Invalid input')
elif runs == 'nb':
    print('Extra')
elif runs == 'W':
    print('Wicket')
else:
    print('Invalid input')