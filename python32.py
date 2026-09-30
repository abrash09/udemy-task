def add_even_numbers(start, end):
    cal = 0
    for number in range(start, end):
        if number %2==0:
            cal += number
    return cal

print(add_even_numbers(1,101))