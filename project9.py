print("Welcome to Burger Shop!")
size = input("What size Burger do you want? M, N or L ")
bill = 0
if size == "M":
    bill += 5
elif size == "N":
    bill += 8 
else:
    bill += 10 
    
add_Mushroom = input("Do you want mushroom? Y or N ")
if add_Mushroom == "Y":
    if size == "L":
        bill += 2
    else:
        bill += 1
extra_cheese = input("Do you want extra cheese? Y or N")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
