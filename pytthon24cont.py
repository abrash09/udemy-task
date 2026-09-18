
def leap_year (ryear):
    if ryear % 4 == 0:
        if ryear % 100 == 0:
            if ryear % 400 == 0:
                return "leap year"
            else:
                return "not a leap year"  
        else:
            return "leap year"
        
    else:
        return "Not a leap year"
