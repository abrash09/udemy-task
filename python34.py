def numbers_divisible_byfive(p_list):
    for ban in p_list:
        if ban > 130:
            print("STOP")
            break

        if ban %5 == 0:
            print(ban)

list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
numbers_divisible_byfive(list1)