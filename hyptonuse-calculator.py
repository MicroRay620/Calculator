from math import sqrt
#Ruby Rose (started on October 2022)
print("Hello! You have gone to MAH's Hyptonuse Calculator!")
hypot = input("You need square root? ")
if hypot in {"yes" and "Yes" and "YES" and "Y"}:
    #add in multiple variable options
    a = int(input("What is the number for the first side? "))
    x = a ** 2
    b = int(input("What is the number for the second side? "))
    y = b ** 2
    c = x + y
    z = sqrt(c)
    print(a, "was squared, getting", x)
    print(b, "was squared, getting", y)
    print(x, "was added with", y, "getting", c)
    print(c, "was square rooted, ending with", z, "as the f")
