player1=input('1st player Enter your name: ')

player1_x=int(input(f"{player1} Enter (x) position: "))

player1_y=int(input(f"{player1} Enter (y) position: "))

if (0 < player1_x < 9) and (0 < player1_y < 9):
    player2 = input('2nd player Enter your name: ')
    player2_x = int(input(f"{player2} Enter (x) position: "))
    player2_y = int(input(f"{player2} Enter (y) position: "))
    if (0 < player2_x < 9) and (0 < player2_y < 9) and (1 < player2_x < 8) and (1 < player2_y < 8):

         xx = player1_x-player2_x
         yy = player1_y-player2_y
         if(xx == 1) or (xx == -1) and ((yy == 1) or (yy == -1)):
             print(player1, ' you  cut ', player2)

             if(xx == 1) and (yy == -1):
                 print ('Your new position is (X): ',player1_x-2, '(Y): ', player1_y+2)
             elif(xx == -1) and (yy == 1):
                 print ('Your new position is (X): ',player1_x+2, '(Y): ', player1_y-2)
             elif(xx == -1) and (yy == -1):
                 print ('Your new position is (X): ',player1_x+2, '(Y): ', player1_y+2)
             elif(xx == 1) and (yy == 1):
                 print('Your new position is (X): ',player1_x-2, '(Y): ', player1_y-2)
         else:
             print('you cant cut')
    else:
        print('you cant cut')

else:
    print('check the number')