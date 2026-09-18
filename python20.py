import math
def wall_calculation (height, width, coverage):
    area_wall = height * width
    num_can = math.ceil(area_wall / coverage)
    print(num_can)
height = int(input("Enter height of wall: "))
width = int(input("Enter width of wall: "))

wall_calculation(height,width,4)
