# FIRST METHOD 
first = int((input("What is the first number? ")))
first1 = int((input("What is the first number? ")))
operation = input("pick operation from this list (+,-,*,/)")
if operation == "+" :
    ret = first + first1 
    # first + first1
elif operation == "-" :
    ret = first - first1
elif operation == "*" :
    ret = first * first1
elif operation == "/" :
    ret = first / first1

print (f"{first} {operation} {first1} = {ret}")

# SECOND METHOD
def add(a1, a2):
    return a1 + a2

def min(a1, a2):
    return a1 - a2

def multiply(a1, a2):
    return a1 * a2

def divi(a1, a2):
    return a1 / a2

a1 = int((input("What is the first number? ")))
a2 = int((input("What is the first number? ")))
operation = input("pick operation from this list (+,-,*,/)")
if operation == "+" :
    ret = add(a1, a2)
    # first + first1
elif operation == "-" :
    ret = min(a1, a2)
elif operation == "*" :
    ret =  multiply(a1, a2)
elif operation == "/" :
    ret =  divi(a1, a2)

print (f"{a1} {operation} {a2} = {ret}")
