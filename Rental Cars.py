print("Welcome to the University vehicle rental system")
Car_List = [" 1.Suzuki Van Seats:2",
            " 2.Toyota Corolla Seats:4",
            " 3.Honda CRV Seats:4",
            " 4.Suzuki Swift Seats:4",
            " 5.Mitsubishi Airtrek Seats:4",
            " 6.Nissan DC Ute Seats:4",
            " 7.Toyota Previa Seats:7",
            " 8.Toyota Hi Ace Seats:12",
            " 9.Toyota Hi Ace Seats:12."]

print(Car_List)

number = input("Please enter car number would you like to rent?:")
if number in range (1,9):
    print("Thank you, the car will be ready shortly")
else:
    print("Please input vaild car number")
if number == ("8"):
    Print("This car is currently unavaible please enter vaid car number")


