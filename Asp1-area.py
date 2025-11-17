import math

def calculate_square_area():
    # Given values
    theta = 60  # angle in degrees
    radius = 42

    # Calculate the length of the arc
    arc_length = (theta / 360) * 2 * math.pi * radius

    # Calculate the side length of the square
    side_length = arc_length / 4

    # Calculate the area of the square
    area = side_length ** 2

    return area


square_area = calculate_square_area()
print("The area of the square is:", round(square_area, 2))
