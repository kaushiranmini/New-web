total = 0
player_A_runs = 0
player_B_runs = 0

batsman = input("Enter the batsman (A or B): ")
runs = int(input("Enter the runs (0,1,2,3,4,6): "))

print(f"Player B scored {player_B_runs} runs.")
print(f"Player A scored {player_A_runs} runs")
print(f"you are {total}")

if batsman == "A":
    player_A_runs = player_A_runs + runs
    total = total + runs
    if runs % 2 == 1:
        batsman = "B"
    elif runs % 2 == 0:
        batsman = "A"

elif batsman == "B":
    player_B_runs = player_B_runs + runs
    total = total + runs
    if runs % 2 == 1:
        batsman = "A"
    elif runs % 2 == 0:
        batsman = "B"

print(f"Player A scored {player_A_runs} runs.")
print(f"Player B scored {player_B_runs} runs")
print(f"Team {total}")
print(f"{batsman} is player  ")

# Second ball
runs = int(input("Enter the runs for second ball (0,1,2,3,4,6): "))

if batsman == "A":
    player_A_runs = player_A_runs + runs
    total = total + runs
    if runs % 2 == 0:
        batsman = "A"
    elif runs % 2 == 1:
        batsman = "B"

elif batsman == "B":
    player_B_runs = player_B_runs + runs
    total = total + runs
    if runs % 2 == 1:
        batsman = "A"
    elif runs % 2 == 0:
        batsman = "B"

print(f"Player A scored {player_A_runs} runs.")
print(f"Player B scored {player_B_runs} runs")
print(f"you are {total}")
print(f"{batsman} is player  ")

# Third ball
runs = int(input("Enter the runs for third ball (0,1,2,3,4,6): "))

if batsman == "A":
    player_A_runs = player_A_runs + runs
    total = total + runs
    if runs % 2 == 1:
        batsman = "B"
    elif runs % 2 == 0:
        batsman = "A"

elif batsman == "B":
    player_B_runs = player_B_runs + runs
    total = total + runs
    if runs % 2 == 1:
        batsman = "A"
    elif runs % 2 == 0:
        batsman = "B"

print(f"Player A scored {player_A_runs} runs.")
print(f"Player B scored {player_B_runs} runs")
print(f"you are {total}")
print(f"{batsman} is player  ")

# Fourth ball
runs = int(input("Enter the runs for fourth ball (0,1,2,3,4,6): "))

if batsman == "A":
    player_A_runs = player_A_runs + runs
    total = total + runs
    if runs % 2 == 1:
        batsman = "B"
    elif runs % 2 == 0:
        batsman = "A"

elif batsman == "B":
    player_B_runs = player_B_runs + runs
    total = total + runs
    if runs % 2 == 1:
        batsman = "A"
    elif runs % 2 == 0:
        batsman = "B"

print(f"Player A scored {player_A_runs} runs.")
print(f"Player B scored {player_B_runs} runs")
print(f"you are {total}")
print(f"{batsman} is player  ")

# Fifth ball
runs = int(input("Enter the runs for fifth ball (0,1,2,3,4,6): "))

if batsman == "A":
    player_A_runs = player_A_runs + runs
    total = total + runs
    if runs % 2 == 1:
        batsman = "B"
    elif runs % 2 == 0:
        batsman = "A"

elif batsman == "B":
    player_B_runs = player_B_runs + runs
    total = total + runs
    if runs % 2 == 1:
        batsman = "A"
    elif runs % 2 == 0:
        batsman = "B"

print(f"Player A scored {player_A_runs} runs.")
print(f"Player B scored {player_B_runs} runs")
print(f"you are {total}")
print(f"{batsman} is player  ")

# Sixth ball
runs = int(input("Enter the runs for sixth ball (0,1,2,3,4,6): "))

if batsman == "A":
    player_A_runs = player_A_runs + runs
    total = total + runs
    if runs % 2 == 0:
        batsman = "A"
    elif runs % 2 == 1:
        batsman = "B"

elif batsman == "B":
    player_B_runs = player_B_runs + runs
    total = total + runs
    if runs % 2 == 1:
        batsman = "A"
    elif runs % 2 == 0:
        batsman = "B"

# Final total
print(f"Total runs scored: {total}")
print(f"Player A scored: {player_A_runs} runs.")
print(f"Player B scored: {player_B_runs} runs.")
