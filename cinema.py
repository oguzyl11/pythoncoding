lounge = []
for i in range(5):
    line =["0"]*5
    lounge.append(line)
    for j in range(5):
       print(lounge[i] [j], end=" ")
    print()  
while True:     
 print("Welcome to the cinema booking system!")
 print("1. Book a seat")
 print("2. Side by side booking")
 choice = int(input("Enter your choice (1 or 2): "))
 if choice == 1:
     print("Enter the coordinates of the seat you want to book (row and column):")
     row = int(input("Enter row: "))
     column = int(input("Enter column: "))
     if row < 1 or row > 5 or column < 1 or column > 5:
         print("Invalid input. Please enter row and column numbers between 1 and 5.")
         continue

     if lounge[row-1][column-1] == "0":
         lounge[row-1][column-1] = "X"
         for i in range(5):
             for j in range(5):
                 print(lounge[i][j], end=" ")
             print()    
     else:
         print("Sorry, that seat is already booked. Please choose another seat.")
 else :
         print("Enter the coordinates of the first seat you want to book (row ):")
         row1 = int(input("Enter row: "))
         for i in range(5):
             i = row1-1
    
             for j in range(2):
                 if lounge[i][j] == "0" and lounge[i][j+1] == "0":
                     lounge[i][j] = "X"
                     lounge[i][j+1] = "X"
                 else:
                     for j in range(2-4):
                         if lounge[i][j] == "0" and lounge[i][j+1] == "0":
                             lounge[i][j] = "X"
                             lounge[i][j+1] = "X"
                         else:
                             print("Sorry, those seats are already booked. Please choose another row.")
                             break
                                            
                     for k in range(5):
                         for l in range(5):
                             print(lounge[k][l], end=" ")
                         print()    
                     break
                
 