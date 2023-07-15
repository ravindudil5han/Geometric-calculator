import math

def rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    perimeter = 2 * (length + width)
    area = length * width
    print(f"Perimeter of the rectangle: {perimeter}")
    print(f"Area of the rectangle: {area}")

def square():
    side = float(input("Enter the length of the side of the square: "))
    perimeter = 4 * side
    area = side ** 2
    print(f"Perimeter of the square: {perimeter}")
    print(f"Area of the square: {area}")

def triangle():
    side1 = float(input("Enter the length of the first side of the triangle: "))
    side2 = float(input("Enter the length of the second side of the triangle: "))
    side3 = float(input("Enter the length of the third side of the triangle: "))
    perimeter = side1 + side2 + side3
    area = math.sqrt(perimeter * (perimeter - side1) * (perimeter - side2) * (perimeter - side3))
    angle_sum = side1 + side2 + side3
    print(f"Perimeter of the triangle: {perimeter}")
    print(f"Area of the triangle: {area}")
    print(f"Sum of angles in the triangle: {angle_sum}")

def right_triangle():
    base = float(input("Enter the length of the base of the right triangle: "))
    height = float(input("Enter the height of the right triangle: "))
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    perimeter = base + height + hypotenuse
    area = 0.5 * base * height
    print(f"Hypotenuse of the right triangle: {hypotenuse}")
    print(f"Perimeter of the right triangle: {perimeter}")
    print(f"Area of the right triangle: {area}")

def pythagorean_theorem():
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
    print(f"Hypotenuse of the right triangle: {hypotenuse}")

def isosceles_triangle():
    base = float(input("Enter the length of the base of the isosceles triangle: "))
    side = float(input("Enter the length of the equal side of the isosceles triangle: "))
    perimeter = 2 * side + base
    height = math.sqrt(side ** 2 - (base / 2) ** 2)
    area = 0.5 * base * height
    print(f"Perimeter of the isosceles triangle: {perimeter}")
    print(f"Area of the isosceles triangle: {area}")

def equilateral_triangle():
    side = float(input("Enter the length of the side of the equilateral triangle: "))
    perimeter = 3 * side
    area = (math.sqrt(3) / 4) * side ** 2
    print(f"Perimeter of the equilateral triangle: {perimeter}")
    print(f"Area of the equilateral triangle: {area}")

def trapezoid():
    base1 = float(input("Enter the length of the first base of the trapezoid: "))
    base2 = float(input("Enter the length of the second base of the trapezoid: "))
    height = float(input("Enter the height of the trapezoid: "))
    perimeter = base1 + base2 + 2 * math.sqrt(((base2 - base1) / 2) ** 2 + height ** 2)
    area = 0.5 * (base1 + base2) * height
    print(f"Perimeter of the trapezoid: {perimeter}")
    print(f"Area of the trapezoid: {area}")

def circle():
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print(f"Circumference of the circle: {circumference}")
    print(f"Area of the circle: {area}")

def rectangular_solid():
    length = float(input("Enter the length of the rectangular solid: "))
    width = float(input("Enter the width of the rectangular solid: "))
    height = float(input("Enter the height of the rectangular solid: "))
    surface_area = 2 * (length * width + length * height + width * height)
    volume = length * width * height
    print(f"Surface area of the rectangular solid: {surface_area}")
    print(f"Volume of the rectangular solid: {volume}")

def cube():
    side = float(input("Enter the length of the side of the cube: "))
    surface_area = 6 * side ** 2
    volume = side ** 3
    print(f"Surface area of the cube: {surface_area}")
    print(f"Volume of the cube: {volume}")

def cone():
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    surface_area = math.pi * radius * (radius + slant_height)
    volume = (1 / 3) * math.pi * radius ** 2 * height
    print(f"Slant height of the cone: {slant_height}")
    print(f"Surface area of the cone: {surface_area}")
    print(f"Volume of the cone: {volume}")

def right_circular_cylinder():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    surface_area = 2 * math.pi * radius * (radius + height)
    volume = math.pi * radius ** 2 * height
    print(f"Surface area of the cylinder: {surface_area}")
    print(f"Volume of the cylinder: {volume}")

def sphere():
    radius = float(input("Enter the radius of the sphere: "))
    surface_area = 4 * math.pi * radius ** 2
    volume = (4 / 3) * math.pi * radius ** 3
    print(f"Surface area of the sphere: {surface_area}")
    print(f"Volume of the sphere: {volume}")


# Main script
print("Welcome to the Shape Calculator!")
print("Select a shape:")
print("1. Rectangle")
print("2. Square")
print("3. Triangle")
print("4. Right Triangle")
print("5. Pythagorean Theorem")
print("6. Isosceles Triangle")
print("7. Equilateral Triangle")
print("8. Trapezoid")
print("9. Circle")
print("10. Rectangular Solid")
print("11. Cube")
print("12. Cone")
print("13. Right Circular Cylinder")
print("14. Sphere")

shape_choice = int(input("Enter the corresponding number to select a shape: "))

if shape_choice == 1:
    rectangle()
elif shape_choice == 2:
    square()
elif shape_choice == 3:
    triangle()
elif shape_choice == 4:
    right_triangle()
elif shape_choice == 5:
    pythagorean_theorem()
elif shape_choice == 6:
    isosceles_triangle()
elif shape_choice == 7:
    equilateral_triangle()
elif shape_choice == 8:
    trapezoid()
elif shape_choice == 9:
    circle()
elif shape_choice == 10:
    rectangular_solid()
elif shape_choice == 11:
    cube()
elif shape_choice == 12:
    cone()
elif shape_choice == 13:
    right_circular_cylinder()
elif shape_choice == 14:
    sphere()
else:
    print("Invalid choice!")
