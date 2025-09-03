from math import pi

# define a function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return 


# Calculating area of rectangles
length1 = 10
width1 = 5
area_rectangle1 = calculate_rectangle_area(length1, width1)

length2 = 15
width2 = 7
area_rectangle2 = calculate_rectangle_area(length2, width2)

# Calculating area of circles
radius1 = 4
area_circle1 = pi * (radius1 ** 2)

radius2 = 6
area_circle2 = pi * (radius2 ** 2)

print("Area of first rectangle:", area_rectangle1)
print("Area of second rectangle:", area_rectangle2)
print("Area of first circle:", area_circle1)
print("Area of second circle:", area_circle2)