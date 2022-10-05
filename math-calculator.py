from math import sqrt
#Ruby Rose (started on October 2022)
print("I am your Mathmatical Assistance Helper or MAH!")
print("Please tell me your name!")
name = input("Tell yoru MAH what your name is:")
print("Hello,", name)
print("I go one step at a time. Please keeo in mind, I am currently unable to do letter variables.")
numvars = input("how many numbers do you want? Please only pick a number 1-4. Only type out the numberical character")
if numvars == "1":
    x = int(input("What number would you like? Type ONLY the numberical character and not the word"))
    exponents = input("Want to use exponents? MUST BE written as 'yes' or 'no'")
    if exponents == "yes":
        root = input("Would you like to do a square root? yes or no")
        if root == "yes":
            e = int(input("What exponent do you want?"))
            x = sqrt(x ** e)
            print("Your answer is", x)
        if root == "no":
            e = int(input("What exponent do you want?"))
            x = x ** e
            print("Your answer is", x)
        if root == "No":
            e = int(input("What exponent do you want?"))
            x = x ** e
            print("Your answer is", x)
        if root == "NO":
            e = int(input("What exponent do you want?"))
            x = x ** e
            print("Your answer is", x)
    if exponents == "Yes":
        root = input("Would you like to do a square root? yes or no")
        if root == "no":
            e = int(input("What exponent do you want?"))
            x = x ** e
            print("Your answer is", x)
        if root == "No":
            e = int(input("What exponent do you want?"))
            x = x ** e
            print("Your answer is", x)
        if root == "NO":
            e = int(input("What exponent do you want?"))
            x = x ** e
            print("Your answer is", x)
    if exponents == "YES":
        root = input("Would you like to do a square root? yes or no")
        if root == "yes":
            e = int(input("What exponent do you want?"))
            x = sqrt(x ** e)
            print("You answer is", x)
        if root == "Yes":
            e = int(input("What exponent do you want?"))
            x = sqrt(x ** e)
        if root == "YES":
            e = int(input("What exponent do you want?"))
            x = sqrt(x ** e)
            print("Your answer is", x)
        if root == "no":
            e = int(input("What exponent do you want?"))
            x = x ** e
            print("Your answer is", x)
        if root == "No":
            e = int(input("What exponent do you want?"))
            x = x ** e
            print("Your answer is", x)
        if root == "NO":
            e = int(input("What exponent do you want?"))
            x = x ** e
            print("Your answer is", x)
    if exponents == "no":
        root = input("Would you like to do a square root? yes or no")
        if root == "yes":
            x = sqrt(x)
            print(x)
            print("Your answer is", x)
        if root == "Yes":
            x = sqrt(x)
            print("Your answer is", x)
        if root == "YES":
            x = sqrt(x)
            print("Your answer is", x)
        #if both exponents AND roots are no, go back to line 6
