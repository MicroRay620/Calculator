from math import sqrt
#Ruby Rose (started on October 2022)
#Add a link that will read the text out load
print("I am your Mathmatical Assistance Helper or MAH!")
print("I am here to help with your mathmatical needs!")
print("I go one step at a time. Please keep in mind, I am currently unable to do letter variables.")
numvars = input("how many numbers do you want? Please only pick a number 1-2. Only type out the numberical character")
#change 1 - 2 to 1 - 4
if numvars == "1":
    a = int(input("What number would you like? Type ONLY the numberical character and not the word"))
    exponents = input("Want to use exponents? MUST BE written as 'yes' or 'no'")
    if exponents == "yes" or "Yes" or "YES" or "Y":
        root = input("Would you like to do a square root? yes or no")
        if root == "yes" or "Yes" or "YES" or "Y":
            e = int(input("What exponent do you want?"))
            b = a ** e
            c = sqrt(b)
        print(a, "was put to the power of", e, "giving the result", b)
        print(b, "was then square rooted giving", c)
        if root == "no" or "No" or "NO":
            e = int(input("What exponent do you want?"))
            b = a ** e
        print(a, "was put to the power of", e)
        print("Giving the final answer of", b)
        root = input("Would you like to do a square root? yes or no")
    if exponents == "no" or "No" or "NO" or "N":
        root = input("Would you like to do a square root? yes or no")
        if root == "yes" or "Yes" or "YES" or "N":
            b = sqrt(a)
        print(a, "was square rooted giving the answer of", b)
        #if exponent and root is No; lead to line 6
if numvars == "2":
    a = int(input("Your first number:"))
    function = input("What kind of equasion do you want?")
    b = int(input("Your second number:"))
    exponents = input("Want to use exponents? MUST BE written as 'yes' or 'no'")
    if exponents == "no" or "No" or "NO" or "N":
        root = input("Would you like to do a square root? 'yes' or 'no'")
        if root == "yes" or "Yes" or "YES" or "Y":
            if function == "multiplication" or "Multiplication" or "MULTIPLICATION":
                c = a * b
                d = sqrt(c)
            if function == "division" or "Division" or "DIVISION" or "/":
                c = a / b
                d = sqrt(d)
            if function == "addition" or "Addition" or "ADDITION" or "+":
                c = a + b
                d = sqrt(c)
            if function == "subtraction" or "Subtraction" or "SUBTRACTION" or "-":
                c = a - b
                d = sqrt(c)
            print(a, "was", function, "with", b, "ending up with", c)
            print("Then", c, "was square rooted ending with", d)
        if root == "no" or "No" or "NO" or "N":
            if function == "multiplication" or "Multiplication" or "MULTIPLICATION" or "*":
                c = a * b
            if function == "division" or "Division" or "DIVISION" or "/":
                c = a / b
            if function == "addition" or "Addition" or "ADDITION" or "+":
                c = a + b
            if function == "subtraction" or "Subtraction" or "SUBTRACTION" or "-":
                c = a - b
            print(a, "was", function, "with", b, "ending with", c)
    if exponents == "yes" or "Yes" or "YES" or "Y":
        e = int(input("What exponent do you want? Put a number"))
        root = input("Would you like to do a square root? 'yes' or 'no'")
        if root == "yes" or "Yes" or "YES" or "Y":
            if function == "multiplication" or "Multiplication" or "MULTIPLICATION" or "*":
                c = a * b
                d = c ** e
                f = sqrt(d)
            if function == "division" or "Division" or "DIVISION" or "/":
                c = a / b
                d = c ** e
                f = sqrt(d)
            if function == "addition" or "Addition" or "ADDITION" or "+":
                c = a + b
                d = c ** e
                f = sqrt(d)
            if function == "subtraction" or "Subtraction" or "SUBTRACTION" or "-":
                c = a - b
                d = c ** e
                f = sqrt(d)
            print(a, "was", function, "with", b, "ending up with", c)
            print(c, "was put to the power of", e, "getting", d)
            print(d, "was square rooted, getting", f)
        if root == "no" or "No" or "NO" or "N":
            if function == "multiplication" or "Multiplication" or "MULTIPLICATION" or "*":
                c = a * b
                d = c ** e
            if function == "division" or "Division" or "DIVISION" or "/":
                c = a / b
                d = c ** e
            if function == "addition" or "Addition" or "ADDITION" or "+":
                c = a + b
                d = c ** e
            if function == "subtraction" or "Subtraction" or "SUBTRACTION" or "-":
                c = a - b
                d = c ** e
            print(a, "was", function, "with", b, "ending up with", c)
            print(c, "was then put to the power of", e, "giving answer", d)
