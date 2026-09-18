# Here's is mine own code
def maximum_num (one, two, three):

# using the maximum built in
    return max(one, two, three)
# requesting for input
one = int(input("Enter number: "))
two = int(input("Enter number: "))
three = int(input("Enter number: "))


print(maximum_num (one, two, three))

# Here's the tutor code 

def first_two (p1, p2):
    if p1 > p2:
        return p1
    return p2
print(first_two (4, 5))

def three(p1,p2,p3):
    total = first_two (p1, p2)
    caltotal = first_two (total, p3)
    return caltotal
print(three(9,8,6))



