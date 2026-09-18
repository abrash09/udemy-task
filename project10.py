hours = float (input("Enter hours \n"))
hours_per_hour = float (input("Enter rate per hour \n"))
if hours > 40:
    overtime =  hours - 40
    normal = (40 * hours_per_hour)
    overtime_pay = overtime * (hours_per_hour * 1.5)
    grosspay = overtime_pay + normal
else:
    grosspay = hours * hours_per_hour
print(f"pay:{grosspay}")
