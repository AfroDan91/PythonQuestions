grade = int(input("Please input your grade percentage here ->"))

if grade >= 70:
    print("A")

elif grade >=60 and grade < 70:
    print("B")

elif grade >=50 and grade < 60:
    print("C")

elif grade >=40 and grade < 50:
    print("D")

else:
    print("You failed")