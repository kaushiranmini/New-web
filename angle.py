C = int(input("Enter your x_value (C): "))
C1 = int(input("Enter your y_value (C1): "))

ax = 4
ay = 5
bx = 5
by = 4

if ax < C and ay > C1:
    print("It is a sulu konaya")

elif ax < C and ay == C1:
    print("It is a suju konaya")

elif ax < C and ay < C1:
    print("It is a mahaa konaya")

elif ax == C and ay == C1:
    print("It is a sarala konaya")

elif ax == C and ay > C1:
    print("It is a paraawartha konaya")

elif ax == C and ay < C1:
    print("It is a chakarawarthi konaya")

else:
    print("No condition matched")
