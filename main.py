class Point:
    """
    Establece las coordenadas rectangulares
    en un mapa cartesiano.
    """
    def __init__(self, x_coordinate, y_coordinate) -> None:
        self.x = x_coordinate
        self.y = y_coordinate

class Circle:
    """
    Crea un círculo a partir de un punto y
    el radio.
    """
    def __init__(self, center_coordinates: Point, radius: float) -> None:
        self.center_coordinates = center_coordinates
        self.radius = radius

    def is_point_inside(self, new_point: Point) -> bool:
        """
        Devuelve un booleano que indica si un punto dado por
        el usuario está dentro del circulo definido.
        """
        diff_x = self.center_coordinates.x - new_point.x
        diff_y = self.center_coordinates.y - new_point.y
        distance_beetween_points = (diff_x ** 2 + diff_y ** 2) ** 0.5
        return distance_beetween_points <= self.radius

if __name__ == "__main__":
    print("Ingresa el punto central del círculo")
    print("Coordenada en X:")
    centerX = float(input())
    print("Coordenada en Y:")
    centerY = float(input())
    print("Ingresa el radio del círculo:")
    radius = float(input())

    center_point = Point(centerX, centerY)
    circle = Circle(center_point, radius)

    print("Ingresa coordenadas del punto a evaluar")
    print("Coordenada en X:")
    x_coordinate = float(input())
    print("Coordenada en Y:")
    y_coordinate = float(input())

    given_point = Point(x_coordinate, y_coordinate)
    is_inside = circle.is_point_inside(given_point)

    if is_inside:
        print("\nEl punto está dentro del círculo")
    else:
        print("\nEl punto está fuera del círculo")