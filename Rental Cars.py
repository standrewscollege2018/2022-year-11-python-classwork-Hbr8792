print("Welcome to the University vehicle rental system")
car_list = [" 1.Suzuki Van Seats:2",
            " 2.Toyota Corolla Seats:4",
            " 3.Honda CRV Seats:4",
            " 4.Suzuki Swift Seats:4",
            " 5.Mitsubishi Airtrek Seats:4",
            " 6.Nissan DC Ute Seats:4",
            " 7.Toyota Previa Seats:7",
            " 8.Toyota Hi Ace Seats:12",
            " 9.Toyota Hi Ace Seats:12."]
avail = ["Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available"]
name = input("Enter name:")
run_program = True
while run_program == True:
    for i in range(len(car_list)):
        print(i+1, car_list[i], avail[i])
    check = True
    while check == True:
        number = int(input("Please enter car number would you like to rent?:"))
        
        if number >9 or number <0:
            print("Please input vaild car number")
        else:
            check = False
    if number == 0:
        run_program = False
    else:
        avail[number-1] = "Unavailable"
      
        print(f"{car_list[number-1]}")


        print(f"Thank you for using University Vehicle Rental System {name} your car will be ready shortly")


