from math import pi

# define a function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return pi * (radius ** 2) 


# Calculating area of rectangles
rectangles = [
    {"length": 10, "width": 5},
    {"length": 5, "width": 7},
]

current_rectangle = 1
for rectangle in rectangles:
    print(f"Area of rectangle {current_rectangle}: {calculate_rectangle_area(rectangle["length"], rectangle["width"])}")
    current_rectangle += 1
    
# Calculating area of circles
radius1 = 4
area_circle1 = calculate_circle_area(radius1)

radius2 = 6
area_circle2 = calculate_circle_area(radius2)


print("Area of first circle:", round(area_circle1, 2))
print("Area of second circle:", round(area_circle2, 2))