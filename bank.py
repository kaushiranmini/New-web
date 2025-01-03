Amount = int(input("Enter Amount: "))

notes1 = 5000
notes2 = 1000
notes3 = 500
notes4 = 100
notes5 = 50
notes6 = 20
notes7 = 10

if Amount >= 5000:
   notes1 = int(Amount / 5000)
   print("5000 notes: ", notes1)
   Amount = Amount % 5000

   Amount >= 1000
   notes2 = int(Amount / 1000)
   print("1000 notes: ", notes2)
   Amount = Amount % 1000

   Amount >= 500
   notes3 = int(Amount / 500)
   print("500 notes: ", notes3)
   Amount = Amount % 500

   Amount >= 100
   notes4 = int(Amount / 100)
   print("100 notes: ", notes4)
   Amount = Amount % 100

   Amount >= 50
   notes5 = int(Amount / 50)
   print("50 notes: ", notes5)
   Amount = Amount % 50

   Amount >= 20
   notes6 = int(Amount / 20)
   print("20 notes: ", notes6)
   Amount = Amount % 20

   Amount >= 10
   notes7 = int(Amount / 10)
   print("10 notes: ", notes7)
   Amount = Amount % 10

