def add_odd():
    cal = 0
    for number in range(1,100,2):
        cal += number
    return cal

print(add_odd())