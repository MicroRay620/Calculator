grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+," "D", "D-", "F", "H"]
subject = ["math", "history", "english", "programming"]
#I don't have a science class outside of this; using it to get that credit
print("0: Math")
print("1: History")
print("2: Programming")
print("3: Test")
subjectDeterm = int(input("Insert a number for class [0 to 3]: "))
sub = subject[subjectDeterm]
percGrade = int(input("What is your percentage in that subject? [put the whole number] "))

if percGrade >= 97 and percGrade <= 100:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is an A+")
elif percGrade >= 93 and percGrade <= 96:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is A")
elif percGrade >= 90 and percGrade <= 92:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is A-")
elif percGrade >= 87 and percGrade <= 89:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is B+")
elif percGrade >= 83 and percGrade <= 86:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is B")
elif percGrade >= 80 and percGrade <= 82:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is B-")
elif percGrade >= 77 and percGrade <= 79:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is C+")
elif percGrade >= 73 and percGrade <= 76:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is C")
elif percGrade >= 70 and percGrade <= 72:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is C-")
elif percGrade >= 67 and percGrade <= 69:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is D+")
elif percGrade >= 63 and percGrade <= 66:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is D")
elif percGrade >= 60 and percGrade <= 62:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is D-")
elif percGrade >= 1 and percGrade <= 59:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is F or E (both mean same)")
elif percGrade <= 0 and percGrade < 1:
    print("Your percentage is", str(percGrade) + "%")
    print("Your grade in", sub, "is H")
else:
    print("I would recommended restarting")