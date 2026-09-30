name1 = input("enter your name: ")
name2 = input("enter your name: ")
# converting all name to lower case
cal = (name1 + name2).lower()
# calculating for true
t = cal.count("t")
r = cal.count("r")
u = cal.count("u")
e = cal.count("e")
true = t + r + u + e
l = cal.count("l")
o = cal.count("o")
v = cal.count("v")
e2 = cal.count("e")
love = l + o + v + e2
# joining the true and love 
joined = (f"{true}{love}")
# checking for the condition
if love < 10 or love > 85:
    print(f"Your love score {joined}, you are alright like coke and fanta")
elif love >=40 and love <= 70:
    print(f"Your love score {joined}, you are alright together")
else:
    print(f"your love score is {joined}")