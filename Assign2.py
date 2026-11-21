cm = int(input("Enter centimeters: "))
km = cm // 100000
remaining_cm = cm % 100000
m = remaining_cm // 100
remaining_cm = remaining_cm % 100
print("Kilometers:", km)
print("Meters:", m)
print("Remaining Centimeters:", remaining_cm)