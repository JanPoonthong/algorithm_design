import math


# Helper function to calculate distance between two points
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Brute force method for small sets of points
def brute_force_closest_pair(points):
    min_dist = float("inf")
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, dist(points[i], points[j]))
    return min_dist


# Function to find the closest pair in a strip
def closest_in_strip(strip, d):
    min_dist = d
    n = len(strip)

    # Only check points within delta distance in y-coordinate
    for i in range(n):
        for j in range(i + 1, n):
            if strip[j][1] - strip[i][1] < min_dist:
                min_dist = min(min_dist, dist(strip[i], strip[j]))
    return min_dist


# Recursive function for divide and conquer
def closest_pair_dc(points_sorted_x, points_sorted_y):
    n = len(points_sorted_x)

    # Base case when the points are small
    if n <= 3:
        return brute_force_closest_pair(points_sorted_x)

    # Split points into two halves
    mid = n // 2
    mid_point = points_sorted_x[mid]

    left_x = points_sorted_x[:mid]
    right_x = points_sorted_x[mid:]

    left_y = list(filter(lambda x: x[0] <= mid_point[0], points_sorted_y))
    right_y = list(filter(lambda x: x[0] > mid_point[0], points_sorted_y))

    # Recursively find the smallest distance in both halves
    delta_left = closest_pair_dc(left_x, left_y)
    delta_right = closest_pair_dc(right_x, right_y)

    # Get the minimum distance from both halves
    delta = min(delta_left, delta_right)

    # Build a strip of points within delta distance from the dividing line
    strip = [point for point in points_sorted_y if abs(point[0] - mid_point[0]) < delta]

    # Find the closest distance in the strip
    return min(delta, closest_in_strip(strip, delta))


# Main function to start divide and conquer approach
def closest_pair_of_points(points):
    points_sorted_x = sorted(points, key=lambda x: x[0])
    points_sorted_y = sorted(points, key=lambda x: x[1])

    return closest_pair_dc(points_sorted_x, points_sorted_y)


# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("Closest distance:", closest_pair_of_points(points))
