# Brute Force Approach

import math

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def find_closest():
    closest = None
    most_min = float("inf")

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            min_value = euclidean_distance(points[i], points[j])
            if min_value < most_min:
                closest = (points[i], points[j])
                most_min = min_value

    return closest, most_min


print(find_closest())
