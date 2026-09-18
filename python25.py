def cal_pay (hours, rate):
    if hours > 40:
        overtime =  hours - 40
        normal = (40 * rate)
        overtime_pay = overtime * (rate * 1.5)
        grosspay = overtime_pay + normal
    else:
        grosspay = hours * rate
    return grosspay

def check_type (value):
    try:
        nal = value
        return nal
    except ValueError:
       print ("Enter numerical number")
       quit()

hours = int(input("Enter hours \n"))
hours = check_type(hours)
rate = float (input("Enter rate per hour \n"))
rate = check_type(rate)

grosspay = cal_pay (hours, rate)

print(f"pay:{grosspay}")