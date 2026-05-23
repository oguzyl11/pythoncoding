import json


try:
   
        with open("roomie_data.json", "r") as file:
            roomie_db = json.load(file)
            print("The existing database has been successfully loaded.")
except FileNotFoundError:
    print("No existing database found. A new database will be created.")                    

    roomie_db = {
    "101": {
        "room_type":"standard",
        "price": 100,
        "situation": "available"
    },
    "102": {
        "room_type":"deluxe",
        "price": 180,
        "situation": "available"
    },
    "103": {
        "room_type":"standard",
        "price": 100,
        "situation": "occupied",
        "customer_name": "Ali Yilmaz"
    },
    "104": {
        "room_type":"suite",
        "price": 180,
        "situation": "occupied",
        "customer_name": "Elif Kaya"
    }
}
def check_in(db):
         print("Welcome to our hotel!")
         print("which room do you want to book? (101, 102, 103, 104)")
         input_room = input("Enter the room number: ")
         if input_room in db and db[input_room]["situation"] == "available":
            print("The room is available for booking.")
            name = input("Enter your name: ")
            db[input_room]["situation"] = "occupied"
            db[input_room]["customer_name"] = name
            print(f"Congratulations {name}, you have successfully booked room {input_room}.")
            print("Would you like to look at another room? (yes or no)" )
            with open("roomie_data.json", "w") as file:
              json.dump(db, file, indent=4)
            answer = input("Enter your answer: " )
            if answer.lower() == "yes":
                check_in(db)
            elif answer.lower() == "no":
                print("Thank you for using our hotel booking system. Have a great day!")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
            
         elif input_room in roomie_db and roomie_db[input_room]["situation"] == "occupied":
             print("Sorry, that room is already occupied. Please choose another room.")
         else:
             print("Invalid room number. Please enter a valid room number (101, 102, 103, 104)." )
def check_out(db):
      which_room = input("Enter the room number you want to check out from: ")
     if which_room in db and db[which_room]["situation"] == "occupied":
            db[which_room]["situation"] = "available"
            price = input("how many days did you stay?  ")
            total_price = int(price) * db[which_room]["price"]
            print(f"Your total price is: {total_price} dollars.")
            print(f"Thank you {db[which_room]['customer_name']} for staying with us. You have successfully checked out from room {which_room}.")
            del db[which_room]["customer_name"]
            with open("roomie_data.json", "w") as file:
             json.dump(db, file, indent=4)

            
        elif which_room in db and db[which_room]["situation"] == "available":
            print("That room is already available. Please check the room number and try again.")
            
        else:
            print("Invalid room number. Please enter a valid room number (101, 102, 103, 104)." )
            
    while True :
    ask = input("Welcome to our hotel booking system! What would you like to do? (1. Book a room, 2. Check out) ")
    if ask == "1":
        check_in(roomie_db)
    elif ask == "2":
        check_out(roomie_db)
    else:
        print("Invalid input. Please enter '1' to book a room or '2' to check out.")
        continue