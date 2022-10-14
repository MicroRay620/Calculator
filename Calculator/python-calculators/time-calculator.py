print("You have entered MAH's Time Calculator!")
unit = input("What do you want to convert from? ")
if unit in {"seconds" or "Seconds" or "SECONDS"}:
    sec = int(input("How many seconds? "))
    conv = input("What do you want to convert seconds to? (Must be more than a second) ")
    if conv in {"minutes" or "Minutes" or "MINUTES"}:
        min = sec // 60
        if min == 1:
            print(sec, "seconds, when converted to minutes is", min, "minute")
        if min >= 2:
            print(sec, "seconds, when converted to minutes is", min, "minutes")
    if conv in {"hours" or "Hours" or "HOURS"}:
        hrs = sec // 120
        if hrs == 1:
            print(sec, "seconds converted to hours, is", hrs, "hour")
        if hrs >= 2:
            print(sec, "seconds, converted to hours, is", hrs, "hours")
    if conv in {"days" or "Days" or "DAYS"}:
        hrs = sec // 120
        print (sec, "seconds converted into hours is", hrs, "hours")
        days = hrs // 24
        print(hrs, "hours converted to days is", days, "days")
        if days >= 1:
            print("Which is a greater than or equal to 1 day")
        else: 
            print("Which is less than 1 day")
if unit in {"minutes" or "Minutes" or "MINUTES" or "min" or "Min" or "MIN"}:
    min = int(input("How many minutes? "))
    conv = input("What do you want to convert", unit, "to? ")
    if conv in {"seconds" or "Seconds" or "SECONDS"}:
        sec = min * 60

        print(min, "minutes")