cm = int(input("Enter centimeters: "))
km = cm // 100000
remainingcm = cm % 100000
m = remainingcm // 100
remainingcm = remainingcm % 100
print("Kilometers:", km)
print("Meters:", m)
print("Remaining Centimeters:", remainingcm)