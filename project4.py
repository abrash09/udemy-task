user1 = float (input("Enter hours \n"))
user2 = float (input("Enter rate per hour \n"))
grosspay = user1 * user2 
grosspay = round(user1 * user2, 2)
print(f"pay:{grosspay}")