print("Welcome to MAH's Distance Calculator!")
unit = input("What distance do you want? ")
if unit in {"inches" or "Inches" or "INCHES" or "\""}:
    inch = int(input("How many inches would you like to use? "))
    conv = input("What do you want to convert inches to? ")
    if conv in {"feet" or "Feet" or "FEET" or "ft" or "\'"}:
        ft = inch // 12
        if ft == 1:
            print(inch, "iches is equal to", ft, "foot")
        if ft >= 2 or ft < 1:
            print(inch, "inches is equal to", ft, "feet")
    if conv in {"yard" or "Yard" or "YARD" or "yd"}:
        yd = inch // 36
        if yd == 1:
            print(inch, "inches is equal to", yd, "yard")
        if yd >= 2:
            print(inch, "inches is equal to", yd, "yards")
    if conv in {"yards" or "Yards" or "YARDS" or "yds"}:
        yd = inch // 36
        if yd == 1:
            print(inch, "inches is equal to", yd, "yard")
        if yd >= 2 or yd > 1:
            print(inch, "inches is equal to", yd, "yards")
    if conv in {"miles" or "Miles" or "MILES" or "mi"}:
        mi = inch // 63360
        if mi == 1:
            print(inch, "inches is equal to", mi, "mile")
        if mi >= 2 or mi < 1:
            print(inch, "inches is equal to", mi, "miles")
if unit in {"feet" or "Feet" or "FEET" or "ft" or "\'"}:
    ft = int(input("How many feet do you want to do? "))
    conv = input("What would you like to convert to? ")
    if conv in {"inches" or "Inches" or "INCHES" or "\""}:
        inch = ft * 12
        if inch == 12:
            print(ft, "foot is equal to", inch, "inches")
        if inch >= 13 or inch <= 11 or inch < 1:
            print(ft, "feet is equal to", inch, "inches")
        if inch == 1:
            print(ft, "feet is equal to", inch, "inch")
    if conv in {"yard" or "Yard" or "YARD"}:
        yd = ft // 3
        if yd == 1:
            print(ft, "feet is equal to", yd, "yard")
        if yd >= 2 or yd < 1:
            print(ft, "feet is equal to", yd, "yards")
    if conv in {"miles" or "Miles" or "MILES" or "mi"}:
        mi = ft // 5280
        if mi == 1:
            print(ft, "is equal to", mi, "miles")
        if mi >= 2 or mi < 1:
            print(ft, "is equal to", mi, "miles")
if unit in {"yards" or "Yards" or "YARDS" or "yds" or "YDs"}:
    yd = int(input("How many yards? "))
    conv = input("What do you want to convert yards into? ")
    if conv in {"inches" or "Inches" or "INCHES"}:
        inch = yd * 36
        if inch == 36:
            print(yd, "yard is equal to", inch, "inches")
        if inch >= 37 or inch < 1:
            print(yd, "yards is equal to", inch, "inches")