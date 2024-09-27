Here’s a **Binary Search** practice problem for you:

---

### Problem: **Find Element in a Sorted Array**

You are given a **sorted array** of integers and a target value. Your task is to write a function that uses **Binary Search** (a divide and conquer algorithm) to determine whether the target value exists in the array. If the target value is found, return its index. If the target value is not found, return `-1`.

#### Binary Search Recap:
- **Step 1**: Divide the array into two halves by calculating the middle index.
- **Step 2**: Compare the middle element with the target:
   - If the middle element is equal to the target, return its index.
   - If the middle element is greater than the target, search the left half.
   - If the middle element is smaller than the target, search the right half.
- **Step 3**: Repeat the process on the appropriate half until the element is found or the array cannot be divided further.

### Input:
- A sorted array `arr[]` of integers of size \( n \).
- A target integer `target`.

### Output:
- Return the index of the target element in the array.
- If the target is not found, return `-1`.

### Constraints:
- The array is sorted in ascending order.
- You must implement this using **binary search**.
- The time complexity should be \( O(\log n) \).

### Example:

#### Input:
```python
arr = [-5, 0, 3, 7, 9, 12, 16, 19]
target = 9
```

#### Output:
```
4
```
(Explanation: The target value `9` is at index `4` in the sorted array.)

#### Input:
```python
arr = [-5, 0, 3, 7, 9, 12, 16, 19]
target = 6
```

#### Output:
```
-1
```
(Explanation: The target value `6` is not found in the array, so the output is `-1`.)

---

### Follow-up Challenges:
1. Modify the problem to return the **first occurrence** of the target if the array contains duplicate values.
2. Implement a **recursive** version of the binary search algorithm.
3. Extend the problem to find a range of indices in which the target occurs (if it appears multiple times).