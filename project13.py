hours = (input("Enter hours \n"))
try:
    hours = float(hours)
except ValueError:
    print("Error, please enter numeric for the inputs hours")
    quit()
rate = (input("Enter rate per hour \n"))

try:
    rate = float(rate)
except ValueError:
    print("Error, please enter numeric for the inputs rate")
    quit()
if hours > 40:
        overtime =  hours - 40
        pay = round(40 * rate + overtime * rate * 1.5,2)
else:
        pay = hours * rate
        
print(f"pay:{pay}")