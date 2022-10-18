from ast import Return
from math import sqrt
#Ruby Rose (started on October 2022)
switch = True
print("I am your Mathmatical Assistance Helper or MAH! \n here to help with your mathmatical needs!")
print("I can only go one step at a time. Please keep in mind, I am currently unable to do letter variables.")
while switch == True:
    numvars = input("how many numbers do you want? Please only pick a number 1-3. Only type out the numberical character")
    #change 1 - 2 to 1 - 4
    #ADD WHEN ISSUE RESOLVED <for x in numvars:> NEED TO LEARN PROPER USE FOR THE <for> variable
    if numvars != True:
        Return
        print("Please type in a number")
    if numvars in {"1"}:
        #Insert an option for negatives
            a = int(input("What number would you like? Type ONLY the numberical character and not the word "))
            exponents = input("Want to use exponents? MUST BE written as 'yes' or 'no' ")
            if exponents in {"yes" or "Yes" or "YES" or "Y"}:
                root = input("Would you like to do a square root? yes or no ")
                if root in {"yes" or "Yes" or "YES" or "Y"}:
                    e = int(input("What exponent do you want?"))
                    b = a ** e
                    c = sqrt(b)
                print(a, "was put to the power of", e, "giving the result", b)
                print(b, "was then square rooted giving", c)
                if root == "no" or "No" or "NO":
                    e = int(input("What exponent do you want? "))
                    b = a ** e
                print(a, "was put to the power of", e)
                print("Giving the final answer of", b)
                root = input("Would you like to do a square root? yes or no ")
            if exponents in {"no" or "No" or "NO" or "N"}:
                root = input("Would you like to do a square root? yes or no")
                if root in {"yes" or "Yes" or "YES" or "Y"}:
                    b = sqrt(a)
                    print(a, "was square rooted giving the answer of", b)
                #if exponent and root is No; lead to line 6
                if root in {"no" or "No" or "NO" or "N"}:
                    Return
    if numvars in {"2"}:
            a = int(input("Your first number:"))
            b = int(input("Your second number:"))
            function = input("What kind of equasion do you want?")
            exponents = input("Want to use exponents? MUST BE written as 'yes' or 'no'")
            if exponents in {"yes" or "Yes" or "YES" or "Y"}:
                e = int(input("What exponent do you want? Put a number"))
                root = input("Would you like to do a square root? 'yes' or 'no'")
                if root in {"yes" or "Yes" or "YES" or "Y"}:
                    if function in {"multiplication" or "Multiplication" or "MULTIPLICATION" or "*"}:
                        c = a * b
                        d = c ** e
                        f = sqrt(d)
                    if function in {"division" or "Division" or "DIVISION" or "/"}:
                        c = a / b
                        d = c ** e
                        f = sqrt(d)
                    if function in {"addition" or "Addition" or "ADDITION" or "+"}:
                        c = a + b
                        d = c ** e
                        f = sqrt(d)
                    if function in {"subtraction" or "Subtraction" or "SUBTRACTION" or "-"}:
                        c = a - b
                        d = c ** e
                        f = sqrt(d)
                    print(a, "was", function, "with", b, "ending up with", c)
                    print(c, "was put to the power of", e, "getting", d)
                    print(d, "was square rooted, getting", f)
                if root in {"no" or "No" or "NO" or "N"}:
                    if function in {"multiplication" or "Multiplication" or "MULTIPLICATION" or "*"}:
                        c = a * b
                        d = c ** e
                    if function in {"division" or "Division" or "DIVISION" or "/"}:
                        c = a / b
                        d = c ** e
                    if function in {"addition" or "Addition" or "ADDITION" or "+"}:
                        c = a + b
                        d = c ** e
                    if function in {"subtraction" or "Subtraction" or "SUBTRACTION" or "-"}:
                        c = a - b
                        d = c ** e
                    print(a, "was", function, "with", b, "ending up with", c)
                    print(c, "was then put to the power of", e, "giving answer", d)
            if exponents in {"no" or "No" or "NO" or "N"}:
                root = input("Would you like to do a square root? 'yes' or 'no'")
                if root in {"yes" or "Yes" or "YES" or "Y"}:
                    if function in {"multiplication" or "Multiplication" or "MULTIPLICATION"}:
                        c = a * b
                        d = sqrt(c)
                    if function in {"division" or "Division" or "DIVISION" or "/"}:
                        c = a / b
                        d = sqrt(d)
                    if function in {"addition" or "Addition" or "ADDITION" or "+"}:
                        c = a + b
                        d = sqrt(c)
                    if function in {"subtraction" or "Subtraction" or "SUBTRACTION" or "-"}:
                        c = a - b
                        d = sqrt(c)
                    print(a, "was", function, "with", b, "ending up with", c)
                    print("Then", c, "was square rooted ending with", d)
                if root in {"no" or "No" or "NO" or "N"}:
                    if function in {"multiplication" or "Multiplication" or "MULTIPLICATION" or "*"}:
                        c = a * b
                    if function in {"division" or "Division" or "DIVISION" or "/"}:
                        c = a / b
                    if function in {"addition" or "Addition" or "ADDITION" or "+"}:
                        c = a + b
                    if function in {"subtraction" or "Subtraction" or "SUBTRACTION" or "-"}:
                        c = a - b
                    print(a, "was", function, "with", b, "ending with", c)        
    if numvars in {"3"}:
            a = int(input("Your first number: "))
            b = int(input("Your second number: "))
            c = int(input("Your third number: "))
            function = input("What kind of equasion do you want? ")
            exponents = input("Want to use exponents? MUST BE written as 'yes' or 'no' ")
            if exponents in {"yes" or "Yes" or "YES" or "Y" or "y"}:
                e = int(input("What exponent do you want? Put a number"))
                root = input("Would you like to do a square root? ")
                if root in {"yes" or "Yes" or "YES" or "Y" or "y"}:
                    if function in {"multiplication" or "Multiplication" or "MULTIPLICATION"}:
                        f = a * b * c
                        g = d ** e
                        h = sqrt(g)
                    if function in {"division" or "Division" or "DIVISION" or "/"}:
                        d = a / b 
                        f = d / c
                        g = f ** e
                        h = sqrt(g)
                    if function in {"addition" or "Addition" or "ADDITION" or "+"}:
                        f = a + b + c
                        g = d ** e
                        g = sqrt(f)
                    if function in {"subtraction" or "Subtraction" or "SUBTRACTION" or "-"}:
                        d = a - b
                        f = d - c
                        g = g ** e
                        h = sqrt(g)
                print(a, b, "and", c, "were", function, "getting the answer of", f)
                print(d, "was put to the power of", e, "getting the result of", g)
                print(g, "was square rooted, giving the answer of", h)
                if root in {"no" or "No" or "NO" or "n" or "N"}:
                    if function in {"multiplication" or "Multiplication" or "MULTIPLICATION" or "*"}:
                        d = a * b * c
                    if function in {"division" or "Division" or "DIVISION" or "/"}:
                        d = a / b
                        f = d / c
                        g = f ** e 
                    if function in {"addition" or "Addition" or "ADDITION" or "+"}:
                        d = a + b
                    if function in {"subtraction" or "Subtraction" or "SUBTRACTION" or "-"}:
                        d = a - b
                        f = d - c
                        g = f ** e
                    print(a, b, "and", c, "were", function, "getting the answer of", f)
                    print(f, "was put to the power of", e, "ending with the answer of", g)
            if exponents in {"no" or "No" or "NO" or "n" or "N"}:
                root = input("Would you like to do a square root? ")
                if root in {"yes" or "Yes" or "YES" or "Y" or "y"}:
                    if function in {"multiplication" or "Multiplication" or "MULTIPLICATION"}:
                        f = a * b * c
                        g = sqrt(g)
                    if function in {"division" or "Division" or "DIVISION" or "/"}:
                        d = a / b 
                        f = d / c
                        g = sqrt(f)
                    if function in {"addition" or "Addition" or "ADDITION" or "+"}:
                        f = a + b + c
                        g = sqrt(d)
                    if function in {"subtraction" or "Subtraction" or "SUBTRACTION" or "-"}:
                        d = a - b
                        f = d - c
                        g = sqrt(f)
                    print (a, b, "and", c, "were", function, "getting the answer", f)
                    print(f, "was square rooted getting answer", g)
                if root in {"no" or "No" or "NO" or "n" or "N"}:
                    if function in {"multiplication" or "Multiplication" or "MULTIPLICATION"}:
                        f = a * b * c
                    if function in {"division" or "Division" or "DIVISION" or "/"}:
                        d = a / b 
                        f = d / c
                    if function in {"addition" or "Addition" or "ADDITION" or "+"}:
                        f = a + b + c
                    if function in {"subtraction" or "Subtraction" or "SUBTRACTION" or "-"}:
                        d = a - b
                        f = d - c
                print(a, b, "and", c, "were", function, "getting answer", f)