if numvars == "2":
    x = int(input("Your first number:"))
    function = input("What kind of equasion do you want?")
    y = int(input("Your second number:"))
    exponents = input("Want to use exponents? MUST BE written as 'yes' or 'no'")
    root = input("Would you like to do a square root? yes or no")
    if exponents == "no":
        # Change var z to x
        if function == "multiplication":
            z = x * y
            print("Your multiplication is", z)
        if function == "Multiplication":
            z = x * y
            print("Your multiplication is", z)
        if function == "MULTIPLICATION":
            z = x * y
            print("Your multiplication is", z)
        if function == "*":
            z = x * y
            print("Your multiplication is", z)
        if function == "division":
            z = x / y
            print("You Division answer is", z)
        if function == "Division":
            z = x / y
            print("You Division answer is", z)
        if function == "DIVISION":
            z = x / y
            print("You Division answer is", z)
        if function == "/":
            z = x / y
            print("You Division answer is", z)
        if function == "addition":
            z = x + y
            print("Your addition answer is", z)
        if function == "Addition":
            z = x + y
            print("Your addition answer is", z)
        if function == "ADDITION":
            z = x + y
            print("Your addition answer is", z)
        if function == "+":
            z = x + y
            print("Your addition answer is", z)
        if function == "subtraction":
            z = x - y
            print("Your subtraction answer is", z)
        if function == "Subtraction":
            z = x - y
            print("Your subtraction answer is", z)
        if function == "SUBTRACTION":
            z = x - y
            print("Your subtraction answer is", z)
        if function == "-":
            z = x - y
            print("Your subtraction answer is", z)
    if exponents == "No":
        if function == "multiplication":
            z = x * y
            print("Your multiplication is", z)
        if function == "Multiplication":
            z = x * y
            print("Your multiplication is", z)
        if function == "MULTIPLICATION":
            z = x * y
            print("Your multiplication is", z)
        if function == "*":
            z = x * y
            print("Your multiplication is", z)
        if function == "division":
            z = x / y
            print("You Division answer is", z)
        if function == "Division":
            z = x / y
            print("You Division answer is", z)
        if function == "DIVISION":
            z = x / y
            print("You Division answer is", z)
        if function == "/":
            z = x / y
            print("You Division answer is", z)
        if function == "addition":
            z = x + y
            print("Your addition answer is", z)
        if function == "Addition":
            z = x + y
            print("Your addition answer is", z)
        if function == "ADDITION":
            z = x + y
            print("Your addition answer is", z)
        if function == "+":
            z = x + y
            print("Your addition answer is", z)
        if function == "subtraction":
            z = x - y
            print("Your subtraction answer is", z)
        if function == "Subtraction":
            z = x - y
            print("Your subtraction answer is", z)
        if function == "SUBTRACTION":
            z = x - y
            print("Your subtraction answer is", z)
        if function == "-":
            z = x - y
            print("Your subtraction answer is", z)
    if exponents == "NO":
        if function == "multiplication":
            z = x * y
            print("Your multiplication is", z)
        if function == "Multiplication":
            z = x * y
            print("Your multiplication is", z)
        if function == "MULTIPLICATION":
            z = x * y
            print("Your multiplication is", z)
        if function == "*":
            z = x * y
            print("Your multiplication is", z)
        if function == "division":
            z = x / y
            print("You Division answer is", z)
        if function == "Division":
            z = x / y
            print("You Division answer is", z)
        if function == "DIVISION":
            z = x / y
            print("You Division answer is", z)
        if function == "/":
            z = x / y
            print("You Division answer is", z)
        if function == "addition":
            z = x + y
            print("Your addition answer is", z)
        if function == "Addition":
            z = x + y
            print("Your addition answer is", z)
        if function == "ADDITION":
            z = x + y
            print("Your addition answer is", z)
        if function == "+":
            z = x + y
            print("Your addition answer is", z)
        if function == "subtraction":
            z = x - y
            print("Your subtraction answer is", z)
        if function == "Subtraction":
            z = x - y
            print("Your subtraction answer is", z)
        if function == "SUBTRACTION":
            z = x - y
            print("Your subtraction answer is", z)
        if function == "-":
            z = x - y
            print("Your subtraction answer is", z)
    if exponents == "yes":
        e = int(input("What exponent do you want?"))
        if function == "multiplication":
            z = x * y
            z = z ** e
            print("Your multiplication is", z)
        if function == "Multiplication":
            z = x * y
            z = z ** e
            print("Your multiplication is", z)
        if function == "MULTIPLICATION":
            z = x * y
            z = z ** e
            print("Your multiplication is", z)
        if function == "*":
            z = x * y
            z = z ** e
            print("Your multiplication is", z)
        if function == "division":
            z = x / y
            z = z ** e
            print("You Division answer is", z)
        if function == "Division":
            z = x / y
            z = z ** e
            print("You Division answer is", z)
        if function == "DIVISION":
            z = x / y
            z = z ** e
            print("You Division answer is", z)
        if function == "/":
            z = x / y
            z = z ** e
        print("You Division answer is", z)
        if function == "addition":
            z = x + y
            z = z ** e
            print("Your addition answer is", z)
        if function == "Addition":
            z = x + y
            z = z ** e
            print("Your addition answer is", z)
        if function == "ADDITIONAL":
            z = x + y
            z = z ** e
            print("Your addition answer is", z)
        if function == "+":
            z = x + y
            z = z ** e
            print("Your addition answer is", z)
        if function == "subtraction":
            z = x - y
            z = z ** e
            print("Your subtraction answer is", z)
        if function == "Subtraction":
            z = x - y
            z = z ** e
            print("Your subtraction answer is", z)
        if function == "SUBTRACTION":
            z = x - y
            z = z ** e
            print("Your subtraction answer is", z)
        if function == "-":
            z = x - y
            z = z ** e
            print("Your subtraction answer is", z)
