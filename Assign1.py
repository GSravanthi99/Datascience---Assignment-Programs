#Circle area ,perimeter
PIVALUE = 3.14
radius = int(input('Enter the radius :'))
area = PIVALUE*radius**2
print(' Area Of The Circle :' , area)
perimeter =2*PIVALUE*radius
print('Perimeter Of The Circle :', perimeter)

#Rectangle Area ,Perimeter
l = int(input("Enter length of rectangle: "))
b = int (input("Enter breadth of rectangle: "))
print("Area of rectangle:", l * b)
print("Perimeter of rectangle:", 2 * (l + b))

#Square Area ,perimeter
s = int(input("Enter side of square: "))
print("Area of square:", s * s)
print("Perimeter of square:", 4 * s)
