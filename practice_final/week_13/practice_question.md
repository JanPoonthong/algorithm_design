Here’s a **Divide and Conquer** problem for you to practice, similar in concept to the problems you might see in your exam:

---

### Problem: **Closest Pair of Points**

You are given a list of \( n \) points in a 2D plane, each represented by its \( x \)- and \( y \)-coordinates. Your task is to find the **pair of points** that are closest to each other in terms of **Euclidean distance**.

#### Steps:

1. **Brute Force Approach**:
   Write a program that calculates the distance between every pair of points using the formula:
   \[
   \text{distance}(p1, p2) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
   \]
   where \( p1 = (x_1, y_1) \) and \( p2 = (x_2, y_2) \).
   - Compare every possible pair of points, and return the minimum distance.
   - Time Complexity: \( O(_____ ) \)

2. **Divide and Conquer Approach**:
   - **Step 1**: Sort the points based on their \( x \)-coordinates.
   - **Step 2**: Split the points into two halves: left and right.
   - **Step 3**: Recursively find the smallest distance in both the left and right halves.
   - **Step 4**: Combine the results by checking for points near the dividing line, and ensure the closest pair might not be split between two halves.
   
   Use the following logic for combining the results:
   - Let \( \delta \) be the minimum distance found in the left and right halves.
   - Look at the strip of points within distance \( \delta \) of the dividing line. Check only the points within this strip to see if a pair is closer than \( \delta \).
   - Return the overall minimum distance.
   
   **Note**: Make sure to handle base cases where the number of points in the subset is small (e.g., 2 or 3 points).

   - Time Complexity of Divide and Conquer: \( O( _______ ) \)

#### Input:
- A list of \( n \) points where each point is represented as a tuple \( (x, y) \).

#### Output:
- The smallest distance between any two points.

### Example:

#### Input:
```
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
```

#### Output:
```
1.414213 (the distance between points (2, 3) and (3, 4))
```

---

### Why this problem is useful:
- This problem helps you understand how to apply **Divide and Conquer** for geometrical problems.
- It teaches you to optimize a brute-force approach (with \( O(n^2) \)) into a much faster solution by breaking the problem into smaller subproblems.
- It combines recursion with merging results, giving you practice with the "combine" step in divide and conquer.

### Bonus:
After solving with Divide and Conquer, you can try implementing it using a more efficient approach with sorting and exploring smaller subsets.

