import math

points = [(0, 1), (2, 4), (3, 6), (7, 7)]

def distance(x1, y1, x2, y2):
    distance = math.sqrt(((x2 - x1)**2) + (y2 - y1)**2)
    return distance

d1 = distance(0, 1, 2, 4)
d2 = distance(0, 1, 3, 9)
d3 = distance(0, 1, 7, 7)
d4 = distance(2, 4, 3, 6)
d5 = distance(2, 4, 7, 7)
d6 = distance(3, 6, 7, 7)

print(f"{d1} {d2} {d3} {d4} {d5} {d6}")


def polar_coordinates(point):
    x, y = point
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta

point = points[2]
r, theta = polar_coordinates(point)
print(f"Polar coordinates of {point}: r = {r}, theta = {math.degrees(theta)}°")


def move_point(point, dx, dy):
    x, y = point
    new_x = x + dx
    new_y = y + dy
    return new_x, new_y


point = points[2]
dx, dy = 2, 3
new_position = move_point(point, dx, dy)
print(f"New position of {point} after moving by ({dx},{dy}): {new_position}")
