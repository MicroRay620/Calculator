print("I am your Mathmatical Assistance Helper or MAH!")
print("Please tell me your name!")
name = input("Tell yoru MAH what your name is:")
print("Hello,", name)
print("I go one step at a time.")
x = int(input("Your first number:"))
function = input("What kind of equasion do you want?")
y = int(input("Your second number:"))
exponents = input("Want to use exponents? MUST BE written as 'yes' or 'no'")
if exponents == "no":
    if function == "multiplication":
        z = x * y
        print("Your multiplication is", z)
    if function == "division":
        z = x / y
        print("You Division answer is", z)
    if function == "addition":
        z = x + y
        print("Your addition answer is", z)
    if function == "subtraction":
        z = x - y
        print("Your subtraction answer is", z)
if exponents == "yes":
    e = int(input("What exponent do you want?"))
    if function == "multiplication":
        z = x * y
        z = z ** e
        print("Your multiplication is", z)
    if function == "division":
        z = x / y
        z = z ** e
        print("You Division answer is", z)
    if function == "addition":
        z = x + y
        z = z ** e
        print("Your addition answer is", z)
    if function == "subtraction":
        z = x - y
        z = z ** e
        print("Your subtraction answer is", z)