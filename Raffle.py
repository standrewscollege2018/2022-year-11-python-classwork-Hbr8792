#This Program is for the St Andrews College raffle
names = []
print("Kia ora, Welcome to the St Andrews College Raffle program")
ask_da_Person = True
while ask_da_Person == True:
    prize = input("Enter the prize being raffled: ")
    if prize == "":
        print("Please enter a valid prize.")
    else:
        print(f"The prize for this raffle is {prize}.")
        ask_da_Person = False


#Selecting the prize
        
get_value = True
value = input("Please enter prize value")
value = float(value)

ask_name = True
while ask_name == True:
    name = input("Plese enter name")
    if name == "end":
        ask_name = False
    else:
        names.append(name)

print(names)




                
                
