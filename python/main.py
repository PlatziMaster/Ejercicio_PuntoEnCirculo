import os

def where_is_circle(
    radius: float,
    dot_x: float,
    dot_y: float,
    center_x: float = 0.0,
    center_y: float = 0.0,
) -> str:
    """
    Determine if a given dot is inside or outside of a circle.
    NOTE: If dot is on the circle, it is considered inside.
    """

    if (radius < 0):
        raise ValueError("Radius can't be less 0.")

    side_a = abs(dot_x - center_x)
    side_b = abs(dot_y - center_x)
    hypotenuse = (side_a ** 2 + side_b ** 2) ** 0.5

    if (hypotenuse > radius):
        return "outside"
    else:
        return "inside"

if __name__ == "__main__":
    os.system("clear")
    print('Exercise Dot In Circle:')
    print('Insert radius:')
    radius = float(input())

    os.system("clear")
    print('Exercise Dot In Circle:')
    print('Insert x coordinate for dot:')
    dot_x = float(input())

    os.system("clear")
    print('Exercise Dot In Circle:')
    print('Insert y coordinate for dot:')
    dot_y = float(input())

    os.system("clear")
    print('Exercise Dot In Circle:')
    print('Would you like move circle\'s center: (y/N)')
    decision = input()

    if (decision == 'y'):
        os.system("clear")
        print('Exercise Dot In Circle:')
        print('Insert x coordinate for center:')
        center_x = float(input())

        os.system("clear")
        print('Exercise Dot In Circle:')
        print('Insert y coordinate for center:')
        center_y = float(input())

        os.system("clear")
        print('Exercise Dot In Circle:')
        location = where_is_circle(radius, dot_x, dot_y, center_x, center_y)
        print('The dot is ' + location)

    else:
        os.system("clear")
        print('Exercise Dot In Circle:')
        location = where_is_circle(radius, dot_x, dot_y)
        print('The dot is ' + location)
