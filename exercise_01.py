# Mary Johnson 1/14/2023
# Assuming all inputs are perfect (between 0-100 inclusive), this is fine. 

x = int(input("Enter a grade from 0 to 100: "))
if x >= 90:
    print("Your grade is A")
elif x >= 80:
    print("Your grade is B")
elif x >= 70:
    print("Your grade is C")
elif x >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")