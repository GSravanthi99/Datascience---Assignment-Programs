
a = int(input("Enter 1St side: "))
b = int(input("Enter 2nd side: "))
c = int(input("Enter 3rd side: "))

if a + b > c and a + c > b and b + c > a:
    print("The given sides form a triangle")
else:
    print("The given sides do not form a triangle")