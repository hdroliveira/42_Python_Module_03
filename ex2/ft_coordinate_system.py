import math


def calculate_distance(p1: tuple, p2: tuple) -> float:
    """Calcula a distancia de form Euclidiana entre dois pontos
    Fórmula: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)"""

    x_diff = (p2[0] - p1[0]) ** 2
    y_diff = (p2[1] - p1[1]) ** 2
    z_diff = (p2[2] - p1[2]) ** 2

    return math.sqrt(x_diff + y_diff + z_diff)


def parse_coordinates(coord_str: str) -> tuple:
    """Tenta converter uma string "x, y, z" em tuplo (x, y, z)
    Envia ValueError se a conversao falhar"""
    parts = coord_str.split(',')

    if len(parts) != 3:
        raise ValueError("Coordinates must have exactly 3 parts (x, y, z)")
    coords_list = [int(part) for part in parts]
    return tuple(coords_list)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    pos1 = (10, 20, 5)
    origin = (0, 0, 0)
    print(f"Position created: {pos1}")

    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1:.2f}\n")

    input_str = "3,4,0"
    print(f"Parsing coordinates: \"{input_str}\"")

    try:
        pos2 = parse_coordinates(input_str)
        print(f"Parsed position: {pos2}")

        dist2 = calculate_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {dist2:.1f}\n")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")

    bad_input = "abc, def, ghi"
    print(f"Parsing invalid coordinates: \"{bad_input}\"")

    try:
        parse_coordinates(bad_input)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details Type: {type(e).__name__}, Args: {e.args}\n")

    print("Unpacking demonstration:")
    x, y, z = pos2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x} Y={y} Z={z}")


if __name__ == "__main__":
    main()
